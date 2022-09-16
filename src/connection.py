#---------------------------------------------
from param import param_py
from SOCK import sock_client
from src import lidar
from src import capture
from src import parser_json
from src import device

from threading import Thread

import threading
import socket
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
        update_nb_thread()

        # Wait for 1 second
        time.sleep(1)

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update_nb_thread():
    param_py.state_py["self"]["nb_thread"] = threading.active_count()
