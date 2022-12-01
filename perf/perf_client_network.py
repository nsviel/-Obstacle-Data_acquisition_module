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
    param_py.process_client_iperf.terminate()
    param_py.process_client_iperf.join()

def thread_perf_server():
    reverse = False

    list_band = []
    list_reli = []
    list_jitt = []
    list_late = []
    list_inte = []

    list_band_rev = []
    list_reli_rev = []
    list_jitt_rev = []
    list_late_rev = []
    list_inte_rev = []

    param_py.run_thread_perf_client = True
    while param_py.run_thread_perf_client :
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["iperf_port"]
        reverse = not reverse

        # iperf3
        process_iperf(ip, port, reverse)
        if(reverse == False):
            perf_client_iperf.compute_net_state(list_band, list_reli, list_jitt)
        else:
            perf_client_iperf.compute_net_state_rev(list_band_rev, list_reli_rev, list_jitt_rev)

        # Ping
        perf_client_ping.ping(ip, list_late, list_inte)

        # Update state file and sleep one second
        parser_json.upload_file(param_py.path_state_perf, param_py.state_perf)
        time.sleep(1)

def process_iperf(ip, port, reverse):
    param_py.process_client_iperf = mp.Process(target = perf_client_iperf.process_perf_client, args = (ip, port, reverse))
    param_py.process_client_iperf.start()
    param_py.process_client_iperf.join()
