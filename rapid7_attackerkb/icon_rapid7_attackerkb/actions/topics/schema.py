# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return all topics"


class Input:
    CREATED = "created"
    DISCLOSUREDATE = "disclosureDate"
    DOCUMENT = "document"
    EDITORID = "editorId"
    ID = "id"
    NAME = "name"
    PAGE = "page"
    REVISIONDATE = "revisionDate"
    SIZE = "size"
    

class Output:
    DATA = "data"
    

class TopicsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "created": {
      "type": "string",
      "title": "Created",
      "description": "Return all topics that were created on the given date, eg. 2019-07-04",
      "order": 4
    },
    "disclosureDate": {
      "type": "string",
      "title": "Disclosure Date",
      "description": "Return all topics that were disclosed on the given date, eg. 2019-07-04",
      "order": 6
    },
    "document": {
      "type": "string",
      "title": "Document",
      "description": "Text to query the document parameter. A substring match is performed, eg. RDP",
      "order": 7
    },
    "editorId": {
      "type": "string",
      "title": "Editor ID",
      "description": "The UUID of a contributor",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The UUID of a specific topic to return",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Text to query the name parameter. A substring match is performed",
      "order": 3
    },
    "page": {
      "type": "string",
      "title": "Page",
      "description": "Pagination page number, default value is 0",
      "default": 0,
      "order": 8
    },
    "revisionDate": {
      "type": "string",
      "title": "Revision Date",
      "description": "Return all topics that were last edited on the given date, eg. 2019-07-04",
      "order": 5
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "The number of topics returned per page, default value is 10",
      "default": 10,
      "order": 9
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TopicsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Returned topic data",
      "items": {
        "$ref": "#/definitions/topic"
      },
      "order": 1
    }
  },
  "definitions": {
    "score": {
      "type": "object",
      "title": "score",
      "properties": {
        "attackerValue": {
          "type": "number",
          "title": "Attacker Value",
          "description": "The attacker value score",
          "order": 1
        },
        "exploitability": {
          "type": "number",
          "title": "Exploitability",
          "description": "The exploitability score",
          "order": 2
        }
      }
    },
    "tags": {
      "type": "object",
      "title": "tags",
      "properties": {
        "commonEnterprise": {
          "type": "number",
          "title": "Common Enterprise",
          "description": "The 'Common in enterprise' score",
          "order": 1
        },
        "defaultConfiguration": {
          "type": "number",
          "title": "Default Configuration",
          "description": "The 'Present in default configuration' score",
          "order": 2
        },
        "difficultToDevelop": {
          "type": "number",
          "title": "Difficult To Develop",
          "description": "The 'Difficult to develop' score",
          "order": 3
        },
        "difficultToExploit": {
          "type": "number",
          "title": "Difficult To Exploit",
          "description": "The 'High barrier to exploitation' score",
          "order": 6
        },
        "difficultToPatch": {
          "type": "number",
          "title": "Difficult To Patch",
          "description": "The 'Difficult to patch' score",
          "order": 7
        },
        "easyToDevelop": {
          "type": "number",
          "title": "Easy To Develop",
          "description": "The 'Easy to develop' score",
          "order": 8
        },
        "highPrivilegeAccess": {
          "type": "number",
          "title": "High Privilege Access",
          "description": "The 'Allows high-privileged access' score",
          "order": 9
        },
        "noUsefulData": {
          "type": "number",
          "title": "No Useful Data",
          "description": "The 'Does not produce useful data' score",
          "order": 10
        },
        "obscureConfiguration": {
          "type": "number",
          "title": "Obscure Configuration",
          "description": "The 'Only present in obscure configuration' score",
          "order": 11
        },
        "postAuth": {
          "type": "number",
          "title": "Post Auth",
          "description": "The 'Post-Auth' score",
          "order": 5
        },
        "preAuth": {
          "type": "number",
          "title": "Pre Auth",
          "description": "The 'Pre-Auth' score",
          "order": 4
        },
        "requiresInteraction": {
          "type": "number",
          "title": "Requires Interaction",
          "description": "The 'Requires user interaction' score",
          "order": 12
        }
      }
    },
    "topic": {
      "type": "object",
      "title": "topic",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "description": "The date and time the topic was created, eg. 2019-07-02T16:22:15.879357Z",
          "order": 1
        },
        "disclosureDate": {
          "type": "string",
          "title": "Disclosure Date",
          "description": "The date and time the topic was disclosed, eg. 2019-07-02T16:22:15.879357Z",
          "order": 8
        },
        "document": {
          "type": "string",
          "title": "Document",
          "description": "The main content of the topic",
          "order": 2
        },
        "editorId": {
          "type": "string",
          "title": "Editor ID",
          "description": "The UUID of the contributor who last edited the topic",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The UUID of the topic",
          "order": 4
        },
        "metadata": {
          "type": "object",
          "title": "Metadata",
          "description": "A JSON value containing key/value pairs describing various attributes about this topic",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name or title of the topic",
          "order": 6
        },
        "revisionDate": {
          "type": "string",
          "title": "Revision Date",
          "description": "The date and time the topic was last changed, eg. 2019-07-02T16:22:15.879357Z",
          "order": 7
        },
        "score": {
          "$ref": "#/definitions/score",
          "title": "Score",
          "description": "The topic score properties",
          "order": 9
        },
        "tags": {
          "$ref": "#/definitions/tags",
          "title": "Tags",
          "description": "The frequencies with which various tags appear on assessments",
          "order": 10
        }
      },
      "required": [
        "document",
        "name"
      ],
      "definitions": {
        "score": {
          "type": "object",
          "title": "score",
          "properties": {
            "attackerValue": {
              "type": "number",
              "title": "Attacker Value",
              "description": "The attacker value score",
              "order": 1
            },
            "exploitability": {
              "type": "number",
              "title": "Exploitability",
              "description": "The exploitability score",
              "order": 2
            }
          }
        },
        "tags": {
          "type": "object",
          "title": "tags",
          "properties": {
            "commonEnterprise": {
              "type": "number",
              "title": "Common Enterprise",
              "description": "The 'Common in enterprise' score",
              "order": 1
            },
            "defaultConfiguration": {
              "type": "number",
              "title": "Default Configuration",
              "description": "The 'Present in default configuration' score",
              "order": 2
            },
            "difficultToDevelop": {
              "type": "number",
              "title": "Difficult To Develop",
              "description": "The 'Difficult to develop' score",
              "order": 3
            },
            "difficultToExploit": {
              "type": "number",
              "title": "Difficult To Exploit",
              "description": "The 'High barrier to exploitation' score",
              "order": 6
            },
            "difficultToPatch": {
              "type": "number",
              "title": "Difficult To Patch",
              "description": "The 'Difficult to patch' score",
              "order": 7
            },
            "easyToDevelop": {
              "type": "number",
              "title": "Easy To Develop",
              "description": "The 'Easy to develop' score",
              "order": 8
            },
            "highPrivilegeAccess": {
              "type": "number",
              "title": "High Privilege Access",
              "description": "The 'Allows high-privileged access' score",
              "order": 9
            },
            "noUsefulData": {
              "type": "number",
              "title": "No Useful Data",
              "description": "The 'Does not produce useful data' score",
              "order": 10
            },
            "obscureConfiguration": {
              "type": "number",
              "title": "Obscure Configuration",
              "description": "The 'Only present in obscure configuration' score",
              "order": 11
            },
            "postAuth": {
              "type": "number",
              "title": "Post Auth",
              "description": "The 'Post-Auth' score",
              "order": 5
            },
            "preAuth": {
              "type": "number",
              "title": "Pre Auth",
              "description": "The 'Pre-Auth' score",
              "order": 4
            },
            "requiresInteraction": {
              "type": "number",
              "title": "Requires Interaction",
              "description": "The 'Requires user interaction' score",
              "order": 12
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
