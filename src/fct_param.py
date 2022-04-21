#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Parameters
run = True;
config_ok = True;

with_two_lidar = False
with_writing = True
with_forwarding = True
with_manual_naming = False

lidar_1_url = "http://192.168.1.201/"
lidar_2_url = "http://192.168.1.202/"
IP = {"localhost":"127.0.0.1", \
    "Server MINE":"10.201.224.13", \
    "Mine Louis":"10.201.20.110", \
    "Mine Nathan":"10.201.20.106", \
    "Portable Nathan":"192.168.153.147"}
velo_IP = "127.0.0.1"
velo_port = 2370
lidar_1_dev = "enp34s0"
lidar_2_dev = "enxf8e43b6cdf6c"
lidar_speed = 600

# Statistics
lidar_1_nb_packet = 0
lidar_2_nb_packet = 0
duration = 0

# Program state
ssd_connected = False
capture_L1_ID = 0
capture_L2_ID = 0
capture_L1_name = "capture_L1_" + str(capture_L1_ID)
capture_L2_name = "capture_L2_" + str(capture_L2_ID)

# Paths
path_ssd = "/media/ns/lidar_ssd"
path_capture = os.path.join(path_ssd, "capture")
path_dir_1 = os.path.join(path_capture, "lidar_1")
path_dir_2 = os.path.join(path_capture, "lidar_2")
path_lidar_1 = os.path.join(path_dir_1, capture_L1_name + ".pcap")
path_lidar_2 = os.path.join(path_dir_2, capture_L2_name + ".pcap")
