import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.delete_user import DeleteUser
from icon_gitlab.actions.delete_user.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestDeleteUser(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DeleteUser())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_delete_user(self, mock_delete: MagicMock) -> None:
        mocked_request(mock_delete)
        response = self.action.run(self.params)

        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
