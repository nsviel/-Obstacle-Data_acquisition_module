#---------------------------------------------
from param import param_py

from HTTPS import https_server
from SOCK import sock_client
from perf import perf_lidar_bandwidth
from perf import perf_client_network
from perf import perf_server_network

from src import connection
from src import state
from src import capture
from src import parser_json
from src import device

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
    perf_lidar_bandwidth.start_daemon()
    connection.start_daemon()
    https_server.start_daemon()
    sock_client.connection()
    perf_client_network.start_daemon()
    perf_server_network.start_daemon()
    print("[\033[1;32mOK\033[0m] Program initialized...")

def loop():
    time.sleep(1)

def end():
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    connection.stop_daemon()
    https_server.stop_daemon()
    perf_lidar_bandwidth.stop_daemon()
    perf_client_network.stop_daemon()
    perf_server_network.stop_daemon()
    shutdown()

def shutdown():
    print("[\033[1;32mOK\033[0m] Program terminating", flush=True, end='')
    print("...2", flush=True, end='')
    time.sleep(1)
    print("...1", flush=True)
    time.sleep(1)
