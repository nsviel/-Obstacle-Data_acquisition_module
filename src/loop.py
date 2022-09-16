#---------------------------------------------
from param import param_py

from HTTP import http_server
from SOCK import sock_client

from src import connection
from src import state
from src import capture
from src import parser_json
from src import device
from src import perf

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
    perf.start_daemon()
    connection.start_daemon()
    http_server.start_daemon()
    sock_client.connection()
    param_py.state_py["self"]["status"] = "Online"
    print("[\033[1;32mOK\033[0m] Program initialized...")

def loop():
    time.sleep(1)

def end():
    print("[\033[1;32mOK\033[0m] Program terminating...")
    param_py.state_py["self"]["status"] = "Offline"
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    connection.stop_daemon()
    perf.stop_daemon()
    http_server.stop_daemon()
