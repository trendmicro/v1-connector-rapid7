# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create an issue ticket"


class Input:
    ASSIGNEE = "assignee"
    BODY = "body"
    LABELS = "labels"
    MILESTONE = "milestone"
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    TITLE = "title"


class Output:
    URL = "url"


class CreateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assignee": {
      "type": "string",
      "description": "User to assign this issue to",
      "order": 6
    },
    "body": {
      "type": "string",
      "description": "Body text of issue",
      "order": 2
    },
    "labels": {
      "type": "string",
      "description": "GitHub search tags delimited by commas",
      "order": 3
    },
    "milestone": {
      "type": "number",
      "description": "ID of the milestone to associate this issue with",
      "order": 7
    },
    "organization": {
      "type": "string",
      "description": "Organizational owner of repository",
      "order": 5
    },
    "repository": {
      "type": "string",
      "description": "Repository to post issue",
      "order": 4
    },
    "title": {
      "type": "string",
      "description": "Title of issue",
      "order": 1
    }
  },
  "required": [
    "body",
    "repository",
    "title"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
