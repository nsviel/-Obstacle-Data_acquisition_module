#---------------------------------------------
from param import param_py
from SOCK import sock_client
from src import device
from src import io
from src import connection
from src import terminal

import threading
import pcapy


def start_lidar_capture():
    thread_l1 = threading.Thread(target = start_l1_capture)
    thread_l2 = threading.Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    param_py.run_thread_l1 = False
    param_py.run_thread_l2 = False

def start_l1_capture():
    l1_device = param_py.state_py["lidar_1"]["device"]
    l1_port = param_py.state_py["self"]["l1_port"]

    # Check device
    device_ok = device.check_if_device_exists(l1_device)
    if(device_ok == False):
        terminal.addLog("error", "device [\033[1;32m%s\033[0m does not exists"% l1_device)
        return

    # Start capture
    connected = param_py.state_py["lidar_1"]["connected"]
    if(connected and device_ok):
        param_py.state_py["lidar_1"]["packet"]["value"] = 0
        param_py.state_py["lidar_1"]["running"] = True
        param_py.run_thread_l1 = True
        
        listener = pcapy.open_live(l1_device , 1248 , 1 , 0)
        terminal.addDaemon("#", "ON" "LiDAR 1 capture")

        #port_ok = connection.check_port_open(l1_port)
        while param_py.run_thread_l1:
            if(param_py.state_py["lidar_1"]["activated"]):
                (header, packet) = listener.next()
                print(len(packet))
                sock_client.send_packet_l1(packet)
                param_py.state_py["lidar_1"]["packet"]["value"] += 1
        terminal.addDaemon("#", "OFF" "LiDAR 1 capture")

def start_l2_capture():
    connected = param_py.state_py["lidar_2"]["connected"]
    l2_device = param_py.state_py["lidar_2"]["device"]
    l2_port = param_py.state_py["self"]["l2_port"]
    device_ok = device.check_if_device_exists(l2_device)
    if(connected and device_ok):
        param_py.state_py["lidar_2"]["packet"]["value"] = 0
        param_py.state_py["lidar_2"]["running"] = True
        param_py.run_thread_l2 = True
        listener = pcapy.open_live(l2_device , 1248 , 1 , 0)
        terminal.addDaemon("#", "ON" "LiDAR 2 capture")

        #port_ok = connection.check_port_open(l2_port)
        while param_py.run_thread_l2:
            if(param_py.state_py["lidar_2"]["activated"]):
                (header, packet) = listener.next()
                sock_client.send_packet_l2(packet)
                param_py.state_py["lidar_2"]["packet"]["value"] += 1
        terminal.addDaemon("#", "OFF" "LiDAR 2 capture")

def restart_capture():
    stop_lidar_capture()
    start_lidar_capture()
