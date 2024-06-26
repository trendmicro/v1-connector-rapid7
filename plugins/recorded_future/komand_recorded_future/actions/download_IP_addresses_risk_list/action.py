import insightconnect_plugin_runtime
from .schema import DownloadIPAddressesRiskListInput, DownloadIPAddressesRiskListOutput, Input, Output, Component

# Custom imports below
import base64
from insightconnect_plugin_runtime.helper import clean
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint


class DownloadIPAddressesRiskList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_IP_addresses_risk_list",
            description=Component.DESCRIPTION,
            input=DownloadIPAddressesRiskListInput(),
            output=DownloadIPAddressesRiskListOutput(),
        )

    def run(self, params={}):
        query_params = {"format": "xml/stix/1.2", "gzip": "true"}
        risk_list = AvailableInputs.IpRiskRuleMap.get(params.get(Input.LIST))
        if risk_list:
            query_params[Input.LIST] = risk_list
        response_content, response_dict = self.connection.client.make_request(
            Endpoint.download_ip_risk_list(), query_params
        )
        data = {
            Output.RISK_LIST: response_dict,
            Output.RISK_LIST_GZIP: {
                "filename": "risk_list.gzip",
                "content": response_content,
            },
        }
        return clean(data)
