# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a rule to block traffic"


class Input:
    ACTION = "action"
    DISCARD_OTHER_SESSIONS = "discard_other_sessions"
    LAYER = "layer"
    LIST_OF_SERVICES = "list_of_services"
    NAME = "name"
    POSITION = "position"
    

class Output:
    ACCESS_RULE = "access_rule"
    

class AddAccessRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Action to take",
      "default": "Drop",
      "enum": [
        "Accept",
        "Drop",
        "Ask",
        "Inform",
        "Reject",
        "User Auth",
        "Client Auth",
        "Apply Layer"
      ],
      "order": 4
    },
    "discard_other_sessions": {
      "type": "boolean",
      "title": "Discard Other Sessions",
      "description": "Discard all other user sessions. This can fix errors when objects are locked by other sessions",
      "default": true,
      "order": 6
    },
    "layer": {
      "type": "string",
      "title": "Layer",
      "description": "Layer to add this rule to",
      "default": "Network",
      "order": 3
    },
    "list_of_services": {
      "type": "array",
      "title": "List of services",
      "description": "List of services to block. e.g. [\\"AOL\\", \\"SMTP\\"]",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Rule name",
      "order": 1
    },
    "position": {
      "type": "string",
      "title": "Position",
      "description": "Postion in the list of rules. e.g. top, bottom, 15",
      "default": "top",
      "order": 5
    }
  },
  "required": [
    "action",
    "discard_other_sessions",
    "layer",
    "list_of_services",
    "name",
    "position"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAccessRuleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_rule": {
      "type": "object",
      "title": "Block Rule",
      "description": "The rule that was created",
      "order": 1
    }
  },
  "required": [
    "access_rule"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
