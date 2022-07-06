#! /usr/bin/python
#---------------------------------------------

from param import param_li
from requests.exceptions import ConnectionError

import time
import requests


def test_lidar_connection():
    l1_connected = send_lidar_parameter({}, param_li.ip_l1)
    l2_connected = send_lidar_parameter({}, param_li.ip_l2)
    param_li.l1_connected = l1_connected
    param_li.l2_connected = l2_connected
    if(l1_connected == False):
        param_li.nb_packet_l1 = 0
    if(l2_connected == False):
        param_li.nb_packet_l2 = 0

def start_l1_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % param_li.lidar_speed)
    ip = param_li.ip_l1
    data = {'rpm': str(param_li.lidar_speed),}
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)


def stop_l1_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    ip = param_li.ip_l1
    data = {'rpm': '0',}
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def start_l2_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor activated at \033[96m%d\033[0m rpm" % param_li.lidar_speed)
    ip = param_li.ip_l2
    data = {'rpm': str(param_li.lidar_speed),}
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def stop_l2_motor():
    print("[\033[92mLID\033[0m] - LiDAR motor desactivated")
    ip = param_li.ip_l2
    data = {'rpm': '0',}
    if(send_lidar_parameter(data, ip) == False):
        print("[\033[92mLID\033[0m] - %s does not exist" % ip)

def send_lidar_parameter(data, ip):
    try:
        response = requests.post(ip, data=data, timeout=1)
        return True
    except:
        return False
