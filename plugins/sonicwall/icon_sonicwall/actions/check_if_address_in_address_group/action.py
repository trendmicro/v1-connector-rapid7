import insightconnect_plugin_runtime
from .schema import (
    CheckIfAddressInAddressGroupInput,
    CheckIfAddressInAddressGroupOutput,
    Input,
    Output,
    Component,
)


# Custom imports below


class CheckIfAddressInAddressGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_if_address_in_address_group",
            description=Component.DESCRIPTION,
            input=CheckIfAddressInAddressGroupInput(),
            output=CheckIfAddressInAddressGroupOutput(),
        )

    def run(self, params={}):  # noqa MC0001
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.ADDRESS, "")
        group_name = params.get(Input.GROUP, "")
        address = params.get(Input.ADDRESS, "")
        enable_search = params.get(Input.ENABLE_SEARCH, False)
        # END INPUT BINDING - DO NOT REMOVE

        objects_matching, address_objects_names = [], []
        address_group = self.connection.sonicwall_api.get_group(group_name).get("group_object", {})
        address_object = {}

        for ip in ("ipv4", "ipv6"):
            for value in address_group.values():
                if isinstance(value, list) and value:
                    address_object = next((element.get(ip, {}).get("address_object", {}) for element in value), {})
                elif isinstance(value, dict):
                    address_object = value.get(ip, {}).get("address_object", {})
                if address_object:
                    break
            address_objects_names.extend(address_object.get("ipv4", []))
            address_objects_names.extend(address_object.get("ipv6", []))
            address_objects_names.extend(address_object.get("mac", []))
            address_objects_names.extend(address_object.get("fqdn", []))

        for object_from_group in address_objects_names:
            if object_from_group.get("name") == address:
                objects_matching.append(object_from_group)

        if len(objects_matching) == 0 and enable_search:
            self.logger.info("Results not found on first scan. Searching for results...")
            for object_from_group in address_objects_names:
                response = self.connection.sonicwall_api.get_address_object(object_from_group.get("name"))
                object_type, address_object_response = response.get("object_type", {}), response.get(
                    "address_object", {}
                )

                address_object = {}
                for value in address_object_response.values():
                    if isinstance(value, list) and value:
                        address_object = next((element.get(object_type, {}) for element in value), {})
                    elif isinstance(value, dict):
                        address_object = value.get(object_type, {})
                    if address_object:
                        break

                upper_name = name.upper()
                if (
                    upper_name == address_object.get("address", "").upper()
                    or upper_name.replace(":", "") == address_object.get("address", "").upper()
                    or upper_name == address_object.get("host", {}).get("ip", "").upper()
                    or upper_name == address_object.get("domain", "").upper()
                ):
                    objects_matching.append(address_object)

        return {Output.FOUND: len(objects_matching) > 0, Output.ADDRESS_OBJECTS: objects_matching}
