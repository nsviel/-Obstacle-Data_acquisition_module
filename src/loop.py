#! /usr/bin/python
#---------------------------------------------

from src import saving
from src import connection
from src import capture
from src import socket


def init():
    saving.determine_path()
    saving.read_wallet()
    connection.start_thread_test_conn()
    socket.connection()

def loop():
    a=1#connection.test_connection()
