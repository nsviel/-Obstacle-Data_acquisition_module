#! /usr/bin/python
#---------------------------------------------

from src import parameter

import json
import http.client as client


def test_connection():
    sock = client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
    try:
        sock.request("GET", "/test")
        parameter.http_connected = True
    except:
        connection_closed()
    sock.close()

def connection_closed():
    parameter.http_connected = False
    parameter.mqtt_connected = False
