#---------------------------------------------
# Possible POST command:
# - /post_state_ground
# - /post_state_edge
#---------------------------------------------

from src.param import param_capture
from src.connection.HTTPS.server import https_server_fct
from src.utils import parser_json
from src.interface import command
from src.utils import terminal
from src.interface import capture

import json


def manage_post(self):
    command = str(self.path)
    payload = https_server_fct.retrieve_post_data(self)
    if(payload == None):
        return

    # POST state
    if(command == '/post_state_ground'):
        param_edge.state_ground = json.loads(payload)
    elif(command == '/post_state_edge'):
        param_edge.state_edge = json.loads(payload)
    else:
        print("[error] HTTP POST command not known [%s]"% command)

    # POST command
