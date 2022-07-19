#! /usr/bin/python
#---------------------------------------------

from param import param_py

from threading import Thread

import iperf3


def start_daemon():
    thread_con = Thread(target = thread_perf_client)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_perf = False

def thread_perf_client():
    param_hu.run_thread_perf = True
    while param_hu.run_thread_perf:
        pass
