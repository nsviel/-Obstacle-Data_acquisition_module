#! /usr/bin/python
#---------------------------------------------

from src import http
from src import param_hu
from src import param_py
from src import connection

import json
import requests
import http.client as client


def get_falsealarm():

    if(param_py.http_connected):
        try:
            sock = client.HTTPConnection(param_hu.hubium_ip, param_hu.hubium_http_port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http.connection_closed()

def get_is_mqtt_connected():
    is_loaded = False
    if(param_py.http_connected):
        try:
            sock = client.HTTPConnection(param_hu.hubium_ip, param_hu.hubium_http_port, timeout=1)
            sock.request("GET", "/is_mqtt_connected")
            response = sock.getresponse()
            data = response.read()
            param_hu.hubium_json = json.loads(data)
            sock.close()
        except:
            http.connection_closed()

        if(is_loaded):
            connection.parse_state_json()
