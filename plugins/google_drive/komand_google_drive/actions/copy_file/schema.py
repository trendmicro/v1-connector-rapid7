# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Copy a file to a folder"


class Input:
    FILE_ID = "file_id"
    FOLDER_ID = "folder_id"
    NEW_FILE_NAME = "new_file_name"


class Output:
    RESULT = "result"


class CopyFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_id": {
      "type": "string",
      "title": "File ID",
      "description": "The ID of the file that will be copied to another folder",
      "order": 2
    },
    "folder_id": {
      "type": "string",
      "title": "Folder ID",
      "description": "ID of the folder where the file will be copied",
      "order": 1
    },
    "new_file_name": {
      "type": "string",
      "title": "New File Name",
      "description": "Select a new file name. e.g. testfile.csv",
      "order": 3
    }
  },
  "required": [
    "file_id",
    "folder_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CopyFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "$ref": "#/definitions/copy_file_result",
      "title": "Result",
      "description": "The result containing the ID of the file and ID of the folder to which the file was copied",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "copy_file_result": {
      "type": "object",
      "title": "copy_file_result",
      "properties": {
        "parents": {
          "type": "array",
          "title": "Folder ID",
          "description": "Folder ID",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "File ID",
          "description": "File ID",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)