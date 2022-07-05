#! /usr/bin/python
#---------------------------------------------

import json


def upload_json_file(path, data):
    file = open(path, 'w')
    data_loaded = json.loads(data)
    json.dump(data_loaded, file, indent=4)

def upload_state_lvl1_json(path, lvl1):
    file = open(path, "r")
    data = json.load(file)
    return data[lvl1]

def upload_state_lvl2_json(path, lvl1, lvl2):
    file = open(path, "r")
    data = json.load(file)
    return data[lvl1][lvl2]

def update_state_lvl1_json(path, lvl1, state):
    file = open(path, "r")
    data = json.load(file)
    if(data[lvl1] != state):
        data[lvl1] = state
        file = open(path, "w")
        json.dump(data, file, indent=4)
        file.truncate()

def update_state_lvl2_json(path, lvl1, lvl2, state):
    file = open(path, "r")
    data = json.load(file)
    if(data[lvl1][lvl2] != state):
        data[lvl1][lvl2] = state
        file = open(path, "w")
        json.dump(data, file, indent=4)
        file.truncate()

def parse_json(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data
