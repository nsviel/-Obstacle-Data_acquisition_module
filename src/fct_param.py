#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Parameters
run = True;
with_two_lidar = False
with_writing = True
with_forwarding = True
with_manual_naming = False

velo_IP = "127.0.0.1";
velo_port = 2370
lidar_1_dev = "enp34s0"
lidar_2_dev = "enxf8e43b6cdf6c"

# Statistics
lidar_1_nb_packet = 0
lidar_2_nb_packet = 0
duration = 0

# Program state
ssd_connected = False
capture_ID = 0
capture_L1_name = "capture_L1" + str(capture_ID)
capture_L2_name = "capture_L2" + str(capture_ID)

# Paths
path_ssd = "/media/ns/lidar_ssd"
path_capture = os.path.join(path_ssd, "capture")
path_dir_1 = os.path.join(path_capture, "lidar_1")
path_dir_2 = os.path.join(path_capture, "lidar_2")
path_lidar_1 = os.path.join(capture_L1_name + ".pcap")
path_lidar_2 = os.path.join(capture_L2_name + ".pcap")
