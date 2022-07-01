#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from src import socket
from src import io

from threading import Thread

import pcapy


def start_lidar_capture():
    parameter.thread_l1 = Thread(target = start_l1_capture)
    parameter.thread_l2 = Thread(target = start_l2_capture)
    parameter.thread_l1.start()
    parameter.thread_l2.start()

def stop_lidar_capture():
    parameter.run_thread_l1 = False
    parameter.run_thread_l2 = False

def start_l1_capture():
    if(device.check_if_device_exists(parameter.device_l1)):
        parameter.nb_packet_l1 = 0
        listener = pcapy.open_live(parameter.device_l1 , 1248 , 1 , 0)
        parameter.run_thread_l1 = True

        while parameter.run_thread_l1:
            (header, packet) = listener.next()
            if(len(packet) == 1248):
                io.write_lidar_data(parameter.path_file_l1, packet)
                socket.send_packet(packet)
                parameter.nb_packet_l1 += 1
            pass

def start_l2_capture():
    if(device.check_if_device_exists(parameter.device_l2)):
        parameter.nb_packet_l2 = 0
        listener = pcapy.open_live(parameter.device_l2 , 1248 , 1 , 0)
        parameter.run_thread_l2 = True

        while parameter.run_thread_l2:
            (header, packet) = listener.next()
            if(len(packet) == 1248):
                io.write_lidar_data(parameter.path_file_l2, packet)
                parameter.nb_packet_l2 += 1
            pass
