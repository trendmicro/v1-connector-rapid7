# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add sightings to organization"


class Input:
    SIGHTINGS = "sightings"


class Output:
    STATUS = "status"


class AddSightingsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sightings": {
      "type": "array",
      "title": "Sightings",
      "description": "Event sightings E.g. sighting, false-positive, expiration",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "sightings"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddSightingsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Sightings add status",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
