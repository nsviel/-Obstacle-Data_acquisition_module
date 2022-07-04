#! /usr/bin/python
#---------------------------------------------

from src import saving
from src import connection
from src import capture


def init():
    saving.determine_path()
    saving.read_wallet()

    connection.start_thread_test_conn()

    capture.start_l1_capture()
    capture.start_l2_capture()

def loop():
    a=1#connection.test_connection()
