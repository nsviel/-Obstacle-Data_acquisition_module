#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import saving
from src import connection
from src import capture
from src import socket
from src import file


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
    file.config_from_file()
    saving.determine_path()
    saving.read_wallet()
    http_server.start_http_daemon()
    connection.start_thread_test_conn()
    socket.connection()
    param_py.status = "Online"

def loop():
    a=1

def end():
    param_py.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
