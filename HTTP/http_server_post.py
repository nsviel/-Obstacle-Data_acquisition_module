#! /usr/bin/python
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json

import json


def post_param_py(self):
    http_server_fct.process_post_param(self)
