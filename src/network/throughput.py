#---------------------------------------------
from src.param import param_capture
from src.network import throughput
from src.utils import terminal
from src.base import daemon

import threading
import queue
import time
import psutil
import statistics


class Throughput(daemon.Daemon):
    def __init__(self, name):
        self.name = name
        self.run_sleep = 0.05;
        self.tgp_min = 1000
        self.tgp_max = 0
        self.tgp_mean = 0
        self.tgp_list = [0]

    def thread_function(self):
        try:
            if(param_capture.state_ground[self.name]["info"]["connected"] and param_capture.state_ground[self.name]["info"]["activated"]):
                l2_mbs = self.compute_throughput(param_capture.state_ground[self.name]["info"]["device"])
                self.compute_throughput_range(l2_mbs)

                param_capture.state_ground["lidar_1"]["throughput"]["value"] = l2_mbs * 8
                param_capture.state_network["ground_to_edge"]["throughput"]["value"] = l2_mbs * 8
                param_capture.state_ground[self.name]["throughput"]["min"] = self.tgp_min * 8
                param_capture.state_ground[self.name]["throughput"]["mean"] = self.tgp_mean * 8
                param_capture.state_ground[self.name]["throughput"]["max"] = self.tgp_max * 8
            else:
                #param_capture.state_ground[self.name]["throughput"]["value"] = 0
                param_capture.state_ground[self.name]["throughput"]["min"] = 0
                param_capture.state_ground[self.name]["throughput"]["mean"] = 0
                param_capture.state_ground[self.name]["throughput"]["max"] = 0
                param_capture.state_ground[self.name]["packet"]["value"] = 0
                time.sleep(1)
        except:
            time.sleep(1)

    # Compute function
    def compute_throughput(self, device):
        net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
        net_in_1 = net_stat.bytes_recv
        time.sleep(1)
        net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[device]
        net_in_2 = net_stat.bytes_recv
        net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
        return net_in
    def compute_throughput_range(self, value):
        self.tgp_list.append(value)
        if(len(self.tgp_list) == 20):
            self.tgp_list.pop(0)

        self.tgp_mean = statistics.mean(self.tgp_list)
        self.tgp_min = min(self.tgp_list)
        self.tgp_max = max(self.tgp_list)
