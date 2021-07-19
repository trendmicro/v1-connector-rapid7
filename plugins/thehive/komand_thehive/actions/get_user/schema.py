# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get information about a user"


class Input:
    ID = "id"
    

class Output:
    _ID = "_id"
    _TYPE = "_type"
    CREATEDAT = "createdAt"
    CREATEDBY = "createdBy"
    HASKEY = "hasKey"
    ID = "id"
    NAME = "name"
    PREFERENCES = "preferences"
    ROLES = "roles"
    STATUS = "status"
    UPDATEDAT = "updatedAt"
    UPDATEDBY = "updatedBy"
    USER = "user"
    

class GetUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID. If empty, the current user is used",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_id": {
      "type": "string",
      "title": "_ID",
      "description": "User _ID",
      "order": 10
    },
    "_type": {
      "type": "string",
      "title": "Type",
      "description": "User type",
      "order": 2
    },
    "createdAt": {
      "type": "integer",
      "title": "Created At",
      "description": "Time the user was created at in milliseconds or epoch, e.g. 1496561862924",
      "order": 12
    },
    "createdBy": {
      "type": "string",
      "title": "Updated By",
      "description": "Created by",
      "order": 8
    },
    "hasKey": {
      "type": "boolean",
      "title": "HasKey",
      "description": "User has a key",
      "order": 3
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "ID",
      "order": 11
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name",
      "order": 4
    },
    "preferences": {
      "type": "object",
      "title": "Preferences",
      "description": "User preferences",
      "order": 13
    },
    "roles": {
      "type": "array",
      "title": "Roles",
      "description": "Roles",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Get user status",
      "order": 1
    },
    "updatedAt": {
      "type": "integer",
      "title": "Updated At",
      "description": "Time the user was updated in milliseconds or epoch, e.g. 1496561862924",
      "order": 6
    },
    "updatedBy": {
      "type": "string",
      "title": "Updated By",
      "description": "Updated by",
      "order": 9
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "User",
      "order": 7
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)