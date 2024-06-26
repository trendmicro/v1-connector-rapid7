import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from parameterized import parameterized
from icon_rapid7_intsights.actions.get_iocs_for_cyber_term import GetIocsForCyberTerm
from icon_rapid7_intsights.actions.get_iocs_for_cyber_term.schema import (
    GetIocsForCyberTermInput,
    GetIocsForCyberTermOutput,
)
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.request", side_effect=Util.mock_request)
class TestGetIocsForCyberTerm(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIocsForCyberTerm())

    @parameterized.expand(
        [
            [
                "no_params",
                Util.read_file_to_dict("inputs/get_iocs_cyber_term_no_params.json.inp"),
                Util.read_file_to_dict("expecteds/get_iocs_cyber_term_no_params.json.exp"),
            ],
            [
                "params_1",
                Util.read_file_to_dict("inputs/get_iocs_cyber_term_params_1.json.inp"),
                Util.read_file_to_dict("expecteds/get_iocs_cyber_term_params_1.json.exp"),
            ],
            [
                "params_2",
                Util.read_file_to_dict("inputs/get_iocs_cyber_term_params_2.json.inp"),
                Util.read_file_to_dict("expecteds/get_iocs_cyber_term_params_2.json.exp"),
            ],
        ]
    )
    def test_get_iocs_for_cyber_term(self, mock_request, test_name, input_params, expected):
        validate(input_params, GetIocsForCyberTermInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, GetIocsForCyberTermOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_param",
                Util.read_file_to_dict("inputs/get_iocs_cyber_term_params_bad.json.inp"),
                PluginException(preset=PluginException.Preset.BAD_REQUEST),
            ],
            [
                "cyber_term_not_found",
                Util.read_file_to_dict("inputs/get_iocs_cyber_term_invalid_id.json.inp"),
                PluginException(preset=PluginException.Preset.NOT_FOUND),
            ],
        ]
    )
    def test_get_iocs_for_cyber_term_raise_exception(self, mock_request, test_name, input_parameters, expected_error):
        validate(input_parameters, GetIocsForCyberTermInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, expected_error.cause)
        self.assertEqual(error.exception.assistance, expected_error.assistance)
