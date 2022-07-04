#! /usr/bin/python
#---------------------------------------------

import json


# Hubium
hubium_json = json.load(open('src/state.json', "r"))
hubium_status = "-"
hubium_ip = "127.0.0.1"
hubium_sock_port = 2370
hubium_http_port = 8000

# MQTT
mqtt_connected = False
mqtt_topic = "ai_obstacle"
mqtt_ip = "127.0.0.1"
mqtt_port = 8888

# Edge
edge_connected = False
edge_ip = "127.0.0.1"
edge_port = 8888

# Valeo
vale_connected = False
valeo_ip = "127.0.0.1"
valeo_port = 8888

# Velodium
velo_connected = False
velo_port = 8888

# AI
ai_connected = False
