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
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.bind(("127.0.0.1", param_py.socket_listen))
    sock_server.settimeout(0.1)
    try:
        print("----")
        sock_client.sendto(str.encode("test"), (param_hu.hubium_ip, param_hu.hubium_sock_port))
        print("hello")
        data, (address, port) = sock_server.recvfrom(4096)
        print("hello")
        msg = data.decode('utf-8')
        print(msg)
        if(msg == "ok"):
            param_py.socket_connected = True
    except:
        param_py.socket_connected = False

def connection():
    if(param_py.socket_connected):
        param_py.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        param_py.socket_ready = True

def send_packet(packet):
    # Send packet to velodium server
    if(param_py.socket_connected and packet != None):
        #Remove network queue data
        packet = packet[42:]

        #Send Pur data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet, (param_hu.hubium_ip, param_hu.hubium_sock_port))
