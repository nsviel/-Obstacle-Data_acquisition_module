#! /usr/bin/python
#---------------------------------------------

from param import param_py
from SOCK import socket_client_fct
from src import device

from scapy.all import *

import socket
import pcapy
import time


def test_connection():
    socket_client_fct.test_connection()

def connection():
    connected = param_py.state_py["self"]["sock_connected"]
    if(connected):
        param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_packet(packet):
    socket_client_fct.send_packet(packet)
