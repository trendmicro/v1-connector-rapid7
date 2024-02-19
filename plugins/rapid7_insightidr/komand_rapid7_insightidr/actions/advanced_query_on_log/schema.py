# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Realtime query an InsightIDR log. This will query individual logs for results. Note only 500 results will be returned from a single call, if all results are required for this query please use smaller timeranges. If both a log name and log ID are provided, the log ID will used over the log name"


class Input:
    LOG = "log"
    LOG_ID = "log_id"
    QUERY = "query"
    RELATIVE_TIME = "relative_time"
    TIME_FROM = "time_from"
    TIME_TO = "time_to"
    TIMEOUT = "timeout"


class Output:
    COUNT = "count"
    RESULTS_EVENTS = "results_events"
    RESULTS_STATISTICAL = "results_statistical"


class AdvancedQueryOnLogInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "log": {
      "type": "string",
      "title": "Log Name",
      "description": "Log name to search",
      "order": 6
    },
    "log_id": {
      "type": "string",
      "title": "Log ID",
      "description": "Log id to search",
      "order": 7
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "LEQL Query",
      "order": 1
    },
    "relative_time": {
      "type": "string",
      "title": "Relative Time",
      "description": "A relative time in the past to look for alerts",
      "default": "Last 5 Minutes",
      "enum": [
        "Last 5 Minutes",
        "Last 10 Minutes",
        "Last 20 Minutes",
        "Last 30 Minutes",
        "Last 45 Minutes",
        "Last 1 Hour",
        "Last 2 Hours",
        "Last 3 Hours",
        "Last 6 Hours",
        "Last 12 Hours",
        "Use Time From Value"
      ],
      "order": 2
    },
    "time_from": {
      "type": "string",
      "title": "Time From",
      "description": "Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)",
      "order": 3
    },
    "time_to": {
      "type": "string",
      "title": "Time To",
      "description": "Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)",
      "order": 4
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Time in seconds to wait for the query to return. If exceeded the plugin will throw an error",
      "default": 60,
      "order": 5
    }
  },
  "required": [
    "query",
    "relative_time",
    "timeout"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AdvancedQueryOnLogOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of log entries found",
      "order": 3
    },
    "results_events": {
      "type": "array",
      "title": "Query Results (Events)",
      "description": "Query Results",
      "items": {
        "$ref": "#/definitions/events"
      },
      "order": 1
    },
    "results_statistical": {
      "$ref": "#/definitions/statistics",
      "title": "Query Results (Statistical)",
      "description": "Query Results",
      "order": 2
    }
  },
  "required": [
    "count"
  ],
  "definitions": {
    "events": {
      "type": "object",
      "title": "events",
      "properties": {
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 2
        },
        "sequence_number": {
          "type": "integer",
          "title": "Sequence Number",
          "description": "Sequence number",
          "order": 3
        },
        "log_id": {
          "type": "string",
          "title": "Log ID",
          "description": "Log ID",
          "order": 4
        },
        "message": {
          "$ref": "#/definitions/message",
          "title": "Message",
          "description": "Message",
          "order": 5
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 6
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "sourceName": {
          "type": "string",
          "title": "Source Name",
          "order": 1
        },
        "eventCode": {
          "type": "integer",
          "title": "Event Code",
          "order": 2
        },
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "order": 3
        },
        "sid": {
          "type": "string",
          "title": "SID",
          "order": 4
        },
        "isDomainController": {
          "type": "boolean",
          "title": "Is Domain Controller",
          "order": 5
        },
        "eventData": {
          "$ref": "#/definitions/eventData",
          "title": "Event Data",
          "order": 6
        },
        "timeWritten": {
          "type": "string",
          "title": "Time Written",
          "order": 7
        }
      }
    },
    "eventData": {
      "type": "object",
      "title": "eventData",
      "properties": {
        "oaState": {
          "type": "string",
          "title": "OA State",
          "description": "OA state",
          "order": 1
        },
        "lastAsSignatureAge": {
          "type": "string",
          "title": "Last As Signature Age",
          "description": "Last as signature age",
          "order": 2
        },
        "productStatus": {
          "type": "string",
          "title": "Product Status",
          "description": "Product status",
          "order": 3
        },
        "assignatureVersion": {
          "type": "string",
          "title": "As Signature Version",
          "description": "As signature version",
          "order": 4
        },
        "ioavState": {
          "type": "string",
          "title": "IOAV State",
          "description": "IOAV state",
          "order": 5
        },
        "asSignatureCreationTime": {
          "type": "string",
          "title": "As Signature Creation Time",
          "description": "As signature creation time",
          "order": 6
        },
        "lastFullScanSource": {
          "type": "string",
          "title": "Last Full Scan Source",
          "description": "Last full scan source",
          "order": 7
        },
        "nriSignatureVersion": {
          "type": "string",
          "title": "NRI Signature Version",
          "description": "NRI signature version",
          "order": 8
        },
        "lastFullScanStartTime": {
          "type": "string",
          "title": "Last Full Scan Start Time",
          "description": "Last full scan start time",
          "order": 9
        },
        "engineVersion": {
          "type": "string",
          "title": "Engine Version",
          "description": "Engine version",
          "order": 10
        },
        "bmState": {
          "type": "string",
          "title": "BMS State",
          "description": "BMS state",
          "order": 11
        },
        "lastQuickScanSource": {
          "type": "string",
          "title": "Last Quick Scan Source",
          "description": "Last quick scan source",
          "order": 12
        },
        "lastFullScanEndTime": {
          "type": "string",
          "title": "Last Full Scan End Time",
          "description": "Last full scan end time",
          "order": 13
        },
        "productName": {
          "type": "string",
          "title": "Product Name",
          "description": "Product name",
          "order": 14
        },
        "rtpState": {
          "type": "string",
          "title": "RTP State",
          "description": "RTP state",
          "order": 15
        },
        "platformVersion": {
          "type": "string",
          "title": "Platform Version",
          "description": "Platform version",
          "order": 16
        },
        "lastQuickScanAge": {
          "type": "string",
          "title": "Last Quick Scan Age",
          "description": "Last quick scan age",
          "order": 17
        },
        "data": {
          "type": "array",
          "title": "Data",
          "description": "Data",
          "items": {
            "type": "object"
          },
          "order": 18
        },
        "lastQuickScanEndTime": {
          "type": "string",
          "title": "Last Quick Scan End Time",
          "description": "Last quick scan end time",
          "order": 19
        },
        "avSignatureCreationTime": {
          "type": "string",
          "title": "AV Signature Creation Time",
          "description": "AV signature creation time",
          "order": 20
        },
        "avsignatureVersion": {
          "type": "string",
          "title": "AV Signature Version",
          "description": "AV signature version",
          "order": 21
        },
        "lastAvSignatureAge": {
          "type": "string",
          "title": "Last AV Signature Age",
          "description": "Last AV signature age",
          "order": 22
        },
        "nriEngineVersion": {
          "type": "string",
          "title": "NRI Engine Version",
          "description": "NRI engine version",
          "order": 23
        },
        "lastQuickScanStartTime": {
          "type": "string",
          "title": "Last Quick Scan Start Time",
          "description": "Last quick scan start time",
          "order": 24
        },
        "lastFullScanAge": {
          "type": "string",
          "title": "Last Full Scan Age",
          "description": "Last full scan age",
          "order": 25
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "rel": {
          "type": "string",
          "title": "Relation",
          "description": "Relation",
          "order": 1
        },
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 2
        }
      }
    },
    "statistics": {
      "type": "object",
      "title": "statistics",
      "properties": {
        "stats": {
          "type": "object",
          "title": "Stats",
          "description": "Holds the overall result when query does not contain a 'groupby' clause",
          "order": 1
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "Holds the overall result for each group in a 'groupby' query",
          "items": {
            "type": "object"
          },
          "order": 2
        },
        "granularity": {
          "type": "integer",
          "title": "Granularity",
          "description": "The time window in milliseconds for each time slice in the time series",
          "order": 3
        },
        "timeseries": {
          "type": "object",
          "title": "Time Series",
          "description": "Holds the query results for each timeslice (each partition of the time_range), for non-'groupby' queries",
          "order": 4
        },
        "groups_timeseries": {
          "type": "array",
          "title": "Groups Time Series",
          "description": "For 'groupby' queries, holds the timeseries object for each group",
          "items": {
            "type": "object"
          },
          "order": 5
        },
        "from": {
          "type": "integer",
          "title": "From",
          "description": "The start of the time range for the query, as a UNIX timestamp in milliseconds",
          "order": 6
        },
        "to": {
          "type": "integer",
          "title": "To",
          "description": "The end of the time range for the query, as a UNIX timestamp in milliseconds",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of function performed, for example, \"count\", \"max\", \"average\", \"standarddeviation\"",
          "order": 8
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The key which the function of the 'calculate' clause is applied to",
          "order": 9
        },
        "cardinality": {
          "type": "integer",
          "title": "Cardinality",
          "description": "Always 0",
          "order": 10
        },
        "others": {
          "type": "object",
          "title": "Others",
          "description": "Not yet implemented",
          "order": 11
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Holds a status code for the query, potentially different from the status code of the response",
          "order": 12
        },
        "all_exact_results": {
          "type": "boolean",
          "title": "All Exact Results",
          "description": "Boolean indicating whether groups are calculated approximately (approximated if a groupby query involves over 10,000 groups)",
          "order": 13
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
