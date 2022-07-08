#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import socket
from src import saving
from src import lidar
from src import capture
from src import file

from threading import Thread

import time


def start_thread_test_conn():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_thread():
    param_py.run_thread_con = False
    capture.stop_lidar_capture()

def thread_test_connection():
    param_py.run_thread_con = True
    while param_py.run_thread_con:
        # Test connections
        socket.test_con_sock()
        saving.test_con_ssd()
        lidar.test_con_lidar()

        # Update state
        file.update_state_file()

        # Wait for 1 second
        time.sleep(1)
        pass
