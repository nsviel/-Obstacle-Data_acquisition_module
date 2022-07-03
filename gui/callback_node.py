#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import http


def callback_false_alarm():
    http.send_false_alarm
