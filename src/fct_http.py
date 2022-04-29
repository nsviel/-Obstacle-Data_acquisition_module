#! /usr/bin/python
#---------------------------------------------

from src import fct_param
import http.client

# Parameters
geo_connection = 0
geo_server_ip = "127.0.0.1"
geo_server_port = 80
geo_coordinate = [0, 0]
geo_border = [48.862725, 2.287592]
geo_country = "France"


# Functions
def geo_connection():
    #-------------

    IP = geo_server_ip
    PORT = geo_server_port
    geo_connection = http.client.HTTPConnection(IP, PORT, timeout=2)

    print("[\033[92mGEO\033[0m] HTTP client connected")

    #-------------

def geo_disconnect():
    #-------------

    geo_connection.close()

    #-------------

def geo_request():
    #-------------

    geo_connection.request("GET", "/")
    response = connection.getresponse()
    geo_coordinate = response

    #-------------
