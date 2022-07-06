#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu

from gui import scheme_link

import dearpygui.dearpygui as dpg


def update_gui():
    scheme_link.update_link_color()
    update_ssd_info()
    update_status()

def update_ssd_info():
    dpg.set_value("ssd_total", param_py.ssd_space_total)
    dpg.set_value("ssd_used", param_py.ssd_space_used)

def update_status():
    dpg.set_value("py_status", param_py.status)
    dpg.set_value("hu_status", param_hu.hubium_status)
