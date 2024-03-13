# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add email sender to event"


class Input:
    COMMENT = "comment"
    DISTRIBUTION = "distribution"
    EVENT = "event"
    PROPOSAL = "proposal"
    SENDER = "sender"


class Output:
    STATUS = "status"


class AddEmailSenderInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Attribute comment",
      "order": 3
    },
    "distribution": {
      "type": "string",
      "title": "Distribution",
      "description": "Distribution type",
      "enum": [
        "This Community",
        "This Organization",
        "Connected Communities",
        "All Communities"
      ],
      "order": 4
    },
    "event": {
      "type": "string",
      "title": "Event ID",
      "description": "Event ID to append to",
      "order": 2
    },
    "proposal": {
      "type": "boolean",
      "title": "Proposal",
      "description": "Mark request as a proposal (Default: false)",
      "default": false,
      "order": 5
    },
    "sender": {
      "type": "string",
      "title": "Sender",
      "description": "Sender email address",
      "order": 1
    }
  },
  "required": [
    "comment",
    "distribution",
    "event",
    "proposal",
    "sender"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddEmailSenderOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Email sender add status",
      "order": 1
    }
  },
  "required": [
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
