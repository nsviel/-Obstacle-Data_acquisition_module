#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import http
from src import http_get

from threading import Thread

import time


def test_connection():
    while parameter.thread_con:
        http.test_connection()
        socket.test_socket_connection()
        http_get.get_is_mqtt_connected()
        time.sleep(1)
        pass

def start_thread_test_conn():
    parameter.thread_con = True
    thread_con = Thread(target = test_connection)
    thread_con.start()

def stop_thread():
    parameter.thread_con = False

def parse_state_json():
    parameter.mqtt_connected = parameter.hubium_state['mqtt_connected']
