#! /usr/bin/python
#---------------------------------------------

from src import fct_param

import requests


def lidar_start_motor():
    #-------------

    data = {
        'rpm': str(fct_param.lidar_speed),
    }
    response = requests.post('http://192.168.1.201/cgi/setting', data=data)

    #-------------

def lidar_stop_motor():
    #-------------

    data = {
        'rpm': '0',
    }
    response = requests.post('http://192.168.1.201/cgi/setting', data=data)

    #-------------
