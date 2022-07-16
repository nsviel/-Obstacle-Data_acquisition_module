#! /usr/bin/python
#---------------------------------------------

from param import param_py

from HTTP import http_server
from SOCK import socket_client

from src import connection
from src import file
from src import capture
from src import parser_json
from src import device


#Main function
def program():
    # Init variables
    init()

    # Start main loop program
    while param_py.run_loop:
        loop()

    # Join threads
    end()

#Sub-function
def init():
    file.load_configuration()
    connection.start_daemon()
    http_server.start_daemon()
    socket_client.connection()
    param_py.status = "Online"

def loop():
    a=1

def end():
    param_py.status = "Offline"
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    connection.stop_daemon()
    http_server.stop_daemon()
