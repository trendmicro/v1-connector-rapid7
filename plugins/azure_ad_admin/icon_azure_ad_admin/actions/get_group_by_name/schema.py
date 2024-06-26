# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a group by its name"


class Input:
    NAME = "name"


class Output:
    GROUP = "group"


class GetGroupByNameInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Display name to filter",
      "order": 1
    }
  },
  "required": [
    "name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetGroupByNameOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group": {
      "$ref": "#/definitions/group",
      "title": "Group",
      "description": "Group",
      "order": 1
    }
  },
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "mailNickname": {
          "type": "string",
          "title": "Mail Nickname",
          "description": "Mail nickname",
          "order": 1
        },
        "groupTypes": {
          "type": "array",
          "title": "Group Types",
          "description": "Group types",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display name",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 4
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 5
        },
        "securityEnabled": {
          "type": "boolean",
          "title": "Security Enabled",
          "description": "Security enabled",
          "order": 6
        },
        "renewedDateTime": {
          "type": "string",
          "title": "Renewed Date Time",
          "description": "Renewed date time",
          "order": 7
        },
        "proxyAddresses": {
          "type": "array",
          "title": "Proxy Addresses",
          "description": "Proxy addresses",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "visibility": {
          "type": "string",
          "title": "Visibility",
          "description": "Visibility",
          "order": 9
        },
        "mail": {
          "type": "string",
          "title": "Mail",
          "description": "Mail",
          "order": 10
        },
        "isAssignableToRole": {
          "type": "boolean",
          "title": "Is Assignable to Role",
          "description": "Is assignable to role",
          "order": 11
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 12
        },
        "mailEnabled": {
          "type": "boolean",
          "title": "Mail Enabled",
          "description": "Mail enabled",
          "order": 13
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
