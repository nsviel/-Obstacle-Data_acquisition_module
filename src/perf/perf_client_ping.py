#---------------------------------------------
from src.param import param_py
from src.misc import specific

import datetime
import os


def ping(ip, list_latency, list_interruption):
    # Retrieve latency
    os.system("ping -c 1 -t 1 " + ip + " > src/perf/ping 2>/dev/null")
    with open('src/perf/ping', 'r') as file:
        data = file.read().rstrip()
    id_b = data.find("time=") + 5
    id_e = data.find(" ms")

    # Compute latency
    #print(param_py.state_py["hubium"]["connected"])
    if(param_py.state_py["hubium"]["connected"] == True):
        param_py.has_been_connected = True
        param_py.has_been_deconnected = False
        latency = float(data[id_b:id_e])

        specific.list_stack(list_latency, latency, 10)
        param_py.state_perf["local_cloud"]["latency"]["value"] = latency
        param_py.state_perf["local_cloud"]["latency"]["min"] = min(list_latency)
        param_py.state_perf["local_cloud"]["latency"]["max"] = max(list_latency)
        param_py.state_perf["local_cloud"]["latency"]["mean"] = round(specific.mean(list_latency))

        # Compute network interruption time
        if(param_py.has_been_deconnected):
            interruption_end = datetime.datetime.now()
            delta = interruption_end - param_py.interruption_time

            specific.list_stack(list_interruption, delta.total_seconds(), 10)
            param_py.state_perf["local_cloud"]["interruption"]["value"] = delta.total_seconds()
            param_py.state_perf["local_cloud"]["interruption"]["min"] = min(list_interruption)
            param_py.state_perf["local_cloud"]["interruption"]["max"] = max(list_interruption)
            param_py.state_perf["local_cloud"]["interruption"]["mean"] = round(specific.mean(list_interruption))

    # If any, compute interruption time
    if(param_py.state_py["hubium"]["connected"] == False and param_py.has_been_connected):
        param_py.has_been_connected = False
        param_py.has_been_deconnected = True
        param_py.interruption_time = datetime.datetime.now()
