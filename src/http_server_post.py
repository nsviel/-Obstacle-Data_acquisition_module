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
