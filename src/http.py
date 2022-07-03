#! /usr/bin/python
#---------------------------------------------

from src import parameter

import json
import http.client


def test_connection():
    connection = http.client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
    try:
        connection.request("GET", "/test")
        parameter.http_connected = True
    except:
        parameter.http_connected = False
    connection.close()

def send_false_alarm():
    connection = http.client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
    try:
        connection.request("GET", "/falsealarm")
    except:
        print("No HTTP connection")
    connection.close()
