#! /usr/bin/python
#---------------------------------------------

from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet_l1(packet):
    sock_client_fct.send_packet_l1(packet)

def send_packet_l2(packet):
    sock_client_fct.send_packet_l2(packet)
