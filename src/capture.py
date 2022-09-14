#! /usr/bin/python
#---------------------------------------------

from param import param_py
from SOCK import sock_client
from src import device
from src import io

from threading import Thread

import pcapy


def start_lidar_capture():
    thread_l1 = Thread(target = start_l1_capture)
    thread_l2 = Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    print("[\033[1;32mOK\033[0m] LiDAR capture deactivated")
    param_py.run_thread_l1 = False
    param_py.run_thread_l2 = False

def start_l1_capture():
    connected = param_py.state_py["lidar_1"]["connected"]
    l1_device = param_py.state_py["lidar_1"]["device"]
    if(connected):
        device_ok = device.check_if_device_exists(l1_device)
        if(device_ok):
            param_py.state_py["lidar_1"]["nb_packet"] = 0
            listener = pcapy.open_live(l1_device , 1248 , 1 , 0)
            param_py.run_thread_l1 = True
            print("[\033[1;32mOK\033[0m] LiDAR 1 capturing...")
            while param_py.run_thread_l1:
                if(param_py.state_py["lidar_1"]["activated"]):
                    (header, packet) = listener.next()
                    sock_client.send_packet_l1(packet)
                    param_py.state_py["lidar_1"]["nb_packet"] += 1

def start_l2_capture():
    connected = param_py.state_py["lidar_2"]["connected"]
    l2_device = param_py.state_py["lidar_2"]["device"]
    if(connected):
        device_ok = device.check_if_device_exists(l2_device)
        if(device_ok):
            param_py.state_py["lidar_2"]["nb_packet"] = 0
            param_py.run_thread_l2 = True
            listener = pcapy.open_live(l2_device , 1248 , 1 , 0)
            print("[\033[1;32mOK\033[0m] LiDAR 2 capturing...")
            while param_py.run_thread_l2:
                if(param_py.state_py["lidar_2"]["activated"]):
                    (header, packet) = listener.next()
                    sock_client.send_packet_l2(packet)
                    param_py.state_py["lidar_2"]["nb_packet"] += 1

def restart_capture():
    stop_lidar_capture()
    start_lidar_capture()
