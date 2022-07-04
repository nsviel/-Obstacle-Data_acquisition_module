#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu
from param import param_li
from src import device
from scapy.all import *

import socket
import pcapy


def test_socket_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(" ", (param_hu.hubium_ip, param_hu.hubium_sock_port))
        param_py.socket_connected = True
    except:
        param_py.socket_connected = False
    #print(param_py.socket_connected)

#Create new client socket
def connection():
    if(param_py.socket_connected):
        param_py.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        param_py.socket_ready = True

def send_packet(packet):
    # Send packet to velodium server
    if(param_py.socket_connected and param_li.with_forwarding and packet != None):
        #Remove network queue data
        packet = packet[42:]

        #Send Pur data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet, (param_hu.hubium_ip, param_hu.hubium_sock_port))
