# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Lock the user's computer by its ID"


class Input:
    ID = "ID"
    PASSCODE = "passcode"
    

class Output:
    STATUS = "status"
    

class LockComputerInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ID": {
      "type": "string",
      "title": "Computer ID",
      "description": "Identifier of the computer",
      "order": 1
    },
    "passcode": {
      "type": "string",
      "title": "Computer Passcode",
      "description": "The passcode of the computer",
      "order": 2
    }
  },
  "required": [
    "ID",
    "passcode"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LockComputerOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)