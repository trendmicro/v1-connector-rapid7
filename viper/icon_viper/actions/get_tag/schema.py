# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a single tag for this project"


class Input:
    ID = "id"
    PROJECT_NAME = "project_name"
    

class Output:
    TAG = "tag"
    

class GetTagInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Tag ID",
      "order": 2
    },
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "order": 1
    }
  },
  "required": [
    "id",
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTagOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tag": {
      "$ref": "#/definitions/Tag",
      "title": "Tag",
      "order": 1
    }
  },
  "required": [
    "tag"
  ],
  "definitions": {
    "Tag": {
      "type": "object",
      "title": "Tag",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Tag ID",
          "order": 1
        },
        "tag": {
          "type": "string",
          "title": "Name",
          "description": "Tag name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)