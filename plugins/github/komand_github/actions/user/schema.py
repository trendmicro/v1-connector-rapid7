# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get user information"


class Input:
    USERNAME = "username"


class Output:
    AVATAR = "avatar"
    BIO = "bio"
    EMAIL = "email"
    NAME = "name"
    URL = "url"


class UserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "username": {
      "type": "string",
      "description": "GitHub username",
      "order": 1
    }
  },
  "required": [
    "username"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "avatar": {
      "type": "string",
      "title": "Avatar",
      "description": "Avatar",
      "order": 4
    },
    "bio": {
      "type": "string",
      "title": "Bio",
      "description": "Bio",
      "order": 5
    },
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name",
      "order": 1
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 3
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
