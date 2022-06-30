#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from src import callback
from src import io
from src import lidar
from src import saving
from src import loop
from src import gui_runtime

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


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
