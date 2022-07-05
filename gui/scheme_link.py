#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu
from param import param_li

from gui import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    dpg.add_node_link("py_client", "hu_sock_port", tag="link_py_hu_sock")
    dpg.add_node_link("py_client", "hu_httpd_port", tag="link_py_hu_http")
    dpg.add_node_link("py_client", "ssd_input", tag="link_py_ssd")
    dpg.add_node_link("py_server", "l1_input", tag="link_py_l1")
    dpg.add_node_link("py_server", "l2_input", tag="link_py_l2")
    dpg.add_node_link("py_server", "geo_input", tag="link_py_geo")

    dpg.add_node_link("hu_client", "sncf_mqtt_port", tag="link_hu_sncf")
    dpg.add_node_link("hu_client", "ed_server", tag="link_hu_ed")
    dpg.add_node_link("hu_server", "ed_client", tag="link_ed_hu")
    dpg.add_node_link("hu_stockage", "ve_input", tag="link_hu_ve")
    dpg.add_node_link("hu_stockage", "ai_input", tag="link_hu_ai")

    dpg.add_node_link("va_httpd_port", "hu_httpd_port", tag="link_va_hu")

def update_link_color():
    # Pywardium connections
    update_link(param_py.http_connected, "link_py_hu_http")
    update_link(param_py.socket_connected, "link_py_hu_sock")
    update_link(param_py.ssd_connected, "link_py_ssd")
    update_link(param_li.l1_connected, "link_py_l1")
    update_link(param_li.l2_connected, "link_py_l2")

    # Hubium connections
    update_link(param_hu.mqtt_connected, "link_hu_sncf")


    #update_link(param_hu.hubium_json['velo_connected'], "link_hu_ve")
    #update_link(param_hu.hubium_json['vale_connected'], "link_va_hu")
    #update_link(param_hu.hubium_json['ia_connectes'], "link_hu_ai")
    #update_link(param_hu.hubium_json['edge_conncted'], "link_hu_ed")

def update_link(state, tag):
    if(state):
        green = scheme_color.color_green()
        dpg.bind_item_theme(tag, green)
    else:
        red = scheme_color.color_red()
        dpg.bind_item_theme(tag, red)
