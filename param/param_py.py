#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# State
#--------------------
status = "Offline"
ip = "127.0.0.1"
#--------------------

# HTTP
http_connected = False
http_port = 1

# Parameter
path_state_py = "param/state.json"
path_config = "param/config.json"

# Edge info
edge_ip = "127.0.0.1"
edge_port = 1

# Thread
run_loop = True;
run_thread_con = False

# Socket
socket_connected = False
socket = None
socket_listen = 1

# Geolocalization
geo_country = "France"

# SSD
ssd_connected = False
ssd_path = "/media/" + os.getlogin() + "/lidar_ssd"
ssd_space_total = 0
ssd_space_used = 0

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
