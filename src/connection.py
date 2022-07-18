#! /usr/bin/python
#---------------------------------------------

from param import param_py
from SOCK import sock_client
from src import lidar
from src import capture
from src import parser_json
from src import device

from threading import Thread

import time


def start_daemon():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_con = False
    capture.stop_lidar_capture()

def thread_test_connection():
    param_py.run_thread_con = True
    while param_py.run_thread_con:
        # Test connections
        lidar.test_connection()
        device.update_list()

        # Update state
        parser_json.upload_state()

        # Wait for 1 second
        time.sleep(1)
        pass
