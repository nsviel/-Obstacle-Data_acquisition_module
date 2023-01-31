#---------------------------------------------
from src.param import param_py

from src.HTTPS import https_server
from src.SOCK import sock_client
from src.perf import perf_throughput
from src.perf import perf_client_network
from src.perf import perf_server_network

from src.misc import connection
from src.misc import state
from src.misc import capture
from src.misc import parser_json
from src.misc import device
from src.misc import terminal
from src.misc import lidar

import time


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
    state.load_configuration()
    sock_client.connection()
    lidar.display_connection_status()
    https_server.start_daemon()
    perf_throughput.start_daemon()
    perf_client_network.start_daemon()
    perf_server_network.start_daemon()
    connection.start_daemon()
    terminal.addLog("OK", "Program initialized")
    terminal.addLine()

def loop():
    time.sleep(1)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    capture.stop_lidar_capture()
    connection.stop_daemon()
    https_server.stop_daemon()
    perf_throughput.stop_daemon()
    perf_client_network.stop_daemon()
    perf_server_network.stop_daemon()
