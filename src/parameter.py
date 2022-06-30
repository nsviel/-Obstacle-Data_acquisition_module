#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Parameters
run = True;
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
lidar_1_ip = "http://192.168.1.201/cgi/setting"
lidar_2_ip = "http://192.168.1.202/cgi/setting"
hubium_ip = "127.0.0.1"
hubium_sock_port = 2370
hubium_http_port = 8889
http_sock = 0
http_connected = False
socket_connected = False

# LiDAR
lidar_1_dev = "enxf8e43b6cecab"
lidar_2_dev = "enxf8e43b6cdf6c"
nb_packet_l1 = 0
nb_packet_l2 = 0
lidar_speed = 600

# State
time_capture = 0
geo_country = "France"
ssd_connected = False
capture_ID = 0
listener_l1 = 0
listener_l2 = 0
socket_out = 0
socket_ready = False

# Paths
path_ssd = "/media/ns/lidar_ssd"
path_capture = ""
path_dir_l1 = ""
path_dir_l2 = ""
path_file_l1 = ""
path_file_l2 = ""
path_name = ""
