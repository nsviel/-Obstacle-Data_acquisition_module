#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import gui_scheme

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1nbpck", parameter.nb_packet_l1)
    dpg.set_value("l2nbpck", parameter.nb_packet_l2)
