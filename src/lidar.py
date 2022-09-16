#---------------------------------------------
from param import param_py
from src import capture

from requests.exceptions import ConnectionError

import time
import requests


def test_connection():
    l1_ip = param_py.state_py["lidar_1"]["ip"]
    l2_ip = param_py.state_py["lidar_2"]["ip"]
    l1_connected = param_py.state_py["lidar_1"]["connected"]
    l2_connected = param_py.state_py["lidar_2"]["connected"]

    l1_ok = send_lidar_parameter({}, l1_ip)
    l2_ok = send_lidar_parameter({}, l2_ip)

    param_py.state_py["lidar_1"]["connected"] = l1_ok
    param_py.state_py["lidar_2"]["connected"] = l2_ok

    if(l1_connected == False and l1_ok or l2_connected == False and l2_ok):
        param_py.state_py["lidar_1"]["packet"]["value"] = 0
        param_py.state_py["lidar_1"]["bandwidth"]["value"] = 0
        param_py.state_py["lidar_2"]["packet"]["value"] = 0
        param_py.state_py["lidar_2"]["bandwidth"]["value"] = 0
        capture.start_lidar_capture()

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
