# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Perform a domain lookup"


class Input:
    DOMAIN = "domain"


class Output:
    ENTITIES = "entities"
    EVENTS = "events"
    NAME = "name"
    NAMESERVERS = "nameservers"
    PORT43 = "port43"
    PUBLICIDS = "publicIds"
    REGISTRYDOMAINID = "registryDomainId"
    SECUREDNS = "secureDns"
    STATUS = "status"
    UNICODENAME = "unicodeName"
    VARIANTS = "variants"


class DomainLookupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain for which information will be searched",
      "order": 1
    }
  },
  "required": [
    "domain"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainLookupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "entities": {
      "type": "array",
      "title": "Entities",
      "description": "Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people",
      "items": {
        "$ref": "#/definitions/entity"
      },
      "order": 3
    },
    "events": {
      "type": "array",
      "title": "Events",
      "description": "List of events that have occurred",
      "items": {
        "$ref": "#/definitions/event"
      },
      "order": 7
    },
    "name": {
      "type": "string",
      "title": "LDH Name",
      "description": "The LDH name of the domain",
      "order": 1
    },
    "nameservers": {
      "type": "array",
      "title": "Nameservers",
      "description": "List of nameservers",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "port43": {
      "type": "string",
      "title": "Port 43",
      "description": "The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found",
      "order": 8
    },
    "publicIds": {
      "type": "array",
      "title": "Public IDs",
      "description": "List of public IDs",
      "items": {
        "$ref": "#/definitions/publicId"
      },
      "order": 10
    },
    "registryDomainId": {
      "type": "string",
      "title": "Registry Domain ID",
      "description": "The registry-unique identifier of the domain object instance",
      "order": 2
    },
    "secureDns": {
      "$ref": "#/definitions/secureDns",
      "title": "Secure DNS",
      "description": "Secure DNS",
      "order": 6
    },
    "status": {
      "type": "array",
      "title": "Status",
      "description": "The state of the IP network",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "unicodeName": {
      "type": "string",
      "title": "Unicode Name",
      "description": "The unicode name of the domain",
      "order": 11
    },
    "variants": {
      "type": "array",
      "title": "Variants",
      "description": "List of variants",
      "items": {
        "$ref": "#/definitions/variant"
      },
      "order": 4
    }
  },
  "definitions": {
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "handle": {
          "type": "string",
          "title": "Handle",
          "description": "The registry-unique identifier of the nameserver",
          "order": 1
        },
        "roles": {
          "type": "array",
          "title": "Roles",
          "description": "List of roles",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "description": "The kind of the entity",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "The title of the entity",
          "order": 4
        },
        "role": {
          "type": "string",
          "title": "Role",
          "description": "The role of the entity",
          "order": 5
        },
        "fullname": {
          "type": "string",
          "title": "Fullname",
          "description": "The entity fullname",
          "order": 6
        },
        "address": {
          "$ref": "#/definitions/address",
          "title": "Address",
          "description": "The address of the entity",
          "order": 7
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "The entity phone number",
          "order": 8
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Name of the organization",
          "order": 9
        },
        "language": {
          "type": "string",
          "title": "Language",
          "description": "Information about the language of the entity",
          "order": 10
        }
      }
    },
    "address": {
      "type": "object",
      "title": "address",
      "properties": {
        "postOfficeBox": {
          "type": "string",
          "title": "Post Office Box",
          "description": "The entity post office box",
          "order": 1
        },
        "extendedAddress": {
          "type": "string",
          "title": "Extended Address",
          "description": "The entity extended address",
          "order": 2
        },
        "streetAddress": {
          "type": "string",
          "title": "Street Address",
          "description": "The entity's street address",
          "order": 3
        },
        "locality": {
          "type": "string",
          "title": "Locality",
          "description": "The location of the entity",
          "order": 4
        },
        "region": {
          "type": "string",
          "title": "Region",
          "description": "The entity's region",
          "order": 5
        },
        "postalCode": {
          "type": "string",
          "title": "Postal Code",
          "description": "The entity's postal code",
          "order": 6
        },
        "countryName": {
          "type": "string",
          "title": "Country Name",
          "description": "The country name of the entity",
          "order": 7
        }
      }
    },
    "variant": {
      "type": "object",
      "title": "variant",
      "properties": {
        "relation": {
          "type": "array",
          "title": "Relation",
          "description": "The relationship between the variants and the containing domain object",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "idnTable": {
          "type": "string",
          "title": "IDN Table",
          "description": "The Internationalized Domain Name (IDN) table that has been registered in the IANA Repository of IDN Practices",
          "order": 2
        },
        "variantName": {
          "type": "array",
          "title": "Variant Names",
          "description": "List of variant names",
          "items": {
            "$ref": "#/definitions/variantName"
          },
          "order": 3
        }
      }
    },
    "variantName": {
      "type": "object",
      "title": "variantName",
      "properties": {
        "ldhName": {
          "type": "string",
          "title": "LDH Name",
          "description": "The LDH name of the domain",
          "order": 1
        },
        "unicodeName": {
          "type": "string",
          "title": "Unicode Name",
          "description": "The unicode name of the domain",
          "order": 2
        }
      }
    },
    "secureDns": {
      "type": "object",
      "title": "secureDns",
      "properties": {
        "zoneSigned": {
          "type": "boolean",
          "title": "Zone Signed",
          "description": "Whether the zone has been signed",
          "order": 1
        },
        "delegationSigned": {
          "type": "boolean",
          "title": "Delegation Signed",
          "description": "Whether there are DS records in the parent",
          "order": 2
        },
        "dsData": {
          "type": "array",
          "title": "DS Data",
          "description": "DS Data",
          "items": {
            "$ref": "#/definitions/dsData"
          },
          "order": 3
        },
        "keyData": {
          "type": "array",
          "title": "Key Data",
          "description": "Key Data",
          "items": {
            "$ref": "#/definitions/keyData"
          },
          "order": 4
        }
      }
    },
    "dsData": {
      "type": "object",
      "title": "dsData",
      "properties": {
        "key_tag": {
          "type": "integer",
          "title": "Key Tag",
          "description": "The key tag field of a DNS DS record",
          "order": 1
        },
        "algorithm": {
          "type": "integer",
          "title": "Algorithm",
          "description": "The algorithm field of a DNS DS record",
          "order": 2
        },
        "digest": {
          "type": "string",
          "title": "Digest",
          "description": "The digest field of a DNS DS record",
          "order": 3
        },
        "digestType": {
          "type": "integer",
          "title": "Digest Type",
          "description": "The digest type field of a DNS DS record",
          "order": 4
        }
      }
    },
    "keyData": {
      "type": "object",
      "title": "keyData",
      "properties": {
        "flags": {
          "type": "integer",
          "title": "Flags",
          "description": "The flags field value in the DNSKEY record",
          "order": 1
        },
        "protocol": {
          "type": "integer",
          "title": "Protocol",
          "description": "The protocol field value of the DNSKEY record",
          "order": 2
        },
        "publicKey": {
          "type": "string",
          "title": "Public Key",
          "description": "The public key in the DNSKEY record",
          "order": 3
        },
        "algorithm": {
          "type": "integer",
          "title": "Algorithm",
          "description": "The algorithm field of a DNSKEY record",
          "order": 4
        },
        "events": {
          "type": "array",
          "title": "Events",
          "description": "Events",
          "items": {
            "$ref": "#/definitions/event"
          },
          "order": 5
        }
      }
    },
    "event": {
      "type": "object",
      "title": "event",
      "properties": {
        "eventAction": {
          "type": "string",
          "title": "Event Action",
          "description": "The reason for the event",
          "order": 1
        },
        "eventActor": {
          "type": "string",
          "title": "Event Actor",
          "description": "The actor responsible for the event",
          "order": 2
        },
        "eventDate": {
          "type": "string",
          "title": "Event Date",
          "description": "The time and date the event occurred",
          "order": 3
        }
      }
    },
    "publicId": {
      "type": "object",
      "title": "publicId",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of public identifier",
          "order": 1
        },
        "identifier": {
          "type": "string",
          "title": "Identifier",
          "description": "The public identifier of the type related to 'type'",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
