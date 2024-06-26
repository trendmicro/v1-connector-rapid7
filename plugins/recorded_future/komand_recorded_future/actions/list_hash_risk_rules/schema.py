# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List available filtration rules for hash risk lists"


class Input:
    pass


class Output:
    RISK_RULES = "risk_rules"


class ListHashRiskRulesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListHashRiskRulesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_rules": {
      "type": "array",
      "title": "Risk Rules",
      "description": "Risk rules",
      "items": {
        "$ref": "#/definitions/risk_rule"
      },
      "order": 1
    }
  },
  "required": [
    "risk_rules"
  ],
  "definitions": {
    "risk_rule": {
      "type": "object",
      "title": "risk_rule",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 2
        },
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "description": "Criticality",
          "order": 3
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "description": "Criticality label",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
