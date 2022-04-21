#! /usr/bin/python
#---------------------------------------------

from src import fct_param


import time
import requests


def lidar_start_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m" + fct_param.lidar_speed + "\033[0m rpm")
    #-------------

    data = {
        'rpm': str(fct_param.lidar_speed),
    }
    response = requests.post('http://192.168.1.201/cgi/setting', data=data)
    time.sleep(1)

    #-------------

def lidar_stop_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    #-------------

    data = {
        'rpm': '0',
    }
    response = requests.post('http://192.168.1.201/cgi/setting', data=data)
    time.sleep(1)

    #-------------
