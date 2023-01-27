#---------------------------------------------
from param import param_py

import socket


def create_socket():
    param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_py.sock_client_ok = True

def send_packet_l1(packet):
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_l1_port"]
    nb_packet = param_py.state_py["lidar_1"]["packet"]["sent"]

    if(packet != None and param_py.sock_client_ok):
        param_py.sock_client.sendto(packet, (ip, port))
        param_py.state_py["lidar_1"]["packet"]["sent"] = nb_packet + 1

def send_packet_l2(packet):
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_l2_port"]
    nb_packet = param_py.state_py["lidar_2"]["packet"]["sent"]

    if(packet != None and param_py.sock_client_ok):
        param_py.sock_client.sendto(packet, (ip, port))
        param_py.state_py["lidar_2"]["packet"]["sent"] = nb_packet + 1
