#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Parameters
run = True;
gui_width = 600;
gui_height = 600;

# Options
with_two_lidar = False
with_writing = True
with_forwarding = True
with_manual_naming = False
with_geolocalization = False

# Connection information
IP = {}
lidar_1_ip = "http://192.168.1.201/cgi/setting"
lidar_2_ip = "http://192.168.1.202/cgi/setting"
velo_ip = "127.0.0.1"
velo_port = 2370

# LiDAR
lidar_1_dev = "enxf8e43b6cecab"
lidar_2_dev = "enxf8e43b6cdf6c"
lidar_1_nb_packet = 0
lidar_2_nb_packet = 0
lidar_speed = 600

# State
time_capture = 0
geo_country = "France"
ssd_connected = False
capture_ID = 0

# Paths
path_ssd = "/media/ns/lidar_ssd"
path_capture = ""
path_dir_l1 = ""
path_dir_l2 = ""
path_file_l1 = ""
path_file_l2 = ""
