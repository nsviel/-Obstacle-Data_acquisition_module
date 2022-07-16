#! /usr/bin/python
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json

import json


def get_geo(self):
    print("geo !")

def get_test_http_conn(self):
    self.send_response(200)

def get_state_py(self):
    http_server_fct.send_state(self, param_py.path_state_py)
