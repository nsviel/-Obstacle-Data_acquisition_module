#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /capture_state
#---------------------------------------------

from src.param import param_capture
from src.connection.HTTPS.server import https_server_fct
from src.utils import parser_json


def manage_get(self):
    command = str(self.path)
    if(command == '/http_ping'):
        self.send_response(200)
    elif(command == '/capture_state'):
        manage_capture_state(self)
    elif(command == '/network_state'):
        manage_network_state(self)
    else:
        print("[error] HTTP GET command not known")

def manage_capture_state(self):
    data = parser_json.load_state(param_capture.path_state_current + "state_ground.json")
    https_server_fct.send_get_response(self, data, "application/json")

def manage_network_state(self):
    data = parser_json.load_state(param_capture.path_state_current + "state_network.json")
    https_server_fct.send_get_response(self, data, "application/json")
