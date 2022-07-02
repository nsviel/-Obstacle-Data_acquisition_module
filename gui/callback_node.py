#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import http


def callback_false_alarm():
    http.send_false_alarm

def callback_link():


    if(parameter.socket_connected):
        dpg.bind_item_theme("link_py_hu_sock", green)
    else:
        dpg.bind_item_theme("link_py_hu_sock", red)

    colorize_link(parameter.socket_connected, "link_py_hu_sock")
    dpg.bind_item_theme("link_hu_sncf", red)
    dpg.bind_item_theme("link_hu_ve", red)
    dpg.bind_item_theme("link_hu_ed", red)

def colorize_link(state, tag):
    red = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=red):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (255, 20, 20), category=dpg.mvThemeCat_Nodes)

    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (20, 255, 20), category=dpg.mvThemeCat_Nodes)
        
    if(state):
        dpg.bind_item_theme(tag, green)
    else:
        dpg.bind_item_theme(tag, red)
