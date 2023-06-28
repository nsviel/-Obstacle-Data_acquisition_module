#---------------------------------------------
# Possible POST command:
# - /capture_state
# - /capture_param
#---------------------------------------------

from src.param import param_capture
from src.connection.HTTPS import https_server_fct
from src.utils import parser_json
from src.interface import command
from src.utils import terminal
from src.interface import capture

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/capture_state'):
        manage_capture_state(self)
    elif(command == '/capture_param'):
        manage_capture_param(self)
    else:
        print("[error] HTTP POST command not known")

def manage_capture_state(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_capture.state_capture = data
        parser_json.upload_state()
        terminal.addLog("post", "New state received")
        capture.restart_lidar_capture()

def manage_capture_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        terminal.addPost("capture", lvl1, lvl2, lvl3)
        command.manage_command(lvl1, lvl2, lvl3)
