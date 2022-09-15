#! /usr/bin/python
#---------------------------------------------

from param import param_py
from src import connection
from src import parser_json
from src import capture
from src import lidar

import http.client as client
import json


def post_state(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = parser_json.load_file_to_sock_data_encoded(path)
        self.wfile.write(data)
    except:
        pass

def decode_post_json(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    data = post_data.decode('utf8')
    data = json.loads(data)
    return data
