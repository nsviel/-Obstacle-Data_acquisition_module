#---------------------------------------------
from src.param import param_capture
from src.HTTPS import https_server_get
from src.HTTPS import https_server_post
from src.misc import terminal
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import os


class S(BaseHTTPRequestHandler):
    def do_GET(self):
        https_server_get.manage_get(self);

    def do_POST(self):
        https_server_post.manage_post(self);

    def log_message(self, format, *args):
        return

def start_daemon(server_class=HTTPServer, handler_class=S):
    try:
        address = ("", param_capture.state_capture["self"]["http_server_port"])

        param_capture.https_server = ThreadingHTTPServer(address, handler_class)
        param_capture.http_server_daemon = threading.Thread(target=param_capture.https_server.serve_forever)
        param_capture.http_server_daemon.daemon = True
        param_capture.http_server_daemon.start()
        terminal.addDaemon("#", "ON", "HTTPS server")
    except:
        terminal.fatal_error()
        os.system("sudo kill -9 $(ps -A | grep python | awk '{print $1}')")

def stop_daemon():
    param_capture.https_server.shutdown()
    param_capture.http_server_daemon.join()
    terminal.addDaemon("#", "OFF", "HTTPS server")
