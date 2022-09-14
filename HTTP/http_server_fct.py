#! /usr/bin/python
#---------------------------------------------

from param import param_py
from src import connection
from src import parser_json
from src import capture
from src import lidar

import http.client as client
import json


def send_state(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = parser_json.load_file_to_sock_data_encoded(path)
        self.wfile.write(data)
    except:
        pass
