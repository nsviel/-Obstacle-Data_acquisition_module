#! /usr/bin/python
#---------------------------------------------

from param import param_py

from threading import Thread

import psutil


def start_daemon():
    thread_con = Thread(target = thread_perf_client)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_perf = False

def thread_perf_client():
    param_py.run_thread_perf = True
    while param_py.run_thread_perf:
        try:
            if(param_py.state_py["lidar_1"]["connected"] and param_py.state_py["lidar_1"]["activated"]):
                l1_mbs = perf_device(param_py.state_py["lidar_1"]["device"])
                param_py.state_py["lidar_1"]["bandwidth"] = l1_mbs
            else:
                param_py.state_py["lidar_1"]["bandwidth"] = 0

            if(param_py.state_py["lidar_2"]["connected"] and param_py.state_py["lidar_2"]["activated"]):
                l2_mbs = perf_device(param_py.state_py["lidar_2"]["device"])
                param_py.state_py["lidar_2"]["bandwidth"] = l2_mbs
            else:
                param_py.state_py["lidar_2"]["bandwidth"] = 0
        except:
            time.sleep(1)
            pass

def perf_device(device):

    # Compute bandwidth
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    #net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)
    #print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")

    return net_in
