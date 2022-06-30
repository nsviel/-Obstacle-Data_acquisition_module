#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import callback

import dearpygui.dearpygui as dpg


def build_connection():
    dpg.add_separator()
    dpg.add_text("Connection", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Hubium HTTP: [")
        dpg.add_text("OFF", tag="httpconn", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Hubium socket: [")
        dpg.add_text("OFF", tag="socketconn", color=(31, 140, 250))
        dpg.add_text("]")
    dpg.add_button(label="Refresh", callback=callback.callback_connection)
