#---------------------------------------------
from src.param import param_py
from src.perf import perf_ping
from src.misc import parser_json
from src.misc import terminal

import threading
import time


def start_daemon():
    try:
        thread_con = threading.Thread(target = thread_perf_server)
        thread_con.start()
        terminal.addDaemon("#", "ON", "Network performance")
    except:
        print("[\033[1;32merror\033[0m]   Network performances")

def stop_daemon():
    param_py.run_thread_perf = False
    terminal.addDaemon("#", "OFF", "Network performance")

def thread_perf_server():
    list_throughput = []
    list_reliability = []
    list_latency = []
    list_interruption = []

    param_py.run_thread_perf = True
    while param_py.run_thread_perf :
        # Ping stuff
        perf_ping.compute_ping(list_latency, list_interruption, list_reliability)

        # Update state file and sleep one second
        parser_json.upload_file(param_py.path_state_perf, param_py.state_perf)
        time.sleep(1)
