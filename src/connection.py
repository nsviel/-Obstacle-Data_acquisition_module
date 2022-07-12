#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import socket
from src import lidar
from src import capture
from src import parser_json

from threading import Thread

import time


def start_daemon():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_thread():
    param_py.run_thread_con = False
    capture.stop_lidar_capture()

def thread_test_connection():
    param_py.run_thread_con = True
    while param_py.run_thread_con:
        # Test connections
        socket.test_connection()
        lidar.test_connection()

        # Update state
        parser_json.upload_file(param_py.path_state_py, param_py.state_py)

        # Wait for 1 second
        time.sleep(1)
        pass
