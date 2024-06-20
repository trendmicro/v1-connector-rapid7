# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This will require the user to log back in after any page they are on is refreshed by invalidating all refresh tokens and cookies"


class Input:
    USER_ID = "user_id"


class Output:
    SUCCESS = "success"


class RevokeSignInSessionsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID to revoke",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RevokeSignInSessionsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was the operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
