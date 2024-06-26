import insightconnect_plugin_runtime

from .schema import GetAssetsInput, GetAssetsOutput, Component, Output, Input

from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_assets",
            description=Component.DESCRIPTION,
            input=GetAssetsInput(),
            output=GetAssetsOutput(),
        )

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_offenses_request(params=params, fields=[Input.RANGE, Input.FILTER, Input.FIELDS])
        return {Output.DATA: response}
