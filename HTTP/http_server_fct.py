#! /usr/bin/python
#---------------------------------------------

from param import param_py
from src import connection
from src import parser_json
from src import device

import http.client as client
import json


def process_post_param(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)
        for key, value in data.items():
            lvl1 = key
            for key_, value_ in data[key].items():
                lvl2 = key_
                lvl3 = value_

        param_py.state_py[lvl1][lvl2] = lvl3
        if(lvl2 == "device"):
            device.update_device()
    except:
        print('not valid JSON')

def send_state(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = parser_json.load_file_to_sock_data_encoded(path)
        self.wfile.write(data)
    except:
        pass