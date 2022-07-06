#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# State
status = "Offline"
http_connected = False
socket_connected = False
ssd_connected = False

# Parameter
gui_width = 600;
gui_height = 750;
path_state_py = "param/state_py.json"
path_state_hu = "param/state_hu.json"
path_config = "param/config.json"

# Thread
run_loop = True;
run_thread_con = False

# Socket
socket = None
socket_listen = 2370

# Geolocalization
geo_country = "France"

# SSD
ssd_path = "/media/" + os.getlogin() + "/lidar_ssd"
ssd_space_total = 0
ssd_space_used = 0

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
