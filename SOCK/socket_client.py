#! /usr/bin/python
#---------------------------------------------

from param import param_py
from SOCK import socket_client_fct
from src import device

from scapy.all import *

import socket
import pcapy
import time


def connection():
    param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_packet(packet):
    socket_client_fct.send_packet(packet)
