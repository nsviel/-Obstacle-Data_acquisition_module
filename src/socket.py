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

def init_socket():
    #Socket stuff
    l1_dev = device.check_if_device_exists(parameter.lidar_1_dev)
    l2_dev = device.check_if_device_exists(parameter.lidar_1_dev)

    #- device name, max_bytes, promiscuous, read_timeout
    if(l1_dev and l2_dev):
        parameter.listener_l1 = pcapy.open_live(parameter.lidar_1_dev , 1248 , 1 , 0)
        parameter.listener_l2 = pcapy.open_live(parameter.lidar_2_dev , 1248 , 1 , 0)
        parameter.socket_out = socket.create_socket_udp()
        parameter.socket_ready = True

def send_packet(packet):
    # Send packet to velodium server
    if(parameter.with_forwarding):
        #Remove network queue data
        packet = packet[42:]

        #Send Pur data
        parameter.socket_out.sendto(packet, (parameter.hubium_ip, parameter.hubium_sock_port))
