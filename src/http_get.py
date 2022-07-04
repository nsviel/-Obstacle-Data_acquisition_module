#! /usr/bin/python
#---------------------------------------------

from src import http
from param import param_hu
from param import param_py
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

def get_state():
    is_loaded = False
    if(param_py.http_connected):
        try:
            sock = client.HTTPConnection(param_hu.hubium_ip, param_hu.hubium_http_port, timeout=1)
            sock.request("GET", "/state")
            response = sock.getresponse()
            data = response.read()
            param_hu.hubium_json = json.loads(data)
            sock.close()
            is_loaded = True
        except:
            http.connection_closed()

        if(is_loaded):
            connection.parse_state_json()
