import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_cisco_umbrella_destinations.actions.dlFilterAll import DlFilterAll
from icon_cisco_umbrella_destinations.actions.dlFilterAll.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from mock import (
    Util,
    STUB_ACCESS,
    STUB_IS_GLOBAL,
    STUB_MSP_DEFAULT,
    STUB_DELETION,
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    mocked_request,
)


class TestDlFilterAll(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DlFilterAll())
        self.params = {
            Input.ACCESS: STUB_ACCESS,
            Input.ISMSPDEFAULT: STUB_MSP_DEFAULT,
            Input.ISGLOBAL: STUB_IS_GLOBAL,
            Input.MARKEDFORDELETION: STUB_DELETION,
        }

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_success(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected_response = {
            "data": [
                {
                    "id": 5798992,
                    "access": "block",
                    "isGlobal": False,
                    "name": "Block For All",
                    "createdAt": "2020-05-19T20:58:55+0000",
                    "modifiedAt": "2020-05-19T21:11:15+0000",
                    "isMspDefault": False,
                    "markedForDeletion": False,
                    "bundleTypeId": 1,
                    "meta": {
                        "destinationCount": 0,
                        "domainCount": 0,
                        "urlCount": 0,
                        "ipv4Count": 0,
                        "applicationCount": 0,
                    },
                }
            ]
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
