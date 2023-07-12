#---------------------------------------------
from src.param import param_capture

from src.connection.HTTPS import https_server
from src.connection.SOCK import sock_client
from src.perf import throughput_l1
from src.perf import throughput_l2
from src.perf import network_perf

from src.connection import connection
from src.state import state
from src.interface import capture
from src.utils import parser_json
from src.interface import device
from src.utils import terminal
from src.interface import lidar

import time


daemon_connection = connection.Connection()
daemon_network = network_perf.Network()
daemon_throughput_l1 = throughput_l1.Throughput_l1()
daemon_throughput_l2 = throughput_l2.Throughput_l2()

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
    daemon_throughput_l1.start_daemon()
    daemon_throughput_l2.start_daemon()
    daemon_network.start_daemon()
    daemon_connection.start_daemon()
    terminal.addLog("OK", "Program initialized")
    terminal.addLine()

def loop():
    time.sleep(param_capture.tic_loop)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_capture.path_state_capture, param_capture.state_capture)
    capture.stop_lidar_capture()
    daemon_connection.stop_daemon()
    https_server.stop_daemon()
    daemon_throughput_l1.stop_daemon()
    daemon_throughput_l2.stop_daemon()
    daemon_network.stop_daemon()
    terminal.delai()
