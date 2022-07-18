#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import device

from scapy.all import *

import socket
import pcapy
import time
import sys


def send_packet(packet):
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_port"]
    if(packet != None):
        #Remove network queue data
        packet = packet[42:]

        #Send raw data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet, (ip, port))
