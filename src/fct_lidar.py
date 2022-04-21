#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from requests.exceptions import ConnectionError

import time
import requests


def lidar_start_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % fct_param.lidar_speed)
    #-------------

    #Motor speed value
    data = {
        'rpm': str(fct_param.lidar_speed),
    }

    lidar_send_data(data)

    #-------------

def lidar_stop_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    #-------------

    #Motor speed value
    data = {
        'rpm': '0',
    }

    lidar_send_data(data)

    #-------------

def lidar_send_data(data):
    #-------------

    #LiDAR 1
    try:
        request = requests.get(fct_param.lidar_1_url, timeout=1)
    except ConnectionError:
        print('%s does not exist' % fct_param.lidar_1_url)
    else:
        response = requests.post('http://192.168.1.201/cgi/setting', data=data)
        time.sleep(1)

    #LiDAR 2
    try:
        request = requests.get(fct_param.lidar_2_url, timeout=1)
    except ConnectionError:
        print('%s does not exist' % fct_param.lidar_2_url)
    else:
        response = requests.post('http://192.168.1.201/cgi/setting', data=data)
        time.sleep(1)

    #-------------
