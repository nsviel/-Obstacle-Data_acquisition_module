#---------------------------------------------
from src.param import param_py
from src.SOCK import sock_client
from src.interface import device
from src.misc import connection
from src.misc import terminal

import threading
import pcapy
import re


def start_lidar_capture():
    thread_l1 = threading.Thread(target = start_l1_capture)
    thread_l2 = threading.Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    param_py.run_thread_l1 = False
    param_py.run_thread_l2 = False

def restart_lidar_capture():
    terminal.addDaemon("#", "restart", "LiDAR capture")
    stop_lidar_capture()
    start_lidar_capture()

def start_l1_capture():
    l1_device = param_py.state_py["lidar_1"]["device"]
    l1_port = param_py.state_py["self"]["l1_port"]

    # Check device
    device_ok = device.check_if_device_exists(l1_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l1_device)
        return

    # Start captue
    connected = param_py.state_py["lidar_1"]["connected"]
    if(connected and device_ok):
        param_py.state_py["lidar_1"]["packet"]["value"] = 0
        param_py.state_py["lidar_1"]["running"] = True
        param_py.run_thread_l1 = True
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["sock_server_l2_port"]

        listener = pcapy.open_live(l1_device , 1500, 0, 1)
        terminal.addDaemon("#", "ON" "LiDAR 1 capture")

        while param_py.run_thread_l1 and param_py.state_py["lidar_1"]["connected"]:
            if(param_py.state_py["lidar_1"]["activated"]):
                (header, packet) = listener.next()
                if(packet != None):
                    param_py.sock_client.sendto(packet, (ip, port))
                    param_py.state_py["lidar_1"]["packet"]["value"] += 1
                    terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_py.state_py["lidar_2"]["packet"]["value"])
        terminal.addDaemon("#", "OFF" "LiDAR 1 capture")

def start_l2_capture():
    l2_device = param_py.state_py["lidar_2"]["device"]
    l2_port = param_py.state_py["self"]["l2_port"]

    # Check device
    device_ok = device.check_if_device_exists(l2_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l2_device)
        return

    # Start capture
    connected = param_py.state_py["lidar_2"]["connected"]
    if(connected and device_ok):
        param_py.state_py["lidar_2"]["packet"]["value"] = 0
        param_py.state_py["lidar_2"]["running"] = True
        param_py.run_thread_l2 = True
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["sock_server_l2_port"]

        listener = pcapy.open_live(l2_device, 1500, 0 , 1)
        terminal.addDaemon("#", "ON", "LiDAR 2 capture on \033[1;32m%s\033[0m"%l2_device)

        while param_py.run_thread_l2 and param_py.state_py["lidar_2"]["connected"]:
            if(param_py.state_py["lidar_2"]["activated"]):
                (header, packet) = listener.next()
                if(packet != None):
                    param_py.sock_client.sendto(packet, (ip, port))
                    param_py.state_py["lidar_2"]["packet"]["value"] += 1
                    terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_py.state_py["lidar_2"]["packet"]["value"])
        terminal.addDaemon("#", "OFF", "LiDAR 2 capture")

def restart_capture():
    stop_lidar_capture()
    start_lidar_capture()
