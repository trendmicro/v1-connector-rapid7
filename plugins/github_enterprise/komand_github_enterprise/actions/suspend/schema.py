# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Suspend user from enterprise"


class Input:
    USERNAME = "username"
    

class Output:
    STATUS = "status"
    

class SuspendInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "username": {
      "type": "string",
      "title": "Username",
      "description": "GitHub username",
      "order": 1
    }
  },
  "required": [
    "username"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SuspendOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)