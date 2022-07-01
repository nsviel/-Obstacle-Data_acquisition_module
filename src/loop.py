#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import saving
from src import callback
from src import io
from src import capture

import pcapy

def init():
    saving.determine_path()
    saving.read_wallet()
    #socket.init_socket()
    callback.callback_connection()
    capture.start_l1_capture()
    capture.start_l2_capture()

def loop():
    callback.callback_loop()
