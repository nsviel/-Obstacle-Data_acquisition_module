#---------------------------------------------
from param import param_py
from threading import Thread
from perf import perf_ping
from perf import perf_iperf
from src import parser_json

import multiprocessing as mp

import time


def start_daemon():
    thread_con = Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_net = False

def thread_perf_server():
    list_bandwidth = []
    list_reliability = []
    list_jitter = []
    list_latency = []
    list_interruption = []
    param_py.run_thread_net = True
    while param_py.run_thread_net :
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["iperf_port"]
        process_net = mp.Process(target = perf_iperf.process_perf_server, args = (ip, port))
        process_net.start()
        process_net.join()
        perf_iperf.compute_net_state(list_bandwidth, list_reliability, list_jitter)
        perf_ping.ping(ip, list_latency, list_interruption)

        # Update state file and sleep one second
        parser_json.upload_file(param_py.path_state_net, param_py.state_net)
        time.sleep(1)
