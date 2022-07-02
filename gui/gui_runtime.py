#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io
from src import lidar
from src import http

import dearpygui.dearpygui as dpg


def build_runtime():
    with dpg.collapsing_header(label="Runtime"):
        build_connection()
    with dpg.collapsing_header(label="Stats"):
        build_stat()

def build_connection():
    dpg.add_separator()
    dpg.add_text("Runtime", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        with dpg.group():
            build_geolocalization()
            build_lidar_1()
            build_lidar_2()
        dpg.add_button(label="False alarm", indent=300, callback=http.send_false_alarm)

def build_geolocalization():
    with dpg.group(horizontal=True):
        dpg.add_text("Country: [")
        dpg.add_text(parameter.geo_country, color=(31, 140, 250))
        dpg.add_text("]")

def build_lidar_1():
    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 1 -")
        with dpg.group(horizontal=True):
            dpg.add_text("packet captured: [")
            dpg.add_text(parameter.nb_packet_l1, tag="l1nbpck", color=(31, 140, 250))
            dpg.add_text("]")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start", tag="l1dstart", callback=lidar.start_l1_motor)
            dpg.add_button(label="Stop", tag="l1dstop", callback=lidar.stop_l1_motor)

def build_lidar_2():
    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 2 -")
        with dpg.group(horizontal=True):
            dpg.add_text("packet captured: [")
            dpg.add_text(parameter.nb_packet_l2, tag="l2nbpck", color=(31, 140, 250))
            dpg.add_text("]")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start", tag="l2dstart", callback=lidar.start_l2_motor)
            dpg.add_button(label="Stop", tag="l2dstop", callback=lidar.stop_l2_motor)

def build_stat():
    dpg.add_separator()
    dpg.add_text("Statistics", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Capture time: [")
        dpg.add_text(parameter.time_capture, color=(31, 140, 250))
        dpg.add_text("]")

    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 1 - Size of capture file: [")
        dpg.add_text(io.get_size_Gb(parameter.path_file_l1), color=(31, 140, 250))
        dpg.add_text("]")

    with dpg.group(horizontal=True):
        dpg.add_text("LiDAR 2 - Size of capture file: [")
        dpg.add_text(io.get_size_Gb(parameter.path_file_l2), color=(31, 140, 250))
        dpg.add_text("]")
