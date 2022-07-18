#! /usr/bin/python
#---------------------------------------------

from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet(packet):
    sock_client_fct.send_packet(packet)
