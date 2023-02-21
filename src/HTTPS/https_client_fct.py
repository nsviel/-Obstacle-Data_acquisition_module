#---------------------------------------------
from src.param import param_py

import http.client


def network_info(dest):
    if(dest == "hu" or dest == "perf"):
        ip = param_py.state_py["module_edge"]["ip"]
        port = param_py.state_py["module_edge"]["http_server_port"]

    return [ip, port]

def send_https_ping(ip, port):
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    connected = False
    try:
        client.request("GET", "/test_http_conn")
        connected = True
    except:
        connected = False
    client.close()
    return connected
