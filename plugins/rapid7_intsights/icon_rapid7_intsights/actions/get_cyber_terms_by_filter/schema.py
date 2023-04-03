# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get cyber terms for given filters"


class Input:
    LASTUPDATEFROM = "lastUpdateFrom"
    LASTUPDATETO = "lastUpdateTo"
    LIMIT = "limit"
    OFFSET = "offset"
    ORIGIN = "origin"
    SEARCH = "search"
    SEVERITY = "severity"
    TARGETCOUNTRY = "targetCountry"
    TARGETSECTOR = "targetSector"
    TTP = "ttp"
    TYPE = "type"
    

class Output:
    CYBERTERMS = "cyberTerms"
    NEXTOFFSET = "nextOffset"
    

class GetCyberTermsByFilterInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "lastUpdateFrom": {
      "type": "string",
      "title": "Last Updated From",
      "displayType": "date",
      "description": "Filter by last update date is greater than the given value (in ISO 8601 format)",
      "format": "date-time",
      "order": 8
    },
    "lastUpdateTo": {
      "type": "string",
      "title": "Last Updated To",
      "displayType": "date",
      "description": "Filter by last update date is less than the given value (in ISO 8601 format)",
      "format": "date-time",
      "order": 9
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Limit the results amount per chunk. Default value: 200",
      "order": 10
    },
    "offset": {
      "type": "string",
      "title": "Offset",
      "description": "Request the next page of cyber terms",
      "order": 11
    },
    "origin": {
      "type": "array",
      "title": "Origin",
      "description": "Filter by one or more nationalities",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "search": {
      "type": "string",
      "title": "Search",
      "description": "Filter by free text, which can be the cyber term name or ID",
      "order": 1
    },
    "severity": {
      "type": "array",
      "title": "Severity",
      "description": "Filter by one or more cyber term severities. Allowed values: High, Medium, Low",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "targetCountry": {
      "type": "array",
      "title": "Target Country",
      "description": "Filter by one or more targeted countries",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "targetSector": {
      "type": "array",
      "title": "Target Sector",
      "description": "Filter by one or more targeted sectors",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "ttp": {
      "type": "array",
      "title": "TTP",
      "description": "Filter by one or more TTPs",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "type": {
      "type": "array",
      "title": "Type",
      "description": "Filter by one or more cyber term types. Allowed values: ThreatActor, Malware, Campaign",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCyberTermsByFilterOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cyberTerms": {
      "type": "array",
      "title": "Cyber Terms",
      "description": "List of cyber terms that match the given filters",
      "items": {
        "$ref": "#/definitions/cyberTerm"
      },
      "order": 1
    },
    "nextOffset": {
      "type": "string",
      "title": "Next Offset",
      "description": "Indicator of the next page of cyber terms",
      "order": 2
    }
  },
  "definitions": {
    "cyberTerm": {
      "type": "object",
      "title": "cyberTerm",
      "properties": {
        "additionalInformation": {
          "type": "string",
          "title": "Additional Information",
          "description": "Additional information about the cyber term",
          "order": 13
        },
        "aliases": {
          "type": "array",
          "title": "Aliases",
          "description": "Aliases of the cyber term",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "createdDate": {
          "type": "string",
          "title": "Created Date",
          "description": "The date the cyber term was first reported",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID of the cyber term",
          "order": 1
        },
        "mitreAttack": {
          "type": "array",
          "title": "Mitre Attack",
          "description": "MITRE ATT\\u0026CK tactics and techniques of the cyber term, divided by tactics",
          "items": {
            "$ref": "#/definitions/mitreAttack"
          },
          "order": 17
        },
        "origins": {
          "type": "array",
          "title": "Origins",
          "description": "List of origin nationalities",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "overview": {
          "type": "string",
          "title": "Overview",
          "description": "Overview of the cyber term",
          "order": 12
        },
        "relatedCampaigns": {
          "type": "array",
          "title": "Related Campaigns",
          "description": "Related campaign names",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "relatedMalware": {
          "type": "array",
          "title": "Related Malware",
          "description": "Related malware names",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "relatedThreatActors": {
          "type": "array",
          "title": "Related Threat Actors",
          "description": "Related threat actor names",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity of the cyber term",
          "order": 4
        },
        "targetCountries": {
          "type": "array",
          "title": "Target Countries",
          "description": "List of targeted countries",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "targetSectors": {
          "type": "array",
          "title": "Target Sectors",
          "description": "List of targeted sectors",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "ttps": {
          "type": "array",
          "title": "TTPs",
          "description": "List of TTPs",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the cyber term",
          "order": 3
        },
        "updatedDate": {
          "type": "string",
          "title": "Updated Date",
          "description": "The date the cyber term was last updated",
          "order": 10
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Name of the cyber term",
          "order": 2
        }
      },
      "definitions": {
        "mitreAttack": {
          "type": "object",
          "title": "mitreAttack",
          "properties": {
            "tactic": {
              "type": "string",
              "title": "Tactic",
              "description": "MITRE ATT\\u0026CK tactic name related to the cyber term",
              "order": 1
            },
            "techniques": {
              "type": "array",
              "title": "Techniques",
              "description": "List of MITRE ATT\\u0026CK technique names and URLs of the MITRE description",
              "items": {
                "$ref": "#/definitions/technique"
              },
              "order": 2
            }
          },
          "definitions": {
            "technique": {
              "type": "object",
              "title": "technique",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name of the technique",
                  "order": 1
                },
                "url": {
                  "type": "string",
                  "title": "URL",
                  "description": "URL",
                  "order": 2
                }
              }
            }
          }
        },
        "technique": {
          "type": "object",
          "title": "technique",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the technique",
              "order": 1
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "URL",
              "order": 2
            }
          }
        }
      }
    },
    "mitreAttack": {
      "type": "object",
      "title": "mitreAttack",
      "properties": {
        "tactic": {
          "type": "string",
          "title": "Tactic",
          "description": "MITRE ATT\\u0026CK tactic name related to the cyber term",
          "order": 1
        },
        "techniques": {
          "type": "array",
          "title": "Techniques",
          "description": "List of MITRE ATT\\u0026CK technique names and URLs of the MITRE description",
          "items": {
            "$ref": "#/definitions/technique"
          },
          "order": 2
        }
      },
      "definitions": {
        "technique": {
          "type": "object",
          "title": "technique",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the technique",
              "order": 1
            },
            "url": {
              "type": "string",
              "title": "URL",
              "description": "URL",
              "order": 2
            }
          }
        }
      }
    },
    "technique": {
      "type": "object",
      "title": "technique",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the technique",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)