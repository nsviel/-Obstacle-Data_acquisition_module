#---------------------------------------------
from src.param import param_capture
from src.network import network_ping
from src.utils import parser_json
from src.utils import terminal
from src.base import daemon

import time


class Network(daemon.Daemon):
    def __init__(self):
        self.name = "Network performance";
        self.run_sleep = 0.5;
        self.list_reliability = []
        self.list_latency = []
        self.list_interruption = []

    def thread_function(self):
        network_ping.compute_ping(self)
