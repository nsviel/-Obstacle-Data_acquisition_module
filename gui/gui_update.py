#! /usr/bin/python
#---------------------------------------------

from param import param_py

import dearpygui.dearpygui as dpg


def update_ssd_info():
    dpg.set_value("ssd_total", param_py.ssd_space_total)
    dpg.set_value("ssd_used", param_py.ssd_space_used)
