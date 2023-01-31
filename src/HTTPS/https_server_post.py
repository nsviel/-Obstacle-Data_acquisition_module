#---------------------------------------------
# Possible POST command:
# - /py_state
# - /py_param
#---------------------------------------------

from src.param import param_py
from src.HTTPS import https_server_fct
from src.misc import parser_json
from src.interface import command
from src.misc import terminal
from src.interface import capture

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/py_state'):
        manage_py_state(self)
    elif(command == '/py_param'):
        manage_py_param(self)

def manage_py_state(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_py.state_py = data
        parser_json.upload_state()
        terminal.addLog("com", "New state received")
        capture.restart_lidar_capture()

def manage_py_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        command.manage_command(lvl1, lvl2, lvl3)
        terminal.addPost("py", lvl1, lvl2, lvl3)
