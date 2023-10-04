#---------------------------------------------
from src.param import param_capture
from src.utils import specific
from src.utils import terminal
import subprocess
import datetime
import time
import os


def compute_ping(self):
    data = make_ping()
    if(data != None):
        compute_timestamp()
        compute_latency(data, self.list_latency)
        compute_reliability(data, self.list_reliability)
        compute_interruption(self.list_interruption)

def make_ping():
    ip = param_capture.state_edge["hub"]["info"]["ip"]
    try:
        response = subprocess.check_output(
            ['ping', '-c', '3', '-i', '0.002', ip],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
    except subprocess.CalledProcessError:
        response = None
    return response

def compute_timestamp():
    timestamp = time.time()
    param_capture.state_network["ground_to_edge"]["timestamp"] = timestamp

def compute_latency(data, list_latency):
    if(param_capture.state_ground["interface"]["edge"]["http_connected"] == True and data != ""):
        try:
            id_b = data.find("time=") + 5
            id_e = data.find(" ms")
            latency = float(data[id_b:id_e])
            specific.list_stack(list_latency, latency, 10)

            param_capture.state_network["ground_to_edge"]["latency"]["value"] = latency
            param_capture.state_network["ground_to_edge"]["latency"]["min"] = min(list_latency)
            param_capture.state_network["ground_to_edge"]["latency"]["max"] = max(list_latency)
            param_capture.state_network["ground_to_edge"]["latency"]["mean"] = specific.mean(list_latency)
        except:
            pass

def compute_reliability(data, list_reliability):
    if(param_capture.state_ground["interface"]["edge"]["http_connected"] == True and data != ""):
        packetloss = float([x for x in data.split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
        reliability = 100 - packetloss
        specific.list_stack(list_reliability, reliability, 10)

        param_capture.state_network["ground_to_edge"]["reliability"]["value"] = reliability;
        param_capture.state_network["ground_to_edge"]["reliability"]["min"] = min(list_reliability)
        param_capture.state_network["ground_to_edge"]["reliability"]["max"] = max(list_reliability)
        param_capture.state_network["ground_to_edge"]["reliability"]["mean"] = specific.mean(list_reliability)

def compute_interruption(list_interruption):
    if(param_capture.state_ground["interface"]["edge"]["http_connected"] == True):
        # Compute network interruption time
        if(param_capture.has_been_deconnected):
            interruption_end = datetime.datetime.now()
            delta = interruption_end - param_capture.interruption_time
            specific.list_stack(list_interruption, delta.total_seconds(), 10)

            param_capture.state_network["ground_to_edge"]["interruption"]["value"] = delta.total_seconds()
            param_capture.state_network["ground_to_edge"]["interruption"]["min"] = min(list_interruption)
            param_capture.state_network["ground_to_edge"]["interruption"]["max"] = max(list_interruption)
            param_capture.state_network["ground_to_edge"]["interruption"]["mean"] = specific.mean(list_interruption)
        else:
            param_capture.state_network["ground_to_edge"]["interruption"]["value"] = 0

        param_capture.has_been_connected = True
        param_capture.has_been_deconnected = False

    # If any, compute interruption time
    if(param_capture.state_ground["interface"]["edge"]["http_connected"] == False and param_capture.has_been_connected):
        param_capture.has_been_connected = False
        param_capture.has_been_deconnected = True
        param_capture.interruption_time = datetime.datetime.now()
