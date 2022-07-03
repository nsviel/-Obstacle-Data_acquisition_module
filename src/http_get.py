#! /usr/bin/python
#---------------------------------------------

from src import http
from src import parameter

import json
import requests
import http.client as client


def get_falsealarm():
    if(parameter.http_connected):
        try:
            parameter.http_sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http.connection_closed()

def get_is_mqtt_connected():
    if(parameter.http_connected):
        try:
            sock = client.HTTPConnection(parameter.hubium_ip, parameter.hubium_http_port, timeout=1)
            sock.request("GET", "/is_mqtt_connected")
            response = sock.getresponse()
            data = response.read()
            parameter.hubium_state = json.loads(data)
            connection.parse_state_json()

            sock.close()
        except:
            http.connection_closed()
