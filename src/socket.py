#! /usr/bin/python
#---------------------------------------------

import socket


#Create new client socket
def create_socket_udp():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
