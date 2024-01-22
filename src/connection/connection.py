#---------------------------------------------
from src.param import param_capture
from src.connection.SOCK import sock_client
from src.interface import lidar
from src.state import state
from src.interface import device
from src.utils import terminal
from src.base import daemon
from src.connection.HTTPS.client import https_client_con
from src.interface import capture

import socket
import threading


class Connection(daemon.Daemon):
    def __init__(self):
        self.name = "Connection";
        self.run_sleep = 0.5;

    def thread_function(self):
        # Test connections
        https_client_con.test_connection_edge()
        lidar.test_connection()
        device.update_list()

        # Update state
        state.upload_states()
        update_nb_thread()

    def stop_daemon(self):
        self.run_thread = False
        terminal.addDaemon("#", "OFF", self.name)
        capture.stop_lidar_capture();

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
    param_capture.state_ground["capture"]["info"]["nb_thread"] = threading.active_count()

def check_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    is_open = False
    if result == 0:
       is_open = True
    else:
        terminal.addLog("error", "Port \033[1;32m%d\033[0m is closed"% port)
    sock.close()
    return is_open;
