#! /usr/bin/python
#---------------------------------------------
# Possible POST command:
# - /py_state
# - /py_param
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json
from src import capture

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/py_state'):
        http_server_post.manage_py_state(self)
    elif(command == '/py_param'):
        http_server_post.manage_py_param(self)

def manage_py_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = http_server_fct.decipher_json(data)
        param_py.state_py[lvl1][lvl2] = lvl3
        if(str(lvl2) == "device" or str(lvl2) == "ip"):
            capture.restart_capture()
        if(str(lvl2) == "speed"):
            lidar.start_l1_motor()
            lidar.start_l2_motor()
        if(str(lvl2) == "lidar_1"):
            lidar.start_l1_motor()
            lidar.start_l2_motor()

def manage_py_state(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_py.state_py = data
        parser_json.upload_state()
