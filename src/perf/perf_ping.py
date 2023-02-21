#---------------------------------------------
from src.param import param_py
from src.misc import specific
from src.misc import terminal

import datetime
import time
import os


def compute_ping(list_latency, list_interruption, list_reliability):
    data = make_ping()
    compute_timestamp()
    compute_latency(data, list_latency)
    compute_reliability(data, list_reliability)
    compute_interruption(list_interruption)

def compute_timestamp():
    timestamp = time.time()
    param_py.state_perf["local_cloud"]["timestamp"] = timestamp

def make_ping():
    ip = param_py.state_py["edge"]["ip"]
    os.system("ping -c 50 -i 0.002 -t 1 " + ip + " > src/state/ping.txt 2>/dev/null")
    with open('src/state/ping.txt', 'r') as file:
        data = file.read().rstrip()
    return data

def compute_latency(data, list_latency):
    if(param_py.state_py["edge"]["connected"] == True):
        id_b = data.find("time=") + 5
        id_e = data.find(" ms")
        latency = float(data[id_b:id_e])
        specific.list_stack(list_latency, latency, 10)

        param_py.state_perf["local_cloud"]["latency"]["value"] = latency
        param_py.state_perf["local_cloud"]["latency"]["min"] = min(list_latency)
        param_py.state_perf["local_cloud"]["latency"]["max"] = max(list_latency)
        param_py.state_perf["local_cloud"]["latency"]["mean"] = specific.mean(list_latency)

def compute_reliability(data, list_reliability):
    if(param_py.state_py["edge"]["connected"] == True):
        packetloss = float([x for x in data.split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
        reliability = 100 - packetloss
        specific.list_stack(list_reliability, reliability, 10)

        param_py.state_perf["local_cloud"]["reliability"]["value"] = reliability;
        param_py.state_perf["local_cloud"]["reliability"]["min"] = min(list_reliability)
        param_py.state_perf["local_cloud"]["reliability"]["max"] = max(list_reliability)
        param_py.state_perf["local_cloud"]["reliability"]["mean"] = specific.mean(list_reliability)

def compute_interruption(list_interruption):
    if(param_py.state_py["edge"]["connected"] == True):
        # Compute network interruption time
        if(param_py.has_been_deconnected):
            interruption_end = datetime.datetime.now()
            delta = interruption_end - param_py.interruption_time
            specific.list_stack(list_interruption, delta.total_seconds(), 10)

            param_py.state_perf["local_cloud"]["interruption"]["value"] = delta.total_seconds()
            param_py.state_perf["local_cloud"]["interruption"]["min"] = min(list_interruption)
            param_py.state_perf["local_cloud"]["interruption"]["max"] = max(list_interruption)
            param_py.state_perf["local_cloud"]["interruption"]["mean"] = specific.mean(list_interruption)

        param_py.has_been_connected = True
        param_py.has_been_deconnected = False

    # If any, compute interruption time
    if(param_py.state_py["edge"]["connected"] == False and param_py.has_been_connected):
        param_py.has_been_connected = False
        param_py.has_been_deconnected = True
        param_py.interruption_time = datetime.datetime.now()
