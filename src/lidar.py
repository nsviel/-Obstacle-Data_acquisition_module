#! /usr/bin/python
#---------------------------------------------

from src import param_li
from requests.exceptions import ConnectionError

import time
import requests


def start_l1_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % param_li.lidar_speed)
    ip = param_li.ip_l1
    data = {'rpm': str(param_li.lidar_speed),}
    send_param_py(data, ip)

def stop_l1_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    ip = param_li.ip_l1
    data = {'rpm': '0',}
    send_param_py(data, ip)

def start_l2_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % param_li.lidar_speed)
    ip = param_li.ip_l2
    data = {'rpm': str(param_li.lidar_speed),}
    send_param_py(data, ip)

def stop_l2_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    ip = param_li.ip_l2
    data = {'rpm': '0',}
    send_param_py(data, ip)

def send_param_py(data, ip):
    #-------------

    try:
        request = requests.get(ip, timeout=1)
    except ConnectionError:
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)
    else:
        response = requests.post(ip, data=data)
        time.sleep(1)

    #-------------
