#---------------------------------------------
from src.param import param_capture

from src.HTTPS import https_server
from src.SOCK import sock_client
from src.network import network_throughput
from src.network import network_perf

from src.misc import connection
from src.misc import state
from src.interface import capture
from src.misc import parser_json
from src.interface import device
from src.misc import terminal
from src.interface import lidar

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
    https_server.start_daemon()
    network_throughput.start_daemon()
    network_perf.start_daemon()
    connection.start_daemon()
    terminal.addLog("OK", "Program initialized")
    terminal.addLine()

def loop():
    time.sleep(param_capture.tic_loop)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_capture.path_state_capture, param_capture.state_capture)
    capture.stop_lidar_capture()
    connection.stop_daemon()
    https_server.stop_daemon()
    network_throughput.stop_daemon()
    network_perf.stop_daemon()
    terminal.delai()
