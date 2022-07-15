#! /usr/bin/python
#---------------------------------------------

from param import param_py
from conn import http_server_get
from conn import http_server_post
from src import io

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server
import io


#Server functions
class S(BaseHTTPRequestHandler):
    def do_GET(self):
        manage_get(self);
    def do_POST(self):
        manage_post(self);
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

#Command functions
def manage_post(self):
    path = str(self.path)
    if(param_py.http_server_verbose):
        print("---- POST request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
    if(path == '/new_state_py'):
        http_server_post.post_new_state_py(self)
    if(path == '/new_param_py'):
        http_server_post.post_new_param_py(self)

def manage_get(self):
    path = str(self.path)
    if(param_py.http_server_verbose):
        print("---- GET request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        http_server_get.get_geo(self)
    elif(path == '/test_http_conn' or path == '/state'):
        http_server_get.get_test_http_conn(self)
    elif(path == '/state_py'):
        http_server_get.get_state_py(self)
