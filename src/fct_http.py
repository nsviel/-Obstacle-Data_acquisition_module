#! /usr/bin/python
#---------------------------------------------

from src import fct_param
import http.client


def geo_connection():
    #-------------

    IP = fct_param.geo_server_ip
    PORT = fct_param.geo_server_port
    fct_param.geo_connection = http.client.HTTPConnection(IP, PORT, timeout=2)

    print("[\033[92mGEO\033[0m] HTTP client connected")

    #-------------

def geo_disconnect():
    #-------------

    fct_param.geo_connection.close()

    #-------------

def geo_request():
    #-------------

    fct_param.geo_connection.request("GET", "/")
    response = connection.getresponse()
    fct_param.geo_coordinate = response

    #-------------
