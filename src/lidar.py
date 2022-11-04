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

    l1_ok = send_lidar_parameter(l1_ip, {})
    l2_ok = send_lidar_parameter(l2_ip, {})

    param_py.state_py["lidar_1"]["connected"] = l1_ok
    param_py.state_py["lidar_2"]["connected"] = l2_ok

    if(l1_connected == False and l1_ok or l2_connected == False and l2_ok):
        param_py.state_py["lidar_1"]["packet"]["value"] = 0
        param_py.state_py["lidar_1"]["throughput"]["value"] = 0
        param_py.state_py["lidar_2"]["packet"]["value"] = 0
        param_py.state_py["lidar_2"]["throughput"]["value"] = 0
        capture.start_lidar_capture()

def start_l1_motor():
    ip = param_py.state_py["lidar_1"]["ip"]
    speed = param_py.state_py["lidar_1"]["speed"]
    data = {'rpm': str(speed),}
    if(send_lidar_parameter(ip, data)):
        print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;32mstart\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_py.state_py["lidar_1"]["running"] = True

def stop_l1_motor():
    ip = param_py.state_py["lidar_1"]["ip"]
    data = {'rpm': '0',}
    if(send_lidar_parameter(ip, data)):
        print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;31mstop\033[0m")
        param_py.state_py["lidar_1"]["running"] = False

def start_l2_motor():
    ip = param_py.state_py["lidar_2"]["ip"]
    speed = param_py.state_py["lidar_2"]["speed"]
    data = {'rpm': str(speed),}
    if(send_lidar_parameter(ip, data) == False):
        print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;32mstart\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_py.state_py["lidar_2"]["running"] = True

def stop_l2_motor():
    ip = param_py.state_py["lidar_2"]["ip"]
    data = {'rpm': '0',}
    if(send_lidar_parameter(ip, data)):
        print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;31mstop\033[0m")
        param_py.state_py["lidar_2"]["running"] = False

def send_lidar_parameter(ip, data):
    address = "http://" + str(ip) + "/cgi/setting"
    try:
        response = requests.post(address, data=data, timeout=1)
        return True
    except:
        return False
