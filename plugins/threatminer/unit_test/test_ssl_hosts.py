import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from mock import mock_request_200, mock_request_500, mock_request_503, mocked_request
from parameterized import parameterized
from utils import Util

from icon_threatminer.actions.ssl_hosts import SslHosts
from icon_threatminer.actions.ssl_hosts.schema import Input, Output


class TestSslHosts(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SslHosts())

    @parameterized.expand(
        [
            (
                {Input.QUERY: "42a8d5b3a867a59a79f44ffadd61460780fe58f2"},
                {
                    "status_code": 200,
                    "status_message": "Results found.",
                    "results": [{"value": "149.154.157.170"}, {"value": "149.154.157.171"}],
                },
            )
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_ssl_hosts(
        self, input_parameters: Dict[str, Any], expected: Dict[str, Any], mock_requests: MagicMock
    ) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.RESPONSE: expected})
        mock_requests.assert_called()

    @parameterized.expand(
        [
            (
                mock_request_500,
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ),
            (
                mock_request_503,
                PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE],
                PluginException.assistances[PluginException.Preset.SERVICE_UNAVAILABLE],
            ),
        ]
    )
    def test_ssl_hosts_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
