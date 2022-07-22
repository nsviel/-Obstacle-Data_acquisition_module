#! /usr/bin/python
#---------------------------------------------

from param import param_py

import socket


def create_socket():
    param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_py.sock_client_ok = True

def send_packet(packet):
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_l1_port"]
    if(packet != None and param_py.sock_client_ok):
        param_py.sock_client.sendto(packet, (ip, port))
