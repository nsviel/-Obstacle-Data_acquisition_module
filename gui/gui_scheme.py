#! /usr/bin/python
#---------------------------------------------

from gui import scheme_link
from gui import scheme_node
from gui import scheme_color

import dearpygui.dearpygui as dpg



def build_scheme():
    create_scheme()
    init_scheme()

def create_scheme():
    # Node editor parameter
    editeur_height = 360
    color_info = (0, 200, 200)

    # Construct node editor
    with dpg.node_editor(height = editeur_height):
        scheme_node.node_pywardium(color_info)
        scheme_node.node_hubium(color_info)
        scheme_node.node_hardware(color_info)
        scheme_node.node_edge(color_info)
        scheme_node.node_edge_local(color_info)
        scheme_node.node_sncf(color_info)
        scheme_node.node_valeo(color_info)
        scheme_link.create_link()

def init_scheme():
    red = scheme_color.color_red()
    layer_train = scheme_color.color_layer_train()
    layer_edge = scheme_color.color_layer_edge()
    layer_cloud = scheme_color.color_layer_cloud()

    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_hard", layer_train)
    dpg.bind_item_theme("node_hu", layer_edge)
    dpg.bind_item_theme("node_local", layer_edge)
    dpg.bind_item_theme("node_ed", layer_cloud)
    dpg.bind_item_theme("node_sncf", layer_cloud)
    dpg.bind_item_theme("but_fal", red)
