#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg


def color_red():
    red = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=red):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (255, 20, 20), category=dpg.mvThemeCat_Nodes)
    return red

def color_green():
    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (20, 255, 20), category=dpg.mvThemeCat_Nodes)
    return green
    
def color_layer_train():
    layer_train = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_train):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (20, 82, 175), category=dpg.mvThemeCat_Nodes)
    return layer_train

def color_layer_edge():
    layer_edge = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_edge):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (45, 108, 143), category=dpg.mvThemeCat_Nodes)
    return layer_edge

def color_layer_cloud():
    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (106, 106, 105), category=dpg.mvThemeCat_Nodes)
    return layer_cloud
