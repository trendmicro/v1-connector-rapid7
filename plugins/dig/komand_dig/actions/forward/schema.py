# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to request a forward lookup for a domain"


class Input:
    DOMAIN = "domain"
    QUERY = "query"
    RESOLVER = "resolver"


class Output:
    ALL_ANSWERS = "all_answers"
    ANSWER = "answer"
    FULLOUTPUT = "fulloutput"
    LAST_ANSWER = "last_answer"
    NAMESERVER = "nameserver"
    QUESTION = "question"
    STATUS = "status"


class ForwardInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name to resolve",
      "order": 1
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query type e.g. ANY, A, MX, NS, etc",
      "enum": [
        "A",
        "AAAA",
        "ANY",
        "CNAME",
        "MX",
        "NS",
        "PTR",
        "SOA"
      ],
      "order": 3
    },
    "resolver": {
      "type": "string",
      "title": "Resolver",
      "description": "Resolver. Leave blank to use default resolver for the system",
      "order": 2
    }
  },
  "required": [
    "domain",
    "query"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ForwardOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "all_answers": {
      "type": "array",
      "title": "All Answers",
      "description": "A list of all answers found",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "answer": {
      "type": "string",
      "title": "Answer",
      "description": "Answer received",
      "order": 4
    },
    "fulloutput": {
      "type": "string",
      "title": "Full Output",
      "description": "Full DNS output",
      "order": 1
    },
    "last_answer": {
      "type": "string",
      "title": "Last Answer",
      "description": "The last answer found in the answers section",
      "order": 7
    },
    "nameserver": {
      "type": "string",
      "title": "Nameserver",
      "description": "Nameserver that fulfilled request",
      "order": 3
    },
    "question": {
      "type": "string",
      "title": "Question",
      "description": "Question asked",
      "order": 5
    },
    "status": {
      "type": "string",
      "title": "Query Status",
      "description": "Query status [ NOERROR | FORMERR | NXDOMAIN | SERVFAIL | REFUSED ...]",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
