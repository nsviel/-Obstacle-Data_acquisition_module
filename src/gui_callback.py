#! /usr/bin/python
#---------------------------------------------

from src import parameter

import dearpygui.dearpygui as dpg


def callback_parameter():
    parameter.with_two_lidar = dpg.get_value("cwtl")
    parameter.with_writing = dpg.get_value("cwws")
    parameter.with_forwarding = dpg.get_value("cwf")
    parameter.lidar_speed = dpg.get_value("ls")
    parameter.path_ssd = dpg.get_value("ssdp")
    parameter.with_geolocalization = dpg.get_value("wgeo")

    parameter.velo_ip = dpg.get_value("veloip")
    parameter.velo_port = dpg.get_value("velopo")

    parameter.lidar_1_dev = dpg.get_value("l1d")
    parameter.lidar_2_dev = dpg.get_value("l2d")

def callback_event():
    parameter.run = dpg.get_value("bclo")
