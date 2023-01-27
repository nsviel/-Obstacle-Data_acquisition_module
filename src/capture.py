#---------------------------------------------
from param import param_py
from SOCK import sock_client
from src import device
from src import io
from src import connection
from src import terminal
from blessings import Terminal

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

        listener = pcapy.open_live(l1_device , 1248 , 1 , 0)
        terminal.addDaemon("#", "ON" "LiDAR 1 capture")

        spinner = Halo(text='Capture packets: 0', spinner='dots')
        spinner.start()
        while param_py.run_thread_l1 and param_py.state_py["lidar_1"]["connected"]:
            if(param_py.state_py["lidar_1"]["activated"]):
                (header, packet) = listener.next()
                sock_client.send_packet_l1(packet)
                param_py.state_py["lidar_1"]["packet"]["value"] += 1
                spinner.enabled = True
                spinner.text = "Capture L2 packets: [\033[1;34m%d\033[0m]"%(param_py.state_py["lidar_2"]["packet"]["value"])
            else:
                spinner.enabled = False
        spinner.stop()
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

        listener = pcapy.open_live(l2_device , 1248 , 1 , 0)
        terminal.addDaemon("#", "ON", "LiDAR 2 capture")

        term = Terminal()
        while param_py.run_thread_l2:
            if(param_py.state_py["lidar_2"]["activated"]):
                (header, packet) = listener.next()
                sock_client.send_packet_l2(packet)
                param_py.state_py["lidar_2"]["packet"]["value"] += 1
                with term.location(term.width - 35, 10):
                    print("Capture L2 packets: [\033[1;34m%d\033[0m]"%(param_py.state_py["lidar_2"]["packet"]["value"]), end="")
        terminal.addDaemon("#", "OFF", "LiDAR 2 capture")

def restart_capture():
    stop_lidar_capture()
    start_lidar_capture()
