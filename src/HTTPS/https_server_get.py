#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /capture_state
#---------------------------------------------

from src.param import param_capture
from src.HTTPS import https_server_fct
from src.misc import parser_json


def manage_get(self):
    command = str(self.path)
    if(command == '/test_http_conn'):
        self.send_response(200)
    elif(command == '/capture_state'):
        manage_capture_state(self)
    elif(command == '/network_state'):
        manage_network_state(self)

def manage_capture_state(self):
    data = parser_json.load_state_utf8(param_capture.path_state_capture)
    https_server_fct.send_get_response(self, data, "application/json")

def manage_network_state(self):
    data = parser_json.load_state_utf8(param_capture.path_state_network)
    https_server_fct.send_get_response(self, data, "application/json")
