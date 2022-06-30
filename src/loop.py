#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import saving


def init():
    saving.determine_path()
    saving.read_wallet()
    socket.init_socket()

def loop():
    loop_lidar_1()
    loop_lidar_2()

def loop_lidar_1():
    if(parameter.socket_ready):
        #-------------

        #Receive packet
        (header, packet) = parameter.listener_l1.next()
        parameter.nb_packet_l1 += 1

        #write packet
        if(parameter.with_writing and parameter.ssd_connected):
            wrpcap(parameter.path_file_l1, packet, append=True)

        # Send packet to velodium server
        if(parameter.with_forwarding):
            #Remove network queue data
            packet = packet[42:]

            #Send Pur data
            parameter.socket_out.sendto(packet, (parameter.velo_ip, parameter.velo_port))

        #-------------

def loop_lidar_2():
    if(parameter.socket_ready and parameter.with_two_lidar):
        #-------------

        #Receive packet
        (header, packet) = parameter.listener_l2.next()
        parameter.nb_packet_l2 += 1

        #write packet
        if(parameter.with_writing and parameter.ssd_connected):
            wrpcap(parameter.path_file_l2, packet, append=True)

        #-------------
