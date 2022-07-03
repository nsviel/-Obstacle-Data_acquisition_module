#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import gui_scheme

import dearpygui.dearpygui as dpg


def loop():
    loop_scheme()
    loop_packet()

def loop_packet():
    dpg.set_value("l1nbpck", parameter.nb_packet_l1)
    dpg.set_value("l2nbpck", parameter.nb_packet_l2)

def loop_scheme():
    gui_scheme.update_link(parameter.http_connected, "link_py_hu_http")
    gui_scheme.update_link(parameter.socket_connected, "link_py_hu_sock")
