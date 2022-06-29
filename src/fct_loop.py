#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from src import fct_device
from src import fct_socket
from src import fct_display
from src import fct_http
from src import fct_coordinate

import threading
import pcapy
import sys
import time

from scapy.all import *



#Main program loop
def lidar_loop():
    #-------------

    #Socket stuff
    #- device name, max_bytes, promiscuous, read_timeout
    lidar_1_capture = pcapy.open_live(fct_param.lidar_1_dev , 1248 , 1 , 0)
    lidar_2_capture = pcapy.open_live(fct_param.lidar_2_dev , 1248 , 1 , 0)
    sock_out = fct_socket.create_client_socket()

    # Display package captured
    start = time.time()
    print("[\033[92mLID\033[0m] Start lidar loop")
    while(fct_param.run):
        #Ask for geolocalization
        if(fct_param.with_geolocalization):
            fct_http.geo_request()
            fct_coordinate.check_position()

        #LiDAR 1 loop
        lidar_1 = loop_lidar_1(lidar_1_capture, sock_out)

        #LiDAR 2 loop
        if(fct_param.with_two_lidar):
            lidar_2 = loop_lidar_2(lidar_2_capture)

        #Display number of captured packets
        fct_display.loop_nb_packet();

    #End loop
    end = time.time()
    fct_param.duration = end - start

    #-------------


def loop_lidar_1(capture, sock):
    #-------------

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
        sock.sendto(packet, (fct_param.velo_ip, fct_param.velo_port))

    #-------------

def loop_lidar_2(capture):
    #-------------

    #Receive packet
    (header, packet) = capture.next()
    fct_param.lidar_2_nb_packet += 1

    #write packet
    if(fct_param.with_writing and fct_param.ssd_connected):
        wrpcap(fct_param.path_lidar_2, packet, append=True)

    #-------------
