#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os
import pcapy
import json

# Connection information
hubium_ip = "127.0.0.1"
hubium_sock_port = 2370
hubium_http_port = 8000

# Hubium
mqtt_topic = "ai_obstacle"
mqtt_ip = "127.0.0.1"
mqtt_port = 8888
edge_ip = "127.0.0.1"
edge_port = 8888
valeo_ip = "127.0.0.1"

hubium_state = json.load(open('src/state.json', "r"))
mqtt_connected = False
velo_connected = False
vale_connected = False
edge_connected = False
ia_connected = False
