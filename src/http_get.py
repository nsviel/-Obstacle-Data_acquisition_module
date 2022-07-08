#! /usr/bin/python
#---------------------------------------------

from src import parser_json

import json


def get_geo(self):
    print("geo !")

def get_test(self):
    self.send_response(200)

def get_state(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    data = parser_json.get_json_encoded()
    self.wfile.write(data)
