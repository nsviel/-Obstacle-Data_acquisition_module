#---------------------------------------------
# Possible POST command:
# - /py_state
# - /py_param
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json
from src import command

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/py_state'):
        manage_py_state(self)
    elif(command == '/py_param'):
        manage_py_param(self)

def manage_py_state(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_py.state_py = data
        parser_json.upload_state()

def manage_py_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = http_server_fct.decipher_json(data)
        command.manage_command(lvl1, lvl2, lvl3)
