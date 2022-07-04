#! /usr/bin/python
#---------------------------------------------

from src import param_li
from src import device
from src import socket
from src import io

from threading import Thread

import pcapy


def start_lidar_capture():
    thread_l1 = Thread(target = start_l1_capture)
    thread_l2 = Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    param_li.run_thread_l1 = False
    param_li.run_thread_l2 = False

def start_l1_capture():
    if(device.check_if_device_exists(param_li.device_l1)):
        param_li.nb_packet_l1 = 0
        listener = pcapy.open_live(param_li.device_l1 , 1248 , 1 , 0)
        param_li.run_thread_l1 = True

        while param_li.run_thread_l1:
            (header, packet) = listener.next()
            if(len(packet) == 1248):
                io.write_lidar_data(param_li.path_file_l1, packet)
                socket.send_packet(packet)
                param_li.nb_packet_l1 += 1
            pass

def start_l2_capture():
    if(device.check_if_device_exists(param_li.device_l2)):
        param_li.nb_packet_l2 = 0
        listener = pcapy.open_live(param_li.device_l2 , 1248 , 1 , 0)
        param_li.run_thread_l2 = True

        while param_li.run_thread_l2:
            (header, packet) = listener.next()
            if(len(packet) == 1248):
                io.write_lidar_data(param_li.path_file_l2, packet)
                param_li.nb_packet_l2 += 1
            pass
