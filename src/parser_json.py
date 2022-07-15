#! /usr/bin/python
#---------------------------------------------

from param import param_py

import json


def load_file(path):
    file = open(path, "r")
    data = json.load(file)
    return data

def load_file_to_sock_data(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data

def load_file_to_sock_data_encoded(path):
    file = open(path)
    data = json.load(file)
    data_encoded = json.dumps(data).encode(encoding='utf_8')
    return data_encoded

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def upload_state():
    file = open(param_py.path_state_py, "w")
    json.dump(param_py.state_py, file, indent=4)

def upload_file_by_sock_data(path, data):
    file = open(path, 'w')
    data_loaded = json.loads(data)
    json.dump(data_loaded, file, indent=4)
