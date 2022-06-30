#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import callback

import json
import http.client


def send_false_alarm():
    connection = http.client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=10)
    try:
        connection.request("GET", "/falsealarm")
    except:
        print("Connection refused")
    connection.close()

def test_connection():
    connection = http.client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=10)
    try:
        connection.request("GET", "/test")
        parameter.http_connected = True
    except:
        parameter.http_connected = False
    connection.close()
    callback.callback_connection()
