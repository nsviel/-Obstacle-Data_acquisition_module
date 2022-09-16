#---------------------------------------------
from param import param_py
from HTTP import http_server_get
from HTTP import http_server_post

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading


class S(BaseHTTPRequestHandler):
    def do_GET(self):
        http_server_get.manage_get(self);

    def do_POST(self):
        http_server_post.manage_post(self);

    def log_message(self, format, *args):
        return

def start_daemon(server_class=HTTPServer, handler_class=S):
    port = param_py.state_py["self"]["http_server_port"]
    address = ("", port)
    param_py.http_server = ThreadingHTTPServer(address, handler_class)
    param_py.http_server_daemon = threading.Thread(target=param_py.http_server.serve_forever)
    param_py.http_server_daemon.daemon = True
    param_py.http_server_daemon.start()

def stop_daemon():
    param_py.http_server.shutdown()
    param_py.http_server_daemon.join()
