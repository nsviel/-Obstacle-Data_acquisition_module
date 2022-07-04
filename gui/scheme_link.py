#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    dpg.add_node_link("py_sock_port", "hu_sock_port", tag="link_py_hu_sock")
    dpg.add_node_link("py_sock_port", "hu_http_port", tag="link_py_hu_http")
    dpg.add_node_link("py_sock_port", "l1_input", tag="link_py_l1")
    dpg.add_node_link("py_sock_port", "l2_input", tag="link_py_l2")
    dpg.add_node_link("py_sock_port", "ssd_input", tag="link_py_ssd")
    dpg.add_node_link("va_http_port", "hu_http_port", tag="link_va_hu")
    dpg.add_node_link("hu_client", "sncf_mqtt_port", tag="link_hu_sncf")
    dpg.add_node_link("hu_client", "ve_input", tag="link_hu_ve")
    dpg.add_node_link("hu_client", "ed_sock_port", tag="link_hu_ed")
    dpg.add_node_link("hu_client", "ai_input", tag="link_hu_ai")

def update_link_color():
    update_link(parameter.http_connected, "link_py_hu_http")
    update_link(parameter.socket_connected, "link_py_hu_sock")
    update_link(parameter.mqtt_connected, "link_hu_sncf")
    update_link(parameter.ssd_connected, "link_py_ssd")

    #update_link(parameter.hubium_state['velo_connected'], "link_hu_ve")
    #update_link(parameter.hubium_state['vale_connected'], "link_va_hu")
    #update_link(parameter.hubium_state['ia_connectes'], "link_hu_ai")
    #update_link(parameter.hubium_state['edge_conncted'], "link_hu_ed")

def update_link(state, tag):
    if(state):
        green = scheme_color.color_green()
        dpg.bind_item_theme(tag, green)
    else:
        red = scheme_color.color_red()
        dpg.bind_item_theme(tag, red)
