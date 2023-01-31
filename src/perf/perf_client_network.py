#---------------------------------------------
from src.param import param_py
from src.perf import perf_client_ping
from src.perf import perf_client_iperf
from src.misc import parser_json
from src.misc import terminal

import multiprocessing as mp
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
    param_py.run_thread_perf_client = False
    terminal.addDaemon("#", "OFF", "Network performance")
    if(param_py.state_py["perf"]["iperf_activated"]):
        param_py.process_client_iperf.terminate()
        param_py.process_client_iperf.join()

def thread_perf_server():
    list_bandwidth = []
    list_reliability = []
    list_jitter = []
    list_latency = []
    list_interruption = []

    param_py.run_thread_perf_client = True
    while param_py.run_thread_perf_client :
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["iperf_port"]

        # iperf3
        process_iperf(ip, port)
        perf_client_iperf.compute_net_state(list_bandwidth, list_reliability, list_jitter)

        # Ping
        perf_client_ping.ping(ip, list_latency, list_interruption)

        # Update state file and sleep one second
        parser_json.upload_file(param_py.path_state_perf, param_py.state_perf)
        time.sleep(1)

def process_iperf(ip, port):
    if(param_py.state_py["perf"]["iperf_activated"]):
        param_py.process_client_iperf = mp.Process(target = perf_client_iperf.process_perf_client, args = (ip, port))
        param_py.process_client_iperf.start()
        param_py.process_client_iperf.join()
