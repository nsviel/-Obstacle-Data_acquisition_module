#---------------------------------------------
from src.param import param_capture
from src.connection.SOCK import socket_client
from src.interface import device
from src.connection import connection
from src.utils import terminal

import threading
import pcapy
import re


def start_lidar_capture():
    thread_l1 = threading.Thread(target = start_l1_capture)
    thread_l2 = threading.Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    param_capture.run_thread_l1 = False
    param_capture.run_thread_l2 = False

def restart_lidar_capture():
    terminal.addDaemon("#", "restart", "LiDAR capture")
    stop_lidar_capture()
    start_lidar_capture()

def start_l1_capture():
    l1_device = param_capture.state_ground["lidar_1"]["info"]["device"]
    l1_port = param_capture.state_ground["capture"]["socket"]["server_l1_port"]
    socket = socket_client.Socket_client()

    # Check device
    device_ok = device.check_if_device_exists(l1_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l1_device)
        return

    # Start captue
    connected = param_capture.state_ground["lidar_1"]["info"]["connected"]
    if(connected and device_ok):
        param_capture.state_ground["lidar_1"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_1"]["running"] = True
        param_capture.run_thread_l1 = True
        ip = param_capture.state_edge["hub"]["info"]["ip"]
        port = param_capture.state_edge["hub"]["socket"]["server_l2_port"]

        listener = pcapy.open_live(l1_device , 1500, 0, 1)
        filter = "udp port 2368 or 2369 or port 8308 or port 8309"
        listener.setfilter(filter)
        terminal.addDaemon("#", "ON", "LiDAR 1 capture on [\033[1;32m%s\033[0m]"%l1_device)

        while param_capture.run_thread_l1 and param_capture.state_ground["lidar_1"]["info"]["connected"]:
            if(param_capture.state_ground["lidar_1"]["info"]["activated"]):
                (header, packet) = listener.next()
                if(packet != None):
                    socket.socket.sendto(packet, (ip, port))
                    if(len(packet) == 1248):
                        param_capture.state_ground["lidar_1"]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_capture.state_ground["lidar_2"]["packet"]["value"])
        terminal.addDaemon("#", "OFF", "LiDAR 1 capture")

def start_l2_capture():
    l2_device = param_capture.state_ground["lidar_2"]["info"]["device"]
    l2_port = param_capture.state_ground["capture"]["socket"]["server_l2_port"]
    socket = socket_client.Socket_client()

    # Check device
    device_ok = device.check_if_device_exists(l2_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l2_device)
        return

    # Start capture
    connected = param_capture.state_ground["lidar_2"]["info"]["connected"]
    if(connected and device_ok):
        param_capture.state_ground["lidar_2"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_2"]["running"] = True
        param_capture.run_thread_l2 = True
        ip = param_capture.state_edge["hub"]["info"]["ip"]
        port = param_capture.state_edge["hub"]["socket"]["server_l2_port"]

        listener = pcapy.open_live(l2_device, 1500, 0 , 1)
        filter = "udp port 2368 or 2369 or port 8308 or port 8309"
        listener.setfilter(filter)
        terminal.addDaemon("#", "ON", "LiDAR 2 capture on [\033[1;32m%s\033[0m]"%l2_device)

        while param_capture.run_thread_l2 and param_capture.state_ground["lidar_2"]["info"]["connected"]:
            if(param_capture.state_ground["lidar_2"]["info"]["activated"]):
                (header, packet) = listener.next()
                if(packet != None):
                    socket.socket.sendto(packet, (ip, port))
                    if(len(packet) == 1248):
                        param_capture.state_ground["lidar_2"]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_capture.state_ground["lidar_2"]["packet"]["value"])
        terminal.addDaemon("#", "OFF", "LiDAR 2 capture")

def restart_capture():
    stop_lidar_capture()
    start_lidar_capture()
