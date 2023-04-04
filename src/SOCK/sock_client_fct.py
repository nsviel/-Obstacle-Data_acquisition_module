#---------------------------------------------
from src.param import param_capture

import socket


def create_socket():
    param_capture.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_capture.sock_client_ok = True

def send_packet_l1(packet):
    ip = param_capture.state_capture["module_edge"]["ip"]
    port = param_capture.state_capture["module_edge"]["sock_server_l1_port"]
    nb_packet = param_capture.state_capture["lidar_1"]["packet"]["sent"]

    if(packet != None and param_capture.sock_client_ok):
        param_capture.sock_client.sendto(packet, (ip, port))
        param_capture.state_capture["lidar_1"]["packet"]["sent"] = nb_packet + 1

def send_packet_l2(packet):
    ip = param_capture.state_capture["module_edge"]["ip"]
    port = param_capture.state_capture["module_edge"]["sock_server_l2_port"]
    nb_packet = param_capture.state_capture["lidar_2"]["packet"]["sent"]

    if(packet != None and param_capture.sock_client_ok):
        param_capture.sock_client.sendto(packet, (ip, port))
        param_capture.state_capture["lidar_2"]["packet"]["sent"] = nb_packet + 1
