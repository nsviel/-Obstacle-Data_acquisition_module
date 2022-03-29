#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from src import fct_device
from src import fct_socket
from src import fct_display

import threading
import pcapy
import sys
import time

from scapy.all import *



#Main program loop
def lidar_loop():
    #-------------

    # Build lidar thread
    lidar_1 = loop_lidar_1()
    if(fct_param.with_two_lidar):
        lidar_2 = loop_lidar_2()

    # Display package captured
    while(fct_param.run):
        #Display number of captured packets
        fct_display.loop_nb_packet();

    # Join lidar thread
    lidar_1.join()
    if(fct_param.with_two_lidar):
        lidar_2.join()

    #-------------


def loop_lidar_1():
    #-------------

    #Create thread
    lidar_1 = threading.Thread(target=lidar_1_thread)

    #Start thread
    print("[\033[92mLID\033[0m] Start lidar 1 loop")
    lidar_1.start()

    return lidar_1
    #-------------

def loop_lidar_2():
    #-------------

    #Create thread
    lidar_2 = threading.Thread(target=lidar_2_thread)

    #Start thread
    print("[\033[92mLID\033[0m] Start lidar 2 loop")
    lidar_2.start()

    return lidar_2
    #-------------

def lidar_1_thread():
    #-------------

    #Socket stuff
    #- device name, max_bytes, promiscuous, read_timeout
    capture = pcapy.open_live(fct_param.lidar_1_dev , 1300 , 1 , 0)
    client_sock = fct_socket.create_client_socket()

    #Main lidar loop
    start = time.time()
    while(fct_param.run):
        #Receive packet
        (header, packet) = capture.next()
        fct_param.lidar_1_nb_packet += 1

        #write packet
        if(fct_param.with_writing and fct_param.ssd_connected):
            wrpcap(fct_param.path_lidar_1, packet, append=True)

        # Send packet to velodium server
        if(fct_param.with_forwarding):
            #Remove network queue data
            packet = packet[42:]

            #Send Pur data
            client_sock.sendto(packet, (fct_param.velo_IP, fct_param.velo_port))

    end = time.time()
    fct_param.duration = end - start

    #-------------

def lidar_2_thread():
    #-------------

    #Socket stuff
    #- device name, max_bytes, promiscuous, read_timeout
    capture = pcapy.open_live(fct_param.lidar_2_dev, 1300 , 1 , 0)
    client_sock = fct_socket.create_client_socket()

    while(fct_param.run):
        #Receive packet
        (header, packet) = capture.next()
        fct_param.lidar_2_nb_packet += 1

        #write packet
        if(fct_param.with_writing and fct_param.ssd_connected):
            wrpcap(fct_param.path_lidar_2, packet, append=True)

    #-------------
