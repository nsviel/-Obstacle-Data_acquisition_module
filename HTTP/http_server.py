#! /usr/bin/python
#---------------------------------------------

from param import param_py
from HTTP import http_server_class

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server


def start_daemon(server_class=HTTPServer, handler_class=http_server_class.S):
    port = param_py.state_py["self"]["http_server_port"]
    address = ("", port)
    param_py.http_server = ThreadingHTTPServer(address, handler_class)
    param_py.http_server_daemon = threading.Thread(target=param_py.http_server.serve_forever)
    param_py.http_server_daemon.daemon = True
    param_py.http_server_daemon.start()

def stop_daemon():
    param_py.http_server.shutdown()
    param_py.http_server_daemon.join()
