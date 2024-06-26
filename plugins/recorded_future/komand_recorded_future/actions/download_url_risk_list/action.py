import insightconnect_plugin_runtime
from .schema import DownloadUrlRiskListInput, DownloadUrlRiskListOutput, Input, Output, Component

# Custom imports below
import base64
from insightconnect_plugin_runtime.helper import clean
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint


class DownloadUrlRiskList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_url_risk_list",
            description=Component.DESCRIPTION,
            input=DownloadUrlRiskListInput(),
            output=DownloadUrlRiskListOutput(),
        )

    def run(self, params={}):
        query_params = {"format": "xml/stix/1.2", "gzip": "true"}
        risk_list = AvailableInputs.UrlRiskRuleMap.get(params.get(Input.LIST))
        if risk_list:
            query_params[Input.LIST] = risk_list
        response_content, response_dict = self.connection.client.make_request(
            Endpoint.download_url_risk_list(), query_params
        )
        data = {
            Output.RISK_LIST: response_dict,
            Output.RISK_LIST_GZIP: {
                "filename": "risk_list.gzip",
                "content": response_content,
            },
        }
        return clean(data)
