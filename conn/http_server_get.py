#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import parser_json

import json


def get_geo(self):
    print("geo !")

def get_test_http_conn(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

def get_state_py(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    try:
        data = parser_json.load_file_to_sock_data_encoded(param_py.path_state_py)
        self.wfile.write(data)
    except:
        print('not valid JSON')
