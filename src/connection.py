#---------------------------------------------
from param import param_py
from SOCK import sock_client
from src import lidar
from src import capture
from src import parser_json
from src import device
from src import terminal

import threading
import socket
import time


def start_daemon():
    try:
        thread_con = threading.Thread(target = thread_test_connection)
        thread_con.start()
        terminal.addDaemon("#", "ON", "Connection tests")
    except:
        pass

def stop_daemon():
    param_py.run_thread_con = False
    capture.stop_lidar_capture()
    terminal.addDaemon("#", "OFF", "Connection tests")

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

def check_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    is_open = False
    if result == 0:
       is_open = True
    else:
        print("[\033[1;31merror\033[0m] Port \033[1;32m%d\033[0m is closed"% port)
    sock.close()
    return is_open;
