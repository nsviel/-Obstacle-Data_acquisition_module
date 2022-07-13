#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import device

from scapy.all import *

import socket
import pcapy


def test_connection():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.bind(("127.0.0.1", param_py.socket_server))
    sock_server.settimeout(0.1)
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_port"]
    try:
        sock_client.sendto(str.encode("test"), (ip, sock_server_port))
        data, (address, port) = sock_server.recvfrom(4096)
        msg = data.decode('utf-8')
        if(msg == "ok"):
            param_py.state_py["self"]["sock_connected"] = True
    except:
        param_py.state_py["self"]["sock_connected"] = False

def connection():
    connected = param_py.state_py["self"]["sock_connected"]
    if(connected):
        param_py.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_packet(packet):
    connected = param_py.state_py["self"]["sock_connected"]
    ip = param_py.state_py["hubium"]["ip"]
    port = param_py.state_py["hubium"]["sock_server_port"]
    if(connected and packet != None):
        #Remove network queue data
        packet = packet[42:]

        #Send raw data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(packet, (ip, port))
