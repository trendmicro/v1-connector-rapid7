# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Blacklist MD5 hashes"


class Input:
    DESCRIPTION = "description"
    DOMAIN_ID = "domain_id"
    HASHES = "hashes"
    NAME = "name"


class Output:
    BLACKLIST_IDS = "blacklist_ids"


class BlacklistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description for the blacklist",
      "order": 2
    },
    "domain_id": {
      "type": "string",
      "title": "Domain ID",
      "description": "ID of the domain to apply the blacklist to. Omitting this input will apply the blacklist to all domains (globally)",
      "order": 4
    },
    "hashes": {
      "type": "array",
      "title": "Hashes",
      "description": "MD5 hashes to add to the blacklist",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name for the blacklist",
      "order": 3
    }
  },
  "required": [
    "description",
    "hashes",
    "name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlacklistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "blacklist_ids": {
      "type": "array",
      "title": "Blacklist IDs",
      "description": "IDs of the resulting blacklists",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "blacklist_ids"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
