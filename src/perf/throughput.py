#---------------------------------------------
from src.param import param_capture
from src.utils import terminal
from src.base import daemon

import threading
import queue
import time
import psutil


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

def network_device(device):
    # Compute throughput
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_1 = net_stat.bytes_recv
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
    net_in_2 = net_stat.bytes_recv
    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    return net_in
