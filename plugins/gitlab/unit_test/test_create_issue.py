import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.create_issue import CreateIssue
from icon_gitlab.actions.create_issue.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestCreateIssue(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(CreateIssue())
        self.params = {Input.TITLE: "Example Title", Input.PROJECT_ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_create_issue(self, mock_post: MagicMock) -> None:
        mocked_request(mock_post)
        response = self.action.run(self.params)

        expected = {
            Output.ISSUE: {
                "assignees": [
                    {
                        "avatar_url": "None",
                        "id": 18,
                        "name": "Alexandra Bashirian",
                        "state": "active",
                        "username": "eileen.lowe",
                        "web_url": "https://gitlab.example.com/eileen.lowe",
                    },
                    {
                        "avatar_url": "",
                        "id": 19,
                        "name": "John Smith",
                        "state": "active",
                        "username": "john.smith",
                        "web_url": "https://gitlab.example.com/john.smith",
                    },
                ],
                "author": {
                    "avatar_url": "",
                    "id": 18,
                    "name": "Alexandra Bashirian",
                    "state": "active",
                    "username": "eileen.lowe",
                    "web_url": "https://gitlab.example.com/eileen.lowe",
                },
                "confidential": True,
                "created_at": "2016-01-07 12:44:33.959000+00:00",
                "description": "Short description about the issue",
                "due_date": "2016-01-07 12:44:33.959000+00:00",
                "id": 12,
                "iid": 12,
                "labels": ["label1", "label2", "label3"],
                "milestone": {
                    "created_at": "2016-01-07 12:44:33.959000+00:00",
                    "description": "project description",
                    "due_date": "2016-01-07 12:44:33.959000+00:00",
                    "id": 3,
                    "iid": 34,
                    "project_id": 3,
                    "state": "Opened",
                    "title": "project title",
                    "updated_at": "2016-01-07 12:44:33.959000+00:00",
                },
                "project_id": 13,
                "state": "opened",
                "subscribed": True,
                "title": "Issues with auth",
                "updated_at": "2016-01-07 12:44:33.959000+00:00",
                "user_notes_count": 20,
                "web_url": "https://gitlab.example.com/eileen.lowe",
            }
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
