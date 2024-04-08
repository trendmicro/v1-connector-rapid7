# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY_V1 = "api_key_v1"
    API_KEY_V2 = "api_key_v2"
    TENANT = "tenant"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key_v1": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key v1",
      "description": "Netskope authorization token for v1 API",
      "order": 2
    },
    "api_key_v2": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key v2",
      "description": "Netskope authorization token for v2 API",
      "order": 3
    },
    "tenant": {
      "type": "string",
      "title": "Tenant",
      "description": "Owner's name that is included in URL",
      "order": 1
    }
  },
  "required": [
    "api_key_v1",
    "api_key_v2",
    "tenant"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
