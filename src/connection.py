#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import socket
from src import http


def test_connection():
    http.test_connection()
    socket.test_socket_connection()
