# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Query for data related to a specified IP range"


class Input:
    DIRECTION = "direction"
    FROM = "from"
    IP_RANGE = "ip_range"
    LIMIT = "limit"
    ORDERBY = "orderby"
    RISKRULE = "riskRule"
    RISKSCORE = "riskScore"


class Output:
    DATA = "data"


class SearchIPAddressesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "direction": {
      "type": "string",
      "title": "Result Direction",
      "description": "Sort results ascending/descending",
      "default": "asc",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 4
    },
    "from": {
      "type": "number",
      "title": "Offset",
      "description": "Number of initial records to skip",
      "default": 0,
      "order": 2
    },
    "ip_range": {
      "type": "string",
      "title": "IP Range",
      "description": "IP address range to search",
      "order": 5
    },
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of results to retrieve, up to 100",
      "order": 1
    },
    "orderby": {
      "type": "string",
      "title": "Order By",
      "description": "Which property to sort the results by",
      "enum": [
        "Created",
        "Lastseen",
        "Firstseen",
        "Modified",
        "Riskscore",
        "Rules",
        "Sevendayshits",
        "Sixtydayshits",
        "Totalhits"
      ],
      "order": 3
    },
    "riskRule": {
      "type": "string",
      "title": "Risk Rule",
      "description": "Filters the results by risk rule",
      "enum": [
        "",
        "Threat Actor Used Infrastructure",
        "Historically Reported by Insikt Group",
        "Inside Possible Bogus BGP Route",
        "Historical Botnet Traffic",
        "Recently Communicating With C&C Server",
        "Nameserver for C&C Server",
        "Historical C&C Server",
        "Cyber Exploit Signal - Critical",
        "Cyber Exploit Signal - Important",
        "Cyber Exploit Signal - Medium",
        "Recent Host of Many DDNS Names",
        "Historically Reported as a Defanged IP",
        "Historically Reported by DHS AIS",
        "Resolution of Fast Flux DNS Name",
        "Historically Reported in Threat List",
        "Historical Honeypot Sighting",
        "Honeypot Host",
        "Recently Active C&C Server",
        "Recent C&C Server",
        "Historically Linked to Intrusion Method",
        "Historically Linked to APT",
        "Historically Linked to Cyber Attack",
        "Malicious Packet Source",
        "Malware Delivery",
        "Historical Multicategory Blacklist",
        "Historical Open Proxies",
        "Phishing Host",
        "Historical Positive Malware Verdict",
        "Recorded Future Predictive Risk Model",
        "Actively Communicating C&C Server",
        "Recently Reported by Insikt Group",
        "Recent Botnet Traffic",
        "Current C&C Server",
        "Recently Reported as a Defanged IP",
        "Recently Reported by DHS AIS",
        "Recent Honeypot Sighting",
        "Recently Linked to Intrusion Method",
        "Recently Linked to APT",
        "Recently Linked to Cyber Attack",
        "Recent Multicategory Blacklist",
        "Recent Open Proxies",
        "Recent Positive Malware Verdict",
        "Recently Referenced by Insikt Group",
        "Recent Spam Source",
        "Recent SSH/Dictionary Attacker",
        "Recent Bad SSL Association",
        "Recent Threat Researcher",
        "Recently Defaced Site",
        "Historically Referenced by Insikt Group",
        "Trending in Recorded Future Analyst Community",
        "Historical Spam Source",
        "Historical SSH/Dictionary Attacker",
        "Historical Bad SSL Association",
        "Historical Threat Researcher",
        "Tor Node",
        "Unusual IP",
        "Vulnerable Host"
      ],
      "order": 6
    },
    "riskScore": {
      "type": "string",
      "title": "Risk Score",
      "description": "Filters the results by risk score",
      "order": 7
    }
  },
  "required": [
    "direction",
    "from",
    "ip_range",
    "limit",
    "orderby"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchIPAddressesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Data",
      "items": {
        "$ref": "#/definitions/ip_search_data"
      },
      "order": 1
    }
  },
  "required": [
    "data"
  ],
  "definitions": {
    "ip_search_data": {
      "type": "object",
      "title": "ip_search_data",
      "properties": {
        "analystNotes": {
          "type": "array",
          "title": "Analyst Notes",
          "description": "Notes from an analyst",
          "items": {
            "$ref": "#/definitions/analystNote"
          },
          "order": 1
        },
        "counts": {
          "type": "array",
          "title": "Counts",
          "description": "Counts",
          "items": {
            "$ref": "#/definitions/counts"
          },
          "order": 2
        },
        "enterpriseLists": {
          "type": "array",
          "title": "Enterprise Lists",
          "description": "Enterprise lists",
          "items": {
            "$ref": "#/definitions/enterpriseLists"
          },
          "order": 3
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "description": "Entity",
          "order": 4
        },
        "intelCard": {
          "type": "string",
          "title": "Intel Card",
          "description": "Intel card",
          "order": 5
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "Location",
          "order": 6
        },
        "metrics": {
          "type": "array",
          "title": "Metrics",
          "description": "Metrics",
          "items": {
            "$ref": "#/definitions/metrics"
          },
          "order": 7
        },
        "relatedEntities": {
          "type": "array",
          "title": "Related Entities",
          "description": "Related entities",
          "items": {
            "$ref": "#/definitions/relatedEntities"
          },
          "order": 8
        },
        "risk": {
          "$ref": "#/definitions/risk",
          "title": "Risk",
          "description": "Risk",
          "order": 9
        },
        "riskyCIDRIPs": {
          "type": "array",
          "title": "Risky CIDR IPs",
          "description": "Risky CIDR IPs",
          "items": {
            "$ref": "#/definitions/riskyCIDRIP"
          },
          "order": 10
        },
        "sightings": {
          "type": "array",
          "title": "Sightings",
          "description": "Sightings",
          "items": {
            "$ref": "#/definitions/sightings"
          },
          "order": 11
        },
        "threatLists": {
          "type": "array",
          "title": "Threat Lists",
          "description": "Threat lists",
          "items": {
            "$ref": "#/definitions/threatLists"
          },
          "order": 12
        },
        "timestamps": {
          "$ref": "#/definitions/timestamps",
          "title": "Timestamps",
          "description": "Timestamps",
          "order": 13
        }
      }
    },
    "analystNote": {
      "type": "object",
      "title": "analystNote",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/attributes",
          "title": "Attributes",
          "description": "Attributes",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "source": {
          "$ref": "#/definitions/labels",
          "title": "Source",
          "description": "Source",
          "order": 3
        }
      }
    },
    "attributes": {
      "type": "object",
      "title": "attributes",
      "properties": {
        "context_entities": {
          "type": "array",
          "title": "Context Entities",
          "description": "Context entities",
          "items": {
            "$ref": "#/definitions/context_entities"
          },
          "order": 1
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "Labels",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 2
        },
        "note_entities": {
          "type": "array",
          "title": "Note Entities",
          "description": "Note entities",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 3
        },
        "published": {
          "type": "string",
          "title": "Published",
          "description": "Published",
          "order": 4
        },
        "text": {
          "type": "string",
          "title": "Text",
          "description": "Text",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 6
        },
        "topic": {
          "$ref": "#/definitions/context_entities",
          "title": "Topic",
          "description": "Topic",
          "order": 7
        },
        "validated_on": {
          "type": "string",
          "title": "Validated On",
          "description": "Validated on",
          "order": 8
        },
        "validation_urls": {
          "type": "array",
          "title": "Validation URLs",
          "description": "Validation URLs",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 9
        }
      }
    },
    "context_entities": {
      "type": "object",
      "title": "context_entities",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 4
        }
      }
    },
    "labels": {
      "type": "object",
      "title": "labels",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "description": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "description": "Date",
          "order": 2
        }
      }
    },
    "enterpriseLists": {
      "type": "object",
      "title": "enterpriseLists",
      "properties": {
        "added": {
          "type": "string",
          "title": "Added",
          "description": "Added",
          "order": 1
        },
        "list": {
          "$ref": "#/definitions/list",
          "title": "List",
          "description": "List",
          "order": 2
        }
      }
    },
    "list": {
      "type": "object",
      "title": "list",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 4
        }
      }
    },
    "location": {
      "type": "object",
      "title": "location",
      "properties": {
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "ASN",
          "order": 1
        },
        "location": {
          "$ref": "#/definitions/location_data",
          "title": "Location",
          "description": "Location",
          "order": 2
        },
        "cidr": {
          "$ref": "#/definitions/cidr",
          "title": "CIDR",
          "description": "Classless Inter-Domain Routing",
          "order": 3
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Organization",
          "order": 4
        }
      }
    },
    "location_data": {
      "type": "object",
      "title": "location_data",
      "properties": {
        "continent": {
          "type": "string",
          "title": "Continent",
          "description": "Continent",
          "order": 1
        },
        "city": {
          "type": "string",
          "title": "City",
          "description": "City",
          "order": 2
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "Country",
          "order": 3
        }
      }
    },
    "cidr": {
      "type": "object",
      "title": "cidr",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "metrics": {
      "type": "object",
      "title": "metrics",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        },
        "value": {
          "type": "number",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "relatedEntities": {
      "type": "object",
      "title": "relatedEntities",
      "properties": {
        "entities": {
          "type": "array",
          "title": "Entities",
          "description": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        }
      }
    },
    "entities": {
      "type": "object",
      "title": "entities",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "description": "Count",
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "description": "Entity",
          "order": 2
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "description": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "description": "Criticality label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "description": "Evidence details",
          "items": {
            "$ref": "#/definitions/evidenceDetails"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "description": "Risk summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "description": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 6
        }
      }
    },
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "description": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "description": "Criticality label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "description": "Evidence string",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "description": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 5
        }
      }
    },
    "riskyCIDRIP": {
      "type": "object",
      "title": "riskyCIDRIP",
      "properties": {
        "ip": {
          "$ref": "#/definitions/ip",
          "title": "IP",
          "description": "IP",
          "order": 1
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 2
        }
      }
    },
    "ip": {
      "type": "object",
      "title": "ip",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "sightings": {
      "type": "object",
      "title": "sightings",
      "properties": {
        "fragment": {
          "type": "string",
          "title": "Fragment",
          "description": "Fragment",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "description": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 6
        }
      }
    },
    "threatLists": {
      "type": "object",
      "title": "threatLists",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 4
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "description": "First seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "description": "Last seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
