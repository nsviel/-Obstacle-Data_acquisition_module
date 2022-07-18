#! /usr/bin/python
#---------------------------------------------

from param import param_py

import socket


def create_socket():
    param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_py.sock_client_ok = True

def send_packet(packet):
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_port"]
    if(packet != None and param_py.sock_client_ok):
        #Remove network queue data
        packet = packet[42:]

        #Send raw data
        param_py.sock_client.sendto(packet, (ip, port))
