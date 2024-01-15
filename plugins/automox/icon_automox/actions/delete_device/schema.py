# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete an Automox device"


class Input:
    DEVICE_ID = "device_id"
    ORG_ID = "org_id"


class Output:
    SUCCESS = "success"


class DeleteDeviceInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device_id": {
      "type": "integer",
      "title": "Device ID",
      "description": "Identifier of device",
      "order": 2
    },
    "org_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Identifier of organization",
      "order": 1
    }
  },
  "required": [
    "device_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteDeviceOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
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
