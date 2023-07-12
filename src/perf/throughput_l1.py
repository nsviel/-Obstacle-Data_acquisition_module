#---------------------------------------------
from src.param import param_capture
from src.perf import throughput
from src.utils import terminal
from src.utils import daemon

import threading
import queue
import time
import psutil


class Throughput_l1(daemon.Daemon):
    def thread_function(self):
        try:
            if(param_capture.state_capture["lidar_1"]["connected"] and param_capture.state_capture["lidar_1"]["activated"]):
                l1_mbs = throughput.network_device(param_capture.state_capture["lidar_1"]["device"])
                [tgp_list, tgp_min, tgp_mean, tgp_max] = throughput.compute_throughput(l1_mbs, tgp_list, tgp_min, tgp_max)

                param_capture.state_capture["lidar_1"]["throughput"]["value"] = l1_mbs
                param_capture.state_capture["lidar_1"]["throughput"]["min"] = tgp_min
                param_capture.state_capture["lidar_1"]["throughput"]["mean"] = tgp_mean
                param_capture.state_zapture["lidar_1"]["throughput"]["max"] = tgp_max
            else:
                param_capture.state_capture["lidar_1"]["throughput"]["value"] = 0
                param_capture.state_capture["lidar_1"]["throughput"]["min"] = 0
                param_capture.state_capture["lidar_1"]["throughput"]["mean"] = 0
                param_capture.state_capture["lidar_1"]["throughput"]["max"] = 0

                param_capture.state_capture["lidar_1"]["packet"]["value"] = 0
                param_capture.state_capture["lidar_1"]["packet"]["min"] = 0
                param_capture.state_capture["lidar_1"]["packet"]["mean"] = 0
                param_capture.state_capture["lidar_1"]["packet"]["max"] = 0
                time.sleep(1)
        except:
            time.sleep(1)

    name = "LiDAR 1 throughput";
    run_sleep = 0.05;
    tgp_min = 1000
    tgp_max = 0
    tgp_list = []
