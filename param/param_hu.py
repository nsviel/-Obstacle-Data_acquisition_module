#! /usr/bin/python
#---------------------------------------------

from param import param_py

import json


# Hubium
hubium_json = {}
hubium_status = "-"
hubium_ip = "127.0.0.1"
hubium_sock_port = 1
hubium_sock_connection = 1
hubium_httpd_port = 1

# MQTT
mqtt_connected = False
mqtt_topic = "ai_obstacle"
mqtt_ip = "127.0.0.1"
mqtt_port = 1

# Edge
edge_connected = False
edge_ip = "127.0.0.1"
edge_port = 1

# Valeo
vale_connected = False
valeo_ip = "127.0.0.1"
valeo_port = 1

# Velodium
velo_connected = False
velo_port = 1

# AI
ai_connected = False
