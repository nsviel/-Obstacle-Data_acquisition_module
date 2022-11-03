#---------------------------------------------
from param import param_hu

import iperf3


def perf_network_server():
    server = iperf3.Server()
    result = server.run()

def print_result(result):
    pass
