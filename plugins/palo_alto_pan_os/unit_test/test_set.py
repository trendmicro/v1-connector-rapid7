import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_palo_alto_pan_os.actions.set import Set
from komand_palo_alto_pan_os.actions.set.schema import Input, SetInput, SetOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestSet(TestCase):
    @parameterized.expand(
        [
            [
                "policy",
                "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Test Rule']",
                "<category><member>adult</member></category><action>drop</action>",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
            [
                "address_object",
                "/config/devices/entry/vsys/entry/address/entry[@name='example.com']",
                "<fqdn>example.com</fqdn><description>Test</description><tag><member>test</member></tag>",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
            [
                "address_group",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']",
                "<static><member>example.com</member></static>",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
        ]
    )
    def test_set(self, mock_get, mock_post, name, xpath, element, expected):
        action = Util.default_connector(Set())
        input_data = {Input.XPATH: xpath, Input.ELEMENT: element}
        validate(input_data, SetInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, SetOutput.schema)
