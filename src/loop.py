#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import saving
from src import connection
from src import capture
from src import socket
from src import file


def init():
    file.init_state()
    saving.determine_path()
    saving.read_wallet()
    connection.start_thread_test_conn()
    socket.connection()
    param_py.status = "Online"

def loop():
    a=1

def end():
    param_py.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
