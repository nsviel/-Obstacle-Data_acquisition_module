#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import parser_json

import json


def post_new_state_py(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)
        param_py.state_py = data
        parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    except:
        print('not valid JSON')

def post_new_param_py(self):
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
    except:
        print('not valid JSON')
