#---------------------------------------------
from src.param import param_capture

from src.connection.HTTPS.server import https_server
from src.connection.SOCK import sock_client
from src.network import throughput_l1
from src.network import throughput_l2
from src.network import network_perf

from src.connection import connection
from src.state import state
from src.interface import capture
from src.utils import parser_json
from src.interface import device
from src.utils import terminal
from src.interface import lidar
from src import deamon

import time


#Main function
def program():
    # Init variables
    init()

    # Start main loop program
    while param_capture.run_loop:
        loop()

    # Join threads
    end()

#Sub-function
def init():
    state.load_configuration()
    sock_client.connection()
    lidar.display_connection_status()
    https_server.start_server()
    daemon.start_daemons()
    terminal.addLog("OK", "Program initialized")
    terminal.addLine()

def loop():
    time.sleep(param_capture.tic_loop)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_capture.path_state_ground, param_capture.state_ground)
    capture.stop_lidar_capture()
    https_server.stop_server()
    daemon.stop_daemons()
    terminal.delai()
