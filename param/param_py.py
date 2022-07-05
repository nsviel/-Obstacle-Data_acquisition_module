#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Thread
run_loop = True;
run_thread_con = False

# Parameter
gui_width = 600;
gui_height = 750;
with_geolocalization = False
path_state = "param/state.json"

# Connection
pywardium_ip = "127.0.0.1"
http_connected = False
socket_connected = False
ssd_connected = False
socket = None
socket_port = 2371

# Geolocalization
geo_country = "France"

# SSD
ssd_path = "/media/" + os.getlogin() + "/lidar_ssd"
ssd_space_total = 0
ssd_space_used = 0

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
