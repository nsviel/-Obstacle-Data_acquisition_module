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
    update_port()

def update_ssd_info():
    dpg.set_value("ssd_total", param_py.ssd_space_total)
    dpg.set_value("ssd_used", param_py.ssd_space_used)

def update_status():
    dpg.set_value("py_status", param_py.status)
    dpg.set_value("hu_status", param_hu.hubium_status)

def update_port():
    dpg.set_value("va_port", param_hu.vale_port)
    dpg.set_value("ve_port", param_hu.velo_port)
    dpg.set_value("hu_sock_port_val", param_hu.hubium_sock_port)
    dpg.set_value("hu_http_port_val", param_hu.hubium_httpd_port)
    dpg.set_value("ed_port", param_hu.edge_port)
    dpg.set_value("sncf_port", param_hu.mqtt_port)
    dpg.set_value("py_port_sock_val", param_py.socket_listen)
