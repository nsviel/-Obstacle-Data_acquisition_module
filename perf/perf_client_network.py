#---------------------------------------------
from param import param_py
from perf import perf_client_ping
from perf import perf_client_iperf
from src import parser_json

import multiprocessing as mp
import threading
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_perf_client = False

def thread_perf_server():
    list_bandwidth = []
    list_reliability = []
    list_jitter = []
    list_latency = []
    list_interruption = []

    param_py.run_thread_perf_client = True
    while param_py.run_thread_perf_client :
        # iperf3
        process_iperf()
        perf_client_iperf.compute_net_state(list_bandwidth, list_reliability, list_jitter)

        # Ping
        ip = param_py.state_py["hubium"]["ip"]
        perf_client_ping.ping(ip, list_latency, list_interruption)

        # Update state file and sleep one second
        parser_json.upload_file(param_py.path_state_perf, param_py.state_perf)
        time.sleep(1)

def process_iperf():
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["iperf_port"]
    process_net = mp.Process(target = perf_client_iperf.process_perf_server, args = (ip, port))
    process_net.start()
    time.sleep(1)
    process_net.terminate()
    process_net.join()
