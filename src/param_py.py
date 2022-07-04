#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os
import pcapy
import json


# Parameters
run = True;
run_thread_l1 = False
run_thread_l2 = False
gui_width = 600;
gui_height = 750;

# Options
with_two_lidar = False
with_writing = True
with_forwarding = True
with_geolocalization = False

# Connection information
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
ip_l1 = "http://192.168.1.201/cgi/setting"
ip_l2 = "http://192.168.1.202/cgi/setting"
pywardium_ip = "127.0.0.1"
http_sock = 0
http_connected = False
socket_connected = False

# LiDAR
device_l1 = "enxf8e43b6cecab"
device_l2 = "enxf8e43b6cdf6c"
nb_packet_l1 = 0
nb_packet_l2 = 0
lidar_speed = 600
thread_l1 = 0
thread_l2 = 0
thread_con = False

# State
time_capture = 0
geo_country = "France"
ssd_connected = False
capture_ID = 0
socket_out = 0

# Paths
path_ssd = "/media/" + os.getlogin() + "/lidar_ssd"
path_capture = ""
path_dir_l1 = ""
path_dir_l2 = ""
path_file_l1 = ""
path_file_l2 = ""
path_name = ""
