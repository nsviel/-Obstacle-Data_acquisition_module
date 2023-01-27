#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /py_state
#---------------------------------------------

from param import param_py
from HTTPS import https_server_fct
from src import parser_json


def manage_get(self):
    command = str(self.path)
    if(command == '/test_http_conn'):
        self.send_response(200)
    elif(command == '/py_state'):
        manage_py_state(self)
    elif(command == '/perf_state'):
        manage_perf_state(self)

def manage_py_state(self):
    data = parser_json.load_state_utf8(param_py.path_state_py)
    https_server_fct.send_get_response(self, data, "application/json")

def manage_perf_state(self):
    data = parser_json.load_state_utf8(param_py.path_state_perf)
    https_server_fct.send_get_response(self, data, "application/json")
