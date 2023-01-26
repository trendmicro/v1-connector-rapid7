# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete exemptions for provided IDs"


class Input:
    EXEMPTIONIDS = "exemptionIds"
    

class Output:
    SUCCESS = "success"
    

class RemoveExemptionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "exemptionIds": {
      "type": "array",
      "title": "Exemption IDs",
      "description": "List of exemption IDs to delete",
      "items": {
        "type": "integer"
      },
      "order": 1
    }
  },
  "required": [
    "exemptionIds"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveExemptionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)