# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides a list of historic WHOIS records for a domain name"


class Input:
    DOMAIN = "domain"
    

class Output:
    RESPONSE = "response"
    

class WhoisHistoryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name you wish to query",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WhoisHistoryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/whois_history_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "history": {
      "type": "object",
      "title": "history",
      "properties": {
        "date": {
          "type": "string",
          "title": "Date",
          "order": 1
        },
        "is_private": {
          "type": "integer",
          "title": "Is Private",
          "order": 2
        },
        "whois": {
          "$ref": "#/definitions/whois_history_whois",
          "title": "Whois",
          "order": 3
        }
      },
      "definitions": {
        "registration": {
          "type": "object",
          "title": "registration",
          "properties": {
            "created": {
              "type": "string",
              "title": "Created",
              "order": 1
            },
            "expires": {
              "type": "string",
              "title": "Expires",
              "order": 2
            },
            "registrar": {
              "type": "string",
              "title": "Registrar",
              "order": 3
            },
            "statuses": {
              "type": "array",
              "title": "Statuses",
              "items": {
                "type": "string"
              },
              "order": 4
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "order": 5
            }
          }
        },
        "whois_history_whois": {
          "type": "object",
          "title": "whois_history_whois",
          "properties": {
            "name_servers": {
              "type": "array",
              "title": "Name Servers",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "record": {
              "type": "string",
              "title": "Record",
              "order": 2
            },
            "registrant": {
              "type": "string",
              "title": "Registrant",
              "order": 3
            },
            "registration": {
              "$ref": "#/definitions/registration",
              "title": "Registration",
              "order": 4
            }
          },
          "definitions": {
            "registration": {
              "type": "object",
              "title": "registration",
              "properties": {
                "created": {
                  "type": "string",
                  "title": "Created",
                  "order": 1
                },
                "expires": {
                  "type": "string",
                  "title": "Expires",
                  "order": 2
                },
                "registrar": {
                  "type": "string",
                  "title": "Registrar",
                  "order": 3
                },
                "statuses": {
                  "type": "array",
                  "title": "Statuses",
                  "items": {
                    "type": "string"
                  },
                  "order": 4
                },
                "updated": {
                  "type": "string",
                  "title": "Updated",
                  "order": 5
                }
              }
            }
          }
        }
      }
    },
    "registration": {
      "type": "object",
      "title": "registration",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "order": 1
        },
        "expires": {
          "type": "string",
          "title": "Expires",
          "order": 2
        },
        "registrar": {
          "type": "string",
          "title": "Registrar",
          "order": 3
        },
        "statuses": {
          "type": "array",
          "title": "Statuses",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "updated": {
          "type": "string",
          "title": "Updated",
          "order": 5
        }
      }
    },
    "whois_history_response": {
      "type": "object",
      "title": "whois_history_response",
      "properties": {
        "history": {
          "type": "array",
          "title": "History",
          "items": {
            "$ref": "#/definitions/history"
          },
          "order": 1
        },
        "record_count": {
          "type": "integer",
          "title": "Record Count",
          "order": 2
        }
      },
      "definitions": {
        "history": {
          "type": "object",
          "title": "history",
          "properties": {
            "date": {
              "type": "string",
              "title": "Date",
              "order": 1
            },
            "is_private": {
              "type": "integer",
              "title": "Is Private",
              "order": 2
            },
            "whois": {
              "$ref": "#/definitions/whois_history_whois",
              "title": "Whois",
              "order": 3
            }
          },
          "definitions": {
            "registration": {
              "type": "object",
              "title": "registration",
              "properties": {
                "created": {
                  "type": "string",
                  "title": "Created",
                  "order": 1
                },
                "expires": {
                  "type": "string",
                  "title": "Expires",
                  "order": 2
                },
                "registrar": {
                  "type": "string",
                  "title": "Registrar",
                  "order": 3
                },
                "statuses": {
                  "type": "array",
                  "title": "Statuses",
                  "items": {
                    "type": "string"
                  },
                  "order": 4
                },
                "updated": {
                  "type": "string",
                  "title": "Updated",
                  "order": 5
                }
              }
            },
            "whois_history_whois": {
              "type": "object",
              "title": "whois_history_whois",
              "properties": {
                "name_servers": {
                  "type": "array",
                  "title": "Name Servers",
                  "items": {
                    "type": "string"
                  },
                  "order": 1
                },
                "record": {
                  "type": "string",
                  "title": "Record",
                  "order": 2
                },
                "registrant": {
                  "type": "string",
                  "title": "Registrant",
                  "order": 3
                },
                "registration": {
                  "$ref": "#/definitions/registration",
                  "title": "Registration",
                  "order": 4
                }
              },
              "definitions": {
                "registration": {
                  "type": "object",
                  "title": "registration",
                  "properties": {
                    "created": {
                      "type": "string",
                      "title": "Created",
                      "order": 1
                    },
                    "expires": {
                      "type": "string",
                      "title": "Expires",
                      "order": 2
                    },
                    "registrar": {
                      "type": "string",
                      "title": "Registrar",
                      "order": 3
                    },
                    "statuses": {
                      "type": "array",
                      "title": "Statuses",
                      "items": {
                        "type": "string"
                      },
                      "order": 4
                    },
                    "updated": {
                      "type": "string",
                      "title": "Updated",
                      "order": 5
                    }
                  }
                }
              }
            }
          }
        },
        "registration": {
          "type": "object",
          "title": "registration",
          "properties": {
            "created": {
              "type": "string",
              "title": "Created",
              "order": 1
            },
            "expires": {
              "type": "string",
              "title": "Expires",
              "order": 2
            },
            "registrar": {
              "type": "string",
              "title": "Registrar",
              "order": 3
            },
            "statuses": {
              "type": "array",
              "title": "Statuses",
              "items": {
                "type": "string"
              },
              "order": 4
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "order": 5
            }
          }
        },
        "whois_history_whois": {
          "type": "object",
          "title": "whois_history_whois",
          "properties": {
            "name_servers": {
              "type": "array",
              "title": "Name Servers",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "record": {
              "type": "string",
              "title": "Record",
              "order": 2
            },
            "registrant": {
              "type": "string",
              "title": "Registrant",
              "order": 3
            },
            "registration": {
              "$ref": "#/definitions/registration",
              "title": "Registration",
              "order": 4
            }
          },
          "definitions": {
            "registration": {
              "type": "object",
              "title": "registration",
              "properties": {
                "created": {
                  "type": "string",
                  "title": "Created",
                  "order": 1
                },
                "expires": {
                  "type": "string",
                  "title": "Expires",
                  "order": 2
                },
                "registrar": {
                  "type": "string",
                  "title": "Registrar",
                  "order": 3
                },
                "statuses": {
                  "type": "array",
                  "title": "Statuses",
                  "items": {
                    "type": "string"
                  },
                  "order": 4
                },
                "updated": {
                  "type": "string",
                  "title": "Updated",
                  "order": 5
                }
              }
            }
          }
        }
      }
    },
    "whois_history_whois": {
      "type": "object",
      "title": "whois_history_whois",
      "properties": {
        "name_servers": {
          "type": "array",
          "title": "Name Servers",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "record": {
          "type": "string",
          "title": "Record",
          "order": 2
        },
        "registrant": {
          "type": "string",
          "title": "Registrant",
          "order": 3
        },
        "registration": {
          "$ref": "#/definitions/registration",
          "title": "Registration",
          "order": 4
        }
      },
      "definitions": {
        "registration": {
          "type": "object",
          "title": "registration",
          "properties": {
            "created": {
              "type": "string",
              "title": "Created",
              "order": 1
            },
            "expires": {
              "type": "string",
              "title": "Expires",
              "order": 2
            },
            "registrar": {
              "type": "string",
              "title": "Registrar",
              "order": 3
            },
            "statuses": {
              "type": "array",
              "title": "Statuses",
              "items": {
                "type": "string"
              },
              "order": 4
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "order": 5
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