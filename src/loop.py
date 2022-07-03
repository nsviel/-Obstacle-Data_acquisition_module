#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import saving
from src import connection
from src import capture

from gui import gui

import pcapy

def init():
    saving.determine_path()
    saving.read_wallet()
    connection.test_connection()
    capture.start_l1_capture()
    capture.start_l2_capture()

def loop():
    connection.test_connection()
