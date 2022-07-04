#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import http
from src import http_get
from src import saving

from gui import scheme_link

from threading import Thread

import time


def thread_test_connection():
    while parameter.thread_con:
        http.test_connection()
        socket.test_socket_connection()
        http_get.get_is_mqtt_connected()
        saving.test_is_ssd()

        scheme_link.update_link_color()
        time.sleep(1)
        pass

def start_thread_test_conn():
    parameter.thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_thread():
    parameter.thread_con = False

def parse_state_json():
    parameter.mqtt_connected = parameter.hubium_state["mqtt"]["connected"]
    parameter.velo_connected = parameter.hubium_state["velodium"]["connected"]
    parameter.vale_connected = parameter.hubium_state["valeo"]["connected"]
    parameter.edge_connected = parameter.hubium_state["edge"]["connected"]
    parameter.ia_connected = parameter.hubium_state["ai"]["connected"]
