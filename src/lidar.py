#! /usr/bin/python
#---------------------------------------------

from param import param_py

from requests.exceptions import ConnectionError

import time
import requests


def test_connection():
    l1_ip = param_py.state_py["lidar_1"]["ip"]
    l2_ip = param_py.state_py["lidar_2"]["ip"]
    l1_connected = send_lidar_parameter({}, l1_ip)
    l2_connected = send_lidar_parameter({}, l2_ip)
    print(l1_connected)
    print(l2_connected)
    param_py.state_py["lidar_1"]["connected"] = l1_connected
    param_py.state_py["lidar_2"]["connected"] = l2_connected
    if(l1_connected == False):
        param_py.state_py["lidar_1"]["nb_packet"] = 0
    if(l2_connected == False):
        param_py.state_py["lidar_2"]["nb_packet"] = 0

def start_l1_motor():
    speed = param_py.state_py["lidar_1"]["speed"]
    ip = param_py.state_py["lidar_1"]["ip"]
    data = {'rpm': str(speed),}
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % speed)
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def stop_l1_motor():
    ip = param_py.state_py["lidar_1"]["ip"]
    data = {'rpm': '0',}
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def start_l2_motor():
    speed = param_py.state_py["lidar_2"]["speed"]
    ip = param_py.state_py["lidar_2"]["ip"]
    data = {'rpm': str(speed),}
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % speed)
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def stop_l2_motor():
    ip = param_py.state_py["lidar_2"]["ip"]
    data = {'rpm': '0',}
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def send_lidar_parameter(data, ip):
    try:
        response = requests.post(ip, data=data, timeout=1)
        return True
    except:
        return False
