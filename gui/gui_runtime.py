#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_li
from src import io
from src import lidar

import dearpygui.dearpygui as dpg


def build_runtime():
    with dpg.collapsing_header(label="Stats"):
        build_stat()

def build_stat():
    dpg.add_separator()
    dpg.add_text("Statistics", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Capture time: [")
        dpg.add_text(param_li.time_capture, color=(31, 140, 250))
        dpg.add_text("]")

    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 1 - Size of capture file: [")
        dpg.add_text(io.get_size_Gb(param_li.path_file_l1), color=(31, 140, 250))
        dpg.add_text("]")

    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 2 - Size of capture file: [")
        dpg.add_text(io.get_size_Gb(param_li.path_file_l2), color=(31, 140, 250))
        dpg.add_text("]")
