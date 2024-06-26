# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates the File Hash List with the values provided"


class Input:
    LIST = "list"
    NAME = "name"


class Output:
    MESSAGE = "message"
    STATUS = "status"


class UpdateFileHashListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "list": {
      "type": "array",
      "title": "Hashes",
      "description": "Comma-separated list of file hashes (MD5 or SHA256), with the maximum size of the list being 8MB",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of an existing File Hash List shown in the Netskope UI on the File Hash List page",
      "order": 1
    }
  },
  "required": [
    "list",
    "name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateFileHashListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "API response message",
      "order": 2
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "API response status",
      "order": 1
    }
  },
  "required": [
    "message",
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
