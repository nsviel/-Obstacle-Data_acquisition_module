#! /usr/bin/python
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json
from src import capture

import json


def post_param_py(self):
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
        if(str(lvl2) == "device" or str(lvl2) == "ip"):
            capture.restart_capture()
        if(str(lvl2) == "speed"):
            lidar.start_l1_motor()
            lidar.start_l2_motor()
        if(str(lvl2) == "lidar_1"):
            lidar.start_l1_motor()
            lidar.start_l2_motor()
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')

def post_new_state_py(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        param_py.state_py = data
        parser_json.upload_state()
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
