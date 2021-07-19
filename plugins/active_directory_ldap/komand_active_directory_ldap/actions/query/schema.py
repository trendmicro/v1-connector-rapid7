# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Run an LDAP query"


class Input:
    ATTRIBUTES = "attributes"
    SEARCH_BASE = "search_base"
    SEARCH_FILTER = "search_filter"
    

class Output:
    COUNT = "count"
    RESULTS = "results"
    

class QueryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attributes": {
      "type": "array",
      "title": "Attributes",
      "description": "Attributes to search. If empty return all attributes",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "search_base": {
      "type": "string",
      "title": "Search Base",
      "description": "The base of the search request",
      "order": 2
    },
    "search_filter": {
      "type": "string",
      "title": "Search Filter",
      "description": "The filter of the search request. It must conform to the LDAP filter syntax specified in RFC4515",
      "order": 1
    }
  },
  "required": [
    "search_base",
    "search_filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of results",
      "order": 2
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results returned",
      "items": {
        "$ref": "#/definitions/result"
      },
      "order": 1
    }
  },
  "definitions": {
    "result": {
      "type": "object",
      "title": "result",
      "properties": {
        "attributes": {
          "type": "object",
          "title": "Attributes",
          "order": 1
        },
        "dn": {
          "type": "string",
          "title": "Dn",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)