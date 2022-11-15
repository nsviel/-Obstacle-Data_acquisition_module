#---------------------------------------------
from param import param_py
from perf import perf_server_iperf

import multiprocessing as mp
import threading
import os
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_perf_server = False
    port = param_py.state_py["self"]["iperf_port"]
    command = 'iperf3 -c 127.0.0.1 -p ' + str(port) + ' -t 1 > /dev/null 2>&1'
    os.system(command)

def thread_perf_server():
    param_py.run_thread_perf_server = True
    while param_py.run_thread_perf_server :
        port = param_py.state_py["self"]["iperf_port"]
        process_net = mp.Process(target = perf_server_iperf.process_perf_server, args = (port,))
        process_net.start()
        time.sleep(1)
        process_net.terminate()
        process_net.join()
