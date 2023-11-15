#---------------------------------------------
# Possible POST command:
# - /post_state_ground
# - /post_state_edge
# - /post_command_lidar_1
#       - start
#       - stop
# - /post_command_lidar_2
#       - start
#       - stop
#---------------------------------------------

from src.param import param_capture
from src.connection.HTTPS.server import https_server_fct
from src.utils import parser_json
from src.interface import command
from src.utils import terminal
from src.interface import capture
from src.interface import lidar
import json


def manage_post(self):
    command = str(self.path)
    payload = https_server_fct.retrieve_post_data(self)
    if(payload == None):
        return

    # POST state
    if(command == '/post_state_ground'):
        param_capture.state_ground = json.loads(payload)
    elif(command == '/post_state_edge'):
        param_capture.state_edge = json.loads(payload)

    # POST command
    elif(command == '/post_command_ground'):
        if(payload == "reset"):
            capture.restart_lidar_capture()
    elif(command == '/post_command_lidar_1'):
        if(payload == "start"):
            lidar.start_l1_motor()
        elif(payload == "stop"):
            lidar.stop_l1_motor()
    elif(command == '/post_command_lidar_2'):
        if(payload == "start"):
            lidar.start_l2_motor()
        elif(payload == "stop"):
            lidar.stop_l2_motor()
    else:
        print("[error] HTTP POST command not known [%s]"% command)
