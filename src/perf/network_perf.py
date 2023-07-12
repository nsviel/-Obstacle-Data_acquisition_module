#---------------------------------------------
from src.param import param_capture
from src.perf import network_ping
from src.utils import parser_json
from src.utils import terminal
from src.utils import daemon

import time


class Network(daemon.Daemon):
    def thread_function(self):
        # Ping stuff
        network_ping.compute_ping(self.list_latency, self.list_interruption, self.list_reliability)

        # Update state file and sleep one second
        parser_json.upload_file(param_capture.path_state_network, param_capture.state_network)
        time.sleep(param_capture.tic_network)

    name = "Network performance";
    run_sleep = 0.5;
    list_reliability = []
    list_latency = []
    list_interruption = []
