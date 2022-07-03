#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from scapy.all import *

import socket
import pcapy


#Create new client socket
def create_socket_udp():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def test_socket_connection():
    try:
        parameter.socket_out.send("some more data")
        parameter.socket_connected = True
    except:
        parameter.socket_connected = False

def init_socket():
    parameter.socket_out = create_socket_udp()
    parameter.socket_ready = True

def send_packet(packet):
    # Send packet to velodium server
    if(parameter.with_forwarding and packet != None):
        #Remove network queue data
        packet = packet[42:]

        #Send Pur data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet, (parameter.hubium_ip, parameter.hubium_sock_port))
