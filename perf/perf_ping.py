#---------------------------------------------
from param import param_py
from src import specific

import datetime
import os


def ping(ip, list_latency, list_interruption):
    # Retrieve latency
    os.system("ping -c 1 -t 1 " + ip + " > perf/ping 2>/dev/null")
    with open('perf/ping', 'r') as file:
        data = file.read().rstrip()
    id_b = data.find("time=") + 5
    id_e = data.find(" ms")

    # Compute latency
    if(id_b != -1 and id_e != -1):
        param_py.has_been_connected = True
        latency = float(data[id_b:id_e])
        specific.list_stack(list_latency, latency, 10)
        param_py.state_net["local_cloud"]["latency"]["value"] = latency
        param_py.state_net["local_cloud"]["latency"]["min"] = min(list_latency)
        param_py.state_net["local_cloud"]["latency"]["max"] = max(list_latency)
        param_py.state_net["local_cloud"]["latency"]["mean"] = specific.mean(list_latency)

        # Compute network interruption time
        if(param_py.has_been_deconnected):
            param_py.has_been_deconnected = False
            interruption_end = datetime.datetime.now()
            delta = interruption_end - interruption_time
            specific.list_stack(list_interruption, delta, 10)
            param_py.state_net["local_cloud"]["interruption"]["value"] = delta
            param_py.state_net["local_cloud"]["interruption"]["min"] = min(list_interruption)
            param_py.state_net["local_cloud"]["interruption"]["max"] = max(list_interruption)
            param_py.state_net["local_cloud"]["interruption"]["mean"] = specific.mean(list_interruption)

    # If any, compute interruption time
    if(data.find("100% packet loss") != -1 and param_py.has_been_connected):
        param_py.has_been_deconnected = True
        interruption_time = datetime.datetime.now()
