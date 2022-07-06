#! /usr/bin/python
#---------------------------------------------


# Thread
run_thread_l1 = False
run_thread_l2 = False

# Options
with_two_lidar = False
with_writing = True

# Connection information
ip_l1 = "http://192.168.1.201/cgi/setting"
ip_l2 = "http://192.168.1.202/cgi/setting"

# LiDAR
device_l1 = "enxf8e43b6cecab"
device_l2 = "enxf8e43b6cdf6c"
nb_packet_l1 = 0
nb_packet_l2 = 0
lidar_speed = 600

# State
l1_connected = False
l2_connected = False
time_capture = 0
capture_ID = 0

# Path
path_capture = ""
path_dir_l1 = ""
path_dir_l2 = ""
path_file_l1 = ""
path_file_l2 = ""
path_name = ""
