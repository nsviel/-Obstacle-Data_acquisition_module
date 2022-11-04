#---------------------------------------------
from param import param_py

from threading import Thread

import queue
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
    bdw_min = 1000
    bdw_max = 0
    bdw_list = []
    param_py.run_thread_perf = True
    while param_py.run_thread_perf:
        try:
            if(param_py.state_py["lidar_1"]["connected"] and param_py.state_py["lidar_1"]["activated"]):
                l1_mbs = perf_device(param_py.state_py["lidar_1"]["device"])
                [bdw_list, bdw_min, bdw_mean, bdw_max] = compute_throughput(l1_mbs, bdw_list, bdw_min, bdw_max)

                param_py.state_py["lidar_1"]["throughput"]["value"] = l1_mbs
                param_py.state_py["lidar_1"]["throughput"]["min"] = bdw_min
                param_py.state_py["lidar_1"]["throughput"]["mean"] = bdw_mean
                param_py.state_py["lidar_1"]["throughput"]["max"] = bdw_max
            else:
                param_py.state_py["lidar_1"]["throughput"]["value"] = 0
                param_py.state_py["lidar_1"]["throughput"]["min"] = 0
                param_py.state_py["lidar_1"]["throughput"]["mean"] = 0
                param_py.state_py["lidar_1"]["throughput"]["max"] = 0

                param_py.state_py["lidar_1"]["packet"]["value"] = 0
                param_py.state_py["lidar_1"]["packet"]["min"] = 0
                param_py.state_py["lidar_1"]["packet"]["mean"] = 0
                param_py.state_py["lidar_1"]["packet"]["max"] = 0
                time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(0.05)

def thread_perf_l2():
    bdw_min = 1000
    bdw_max = 0
    bdw_list = [0]
    param_py.run_thread_perf = True
    while param_py.run_thread_perf:
        try:
            if(param_py.state_py["lidar_2"]["connected"] and param_py.state_py["lidar_2"]["activated"]):
                l2_mbs = perf_device(param_py.state_py["lidar_2"]["device"])
                [bdw_list, bdw_min, bdw_mean, bdw_max] = compute_throughput(l2_mbs, bdw_list, bdw_min, bdw_max)

                param_py.state_py["lidar_2"]["throughput"]["value"] = l2_mbs
                param_py.state_py["lidar_2"]["throughput"]["min"] = bdw_min
                param_py.state_py["lidar_2"]["throughput"]["mean"] = bdw_mean
                param_py.state_py["lidar_2"]["throughput"]["max"] = bdw_max
            else:
                param_py.state_py["lidar_2"]["throughput"]["value"] = 0
                param_py.state_py["lidar_2"]["throughput"]["min"] = 0
                param_py.state_py["lidar_2"]["throughput"]["mean"] = 0
                param_py.state_py["lidar_2"]["throughput"]["max"] = 0

                param_py.state_py["lidar_2"]["packet"]["value"] = 0
                param_py.state_py["lidar_2"]["packet"]["min"] = 0
                param_py.state_py["lidar_2"]["packet"]["mean"] = 0
                param_py.state_py["lidar_2"]["packet"]["max"] = 0
                time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(0.05)

def compute_throughput(value, list, min, max):
    # Mean
    list.append(value)
    if(len(list) == 25):
        list.pop(0)
    val_mean = 0
    for bdw in list:
        val_mean += bdw
    val_mean /= len(list)

    # Min & max
    if(value > max):
        val_max = value
    else:
        val_max = max
    if(value < min):
        val_min = value
    else:
        val_min = min
    return [list, val_min, val_mean, val_max]

def perf_device(device):
    # Compute throughput
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_1 = net_stat.bytes_recv
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_2 = net_stat.bytes_recv
    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    return net_in
