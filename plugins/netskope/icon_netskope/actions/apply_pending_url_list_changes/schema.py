# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Applies currently pending changes for URL lists"


class Input:
    pass


class Output:
    DEPLOYED_URLLISTS = "deployed_urllists"


class ApplyPendingUrlListChangesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ApplyPendingUrlListChangesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "deployed_urllists": {
      "type": "array",
      "title": "Deployed URL Lists",
      "description": "Contains list of deployed URL lists",
      "items": {
        "$ref": "#/definitions/urllist"
      },
      "order": 1
    }
  },
  "required": [
    "deployed_urllists"
  ],
  "definitions": {
    "urllist": {
      "type": "object",
      "title": "urllist",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "URL list identifier",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "URL list name",
          "order": 2
        },
        "data": {
          "$ref": "#/definitions/data",
          "title": "Data",
          "description": "Data containing URLs and type",
          "order": 3
        },
        "modify_type": {
          "type": "string",
          "title": "Modify Type",
          "description": "Shows last modification type. Expected values are Created, Edited, Deleted",
          "order": 4
        },
        "modify_by": {
          "type": "string",
          "title": "Modify By",
          "description": "Name of the URL list modifier",
          "order": 5
        },
        "modify_time": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Modify Time",
          "description": "Last URL list modification time",
          "order": 6
        },
        "pending": {
          "type": "integer",
          "title": "Pending",
          "description": "URL list status of pending (1) and applied (0)",
          "order": 7
        }
      },
      "required": [
        "id",
        "modify_by",
        "modify_time",
        "modify_type",
        "name",
        "pending"
      ]
    },
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "urls": {
          "type": "array",
          "title": "URLs",
          "description": "List of URLs",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "URL List Category",
          "description": "Category of URL list",
          "order": 2
        }
      },
      "required": [
        "type",
        "urls"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
