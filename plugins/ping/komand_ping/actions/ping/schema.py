# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Ping a host to check for connectivity"


class Input:
    COUNT = "count"
    HOST = "host"
    RESOLVE_HOSTNAME = "resolve_hostname"
    

class Output:
    AVERAGE_LATENCY = "average_latency"
    MAXIMUM_LATENCY = "maximum_latency"
    MINIMUM_LATENCY = "minimum_latency"
    PACKETS_PERCENT_LOST = "packets_percent_lost"
    PACKETS_RECEIVED = "packets_received"
    PACKETS_TRANSMITTED = "packets_transmitted"
    REPLY = "reply"
    RESPONSE = "response"
    STANDARD_DEVIATION = "standard_deviation"
    

class PingInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "The number of requests that will be sent, the default is 4",
      "default": 4,
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "The domain name or IP of the host to check",
      "order": 1
    },
    "resolve_hostname": {
      "type": "boolean",
      "title": "Resolve Hostname",
      "description": "Whether to resolve a domain name to an IP address first",
      "order": 3
    }
  },
  "required": [
    "count",
    "host",
    "resolve_hostname"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PingOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "average_latency": {
      "type": "string",
      "title": "Average Latency",
      "description": "Average latency",
      "order": 6
    },
    "maximum_latency": {
      "type": "string",
      "title": "Maximum Latency",
      "description": "Maximum latency",
      "order": 8
    },
    "minimum_latency": {
      "type": "string",
      "title": "Minimum Latency",
      "description": "Minimum latency",
      "order": 7
    },
    "packets_percent_lost": {
      "type": "number",
      "title": "Percent Packet Lost",
      "description": "The percentage of packets that were lost",
      "order": 5
    },
    "packets_received": {
      "type": "integer",
      "title": "Packets Received",
      "description": "The number of packets that the host sent back",
      "order": 4
    },
    "packets_transmitted": {
      "type": "integer",
      "title": "Packets Transmitted",
      "description": "The number of packets that were sent to the host",
      "order": 3
    },
    "reply": {
      "type": "boolean",
      "title": "Reply",
      "description": "Whether the host is responding to our echo",
      "order": 1
    },
    "response": {
      "type": "string",
      "title": "Response",
      "description": "The response to the request",
      "order": 2
    },
    "standard_deviation": {
      "type": "string",
      "title": "Standard Deviation",
      "description": "Standard deviation",
      "order": 9
    }
  },
  "required": [
    "reply",
    "response"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)