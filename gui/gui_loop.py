#! /usr/bin/python
#---------------------------------------------

from param import param_li

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1_packet", param_li.nb_packet_l1)
    dpg.set_value("l2_packet", param_li.nb_packet_l2)
