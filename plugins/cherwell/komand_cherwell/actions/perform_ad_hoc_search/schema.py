# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Runs an ad-hoc Business Object search. To execute a search with Prompts, the PromptId and Value are required in the data request object"


class Input:
    DATA_REQUEST = "data_request"


class Output:
    SEARCH_RESULTS = "search_results"


class PerformAdHocSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data_request": {
      "type": "object",
      "title": "Data Request",
      "description": "Request object to specify search parameters",
      "order": 1
    }
  },
  "required": [
    "data_request"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PerformAdHocSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "search_results": {
      "type": "object",
      "title": "Search Results",
      "description": "The raw JSON search results returned by the endpoint",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
