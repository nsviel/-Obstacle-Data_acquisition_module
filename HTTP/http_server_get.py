#! /usr/bin/python
#---------------------------------------------

from param import param_py
from HTTP import http_server_fct
from src import parser_json
from src import lidar

import json


def get_geo(self):
    pass

def get_test_http_conn(self):
    self.send_response(200)

def get_state_py(self):
    http_server_fct.post_state(self, param_py.path_state_py)

def get_lidar_1_start():
    lidar.start_l1_motor()

def get_lidar_1_stop():
    lidar.stop_l1_motor()

def get_lidar_2_start():
    lidar.start_l2_motor()

def get_lidar_2_stop():
    lidar.stop_l2_motor()
