#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import http_get


def callback_false_alarm():
    http_get.get_falsealarm()
