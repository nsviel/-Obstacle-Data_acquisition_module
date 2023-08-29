#---------------------------------------------
from src.param import param_capture
from src.interface import capture
from src.utils import terminal

from requests.exceptions import ConnectionError

import time
import requests


# LiDAR connection
def test_connection():
    l1_ip = param_capture.state_ground["lidar_1"]["ip"]
    l2_ip = param_capture.state_ground["lidar_2"]["ip"]
    l1_connected = param_capture.state_ground["lidar_1"]["connected"]
    l2_connected = param_capture.state_ground["lidar_2"]["connected"]

    l1_ok = send_lidar_parameter(l1_ip, {})
    l2_ok = send_lidar_parameter(l2_ip, {})

    if(l1_ok != l1_connected):
        if(l1_ok == True):
            terminal.addLog("#", "LiDAR \033[1;34m1\033[0m connection \033[1;32mON\033[0m")
        else:
            terminal.addLog("#", "LiDAR \033[1;34m1\033[0m connection \033[1;31mOFF\033[0m")

    if(l2_ok != l2_connected):
        if(l2_ok == True):
            terminal.addLog("#", "LiDAR \033[1;34m2\033[0m connection \033[1;32mON\033[0m")
        else:
            terminal.addLog("#", "LiDAR \033[1;34m2\033[0m connection \033[1;31mOFF\033[0m")

    param_capture.state_ground["lidar_1"]["connected"] = l1_ok
    param_capture.state_ground["lidar_2"]["connected"] = l2_ok

    if(l1_connected == False and l1_ok or l2_connected == False and l2_ok):
        param_capture.state_ground["lidar_1"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_1"]["throughput"]["value"] = 0
        param_capture.state_ground["lidar_2"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_2"]["throughput"]["value"] = 0
        capture.start_lidar_capture()
def display_connection_status():
    l1_ip = param_capture.state_ground["lidar_1"]["ip"]
    l2_ip = param_capture.state_ground["lidar_2"]["ip"]
    l1_ok = send_lidar_parameter(l1_ip, {})
    l2_ok = send_lidar_parameter(l2_ip, {})

    if(l1_ok):
        terminal.addLog("#", "LiDAR \033[1;34m1\033[0m connection \033[1;32mON\033[0m")
    else:
        terminal.addLog("#", "LiDAR \033[1;34m1\033[0m connection \033[1;31mOFF\033[0m")

    if(l2_ok):
        terminal.addLog("#", "LiDAR \033[1;34m2\033[0m connection \033[1;32mON\033[0m")
    else:
        terminal.addLog("#", "LiDAR \033[1;34m2\033[0m connection \033[1;31mOFF\033[0m")
def send_lidar_parameter(ip, data):
    address = "http://" + str(ip) + "/cgi/setting"
    try:
        response = requests.post(address, data=data, timeout=1)
        time.sleep(1)
        return True
    except:
        return False

# LiDAR 1 motor
def start_l1_motor():
    ip = param_capture.state_ground["lidar_1"]["ip"]
    speed = param_capture.state_ground["lidar_1"]["speed"]
    data = {'rpm': str(speed),}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m1\033[0m motor \033[1;32mON\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_capture.state_ground["lidar_1"]["running"] = True
def stop_l1_motor():
    ip = param_capture.state_ground["lidar_1"]["ip"]
    data = {'rpm': '0',}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m1\033[0m motor \033[1;31mOFF\033[0m")
        param_capture.state_ground["lidar_1"]["running"] = False
def restart_l1_motor():
    terminal.addLog("com", "LiDAR \033[96m1\033[0m motor \033[1;34mRESTART\033[0m")
    stop_l1_motor()
    start_l1_motor()
def change_l1_speed():
    ip = param_capture.state_ground["lidar_1"]["ip"]
    speed = param_capture.state_ground["lidar_1"]["speed"]
    data = {'rpm': str(speed),}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m1\033[0m motor \033[1;32mON\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_capture.state_ground["lidar_1"]["running"] = True

# LiDAR 2 motor
def start_l2_motor():
    ip = param_capture.state_ground["lidar_2"]["ip"]
    speed = param_capture.state_ground["lidar_2"]["speed"]
    data = {'rpm': speed,}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m2\033[0m motor \033[1;32mON\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_capture.state_ground["lidar_2"]["running"] = True
def stop_l2_motor():
    ip = param_capture.state_ground["lidar_2"]["ip"]
    data = {'rpm': '0',}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m2\033[0m motor \033[1;31mOFF\033[0m")
        param_capture.state_ground["lidar_2"]["running"] = False
def restart_l2_motor():
    terminal.addLog("com", "LiDAR \033[96m2\033[0m motor \033[1;34mRESTART\033[0m")
    stop_l2_motor()
    start_l2_motor()
def change_l2_speed():
    ip = param_capture.state_ground["lidar_2"]["ip"]
    speed = param_capture.state_ground["lidar_2"]["speed"]
    data = {'rpm': speed,}
    if(send_lidar_parameter(ip, data)):
        terminal.addLog("com", "LiDAR \033[96m2\033[0m motor \033[1;32mON\033[0m at \033[96m%d\033[0m rpm" % speed)
        param_capture.state_ground["lidar_2"]["running"] = True
