#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import saving
from src import callback


def init():
    saving.determine_path()
    saving.read_wallet()
    socket.init_socket()
    callback.callback_connection()

def loop():
    loop_lidar_1()
    loop_lidar_2()

def loop_lidar_1():
    if(parameter.socket_ready):
        #-------------

        (header, packet) = parameter.listener_l1.next()
        io.write_lidar_data(parameter.path_file_l1)
        socket.send_packet(packet)
        parameter.nb_packet_l1 += 1

        #-------------

def loop_lidar_2():
    if(parameter.socket_ready and parameter.with_two_lidar):
        #-------------

        #Receive packet
        (header, packet) = parameter.listener_l2.next()
        io.write_lidar_data(parameter.path_file_l2)
        parameter.nb_packet_l2 += 1

        #-------------
