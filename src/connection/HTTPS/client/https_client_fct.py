#---------------------------------------------
from src.param import param_capture

import http.client


def network_info(dest):
    if(dest == "edge" or dest == "network"):
        ip = param_capture.state_edge["hub"]["info"]["ip"]
        port = param_capture.state_edge["hub"]["http"]["server_port"]

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
