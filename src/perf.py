#! /usr/bin/python
#---------------------------------------------

from param import param_py

from threading import Thread

import time
import psutil


def start_daemon():
    thread_l1 = Thread(target = thread_perf_l1)
    thread_l2 = Thread(target = thread_perf_l2)
    thread_l1.start()
    thread_l2.start()

def stop_daemon():
    param_py.run_thread_perf = False

def thread_perf_l1():
    param_py.run_thread_perf = True
    while param_py.run_thread_perf:
        try:
            if(param_py.state_py["lidar_1"]["connected"] and param_py.state_py["lidar_1"]["activated"]):
                l1_mbs = perf_device(param_py.state_py["lidar_1"]["device"])
                param_py.state_py["lidar_1"]["bandwidth"] = l1_mbs
            else:
                param_py.state_py["lidar_1"]["bandwidth"] = 0
                param_py.state_py["lidar_1"]["nb_packet"] = 0
        except:
            time.sleep(1)
            pass

def thread_perf_l2():
    param_py.run_thread_perf = True
    while param_py.run_thread_perf:
        try:
            if(param_py.state_py["lidar_2"]["connected"] and param_py.state_py["lidar_2"]["activated"]):
                l2_mbs = perf_device(param_py.state_py["lidar_2"]["device"])
                param_py.state_py["lidar_2"]["bandwidth"] = l2_mbs
            else:
                param_py.state_py["lidar_2"]["bandwidth"] = 0
                param_py.state_py["lidar_2"]["nb_packet"] = 0
        except:
            time.sleep(1)
            pass

def perf_device(device):
    # Compute bandwidth
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_1 = net_stat.bytes_recv
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_2 = net_stat.bytes_recv
    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    return net_in
