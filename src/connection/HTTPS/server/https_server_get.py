#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /get_state_ground
# - /get_state_network
#---------------------------------------------

from src.param import param_capture
from src.connection.HTTPS.server import https_server_fct
import json


def manage_get(self):
    command = str(self.path)
    if(command == '/http_ping'):
        self.send_response(200)
    elif(command == '/get_state_ground'):
        data = json.dumps(param_capture.state_ground).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    elif(command == '/get_state_network'):
        data = json.dumps(param_capture.state_network).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    else:
        print("[error] HTTP GET command not known [%s]"% command)
