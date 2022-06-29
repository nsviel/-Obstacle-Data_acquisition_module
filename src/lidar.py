#! /usr/bin/python
#---------------------------------------------

from src import parameter
from requests.exceptions import ConnectionError

import time
import requests


def start_motor(ip):
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % parameter.lidar_speed)
    #-------------

    #Motor speed value
    data = {
        'rpm': str(parameter.lidar_speed),
    }

    send_parameter(data, ip)

    #-------------

def stop_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    #-------------
    ip = parameter.lidar_1_ip
    #Motor speed value
    data = {
        'rpm': '0',
    }

    send_parameter(data, ip)

    #-------------

def send_parameter(data, ip):
    #-------------

    try:
        request = requests.get(ip, timeout=1)
    except ConnectionError:
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)
    else:
        response = requests.post(ip, data=data)
        time.sleep(1)

    #-------------
