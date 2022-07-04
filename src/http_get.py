#! /usr/bin/python
#---------------------------------------------

from src import http
from src import parameter
from src import connection

import json
import requests
import http.client as client


def get_falsealarm():

    if(parameter.http_connected):
        try:
            sock = client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http.connection_closed()

def get_is_mqtt_connected():
    is_loaded = False
    if(parameter.http_connected):
        try:
            sock = client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
            sock.request("GET", "/is_mqtt_connected")
            response = sock.getresponse()
            data = response.read()
            parameter.hubium_state = json.loads(data)
            sock.close()
        except:
            http.connection_closed()

        if(is_loaded):
            connection.parse_state_json()
