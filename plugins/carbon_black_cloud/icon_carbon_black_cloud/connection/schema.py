# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_ID = "api_id"
    API_SECRET_KEY = "api_secret_key"
    ORG_KEY = "org_key"
    URL = "url"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_id": {
      "type": "string",
      "title": "API ID",
      "description": "API ID",
      "placeholder": "APP ID",
      "tooltip": "Enter the API ID from your Carbon Black Account.",
      "order": 1
    },
    "api_secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Secret Key",
      "description": "API secret key",
      "placeholder": "API Secret Key",
      "tooltip": "Enter your Carbon Black Cloud API Secret Key.",
      "order": 2
    },
    "org_key": {
      "type": "string",
      "title": "Org Key",
      "description": "Organization Key",
      "placeholder": "Org Key",
      "tooltip": "Enter the Carbon Black Cloud Org Key. To obtain the Org Key, log in to your Carbon Black Cloud account and go to Settings > API Access > API Keys.",
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The Carbon Black Cloud URL you use. You can find this by looking at the web address of your Carbon Black Cloud console",
      "default": "defense.conferdeploy.net",
      "placeholder": "URL",
      "tooltip": "To determine which URL to select, login to your Carbon Black Cloud account and refer to the URL displayed in the address bar.",
      "enum": [
        "defense-eap01.conferdeploy.net",
        "dashboard.confer.net",
        "defense.conferdeploy.net",
        "defense-prod05.conferdeploy.net",
        "defense-eu.conferdeploy.net",
        "defense-prodnrt.conferdeploy.net",
        "defense-prodsyd.conferdeploy.net",
        "ew2.carbonblackcloud.vmware.com",
        "gprd1usgw1.carbonblack-us-gov.vmware.com"
      ],
      "order": 4
    }
  },
  "required": [
    "api_id",
    "api_secret_key",
    "org_key",
    "url"
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
