#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import saving
from src import device

import dearpygui.dearpygui as dpg


def callback_parameter():
    parameter.with_two_lidar = dpg.get_value("cwtl")
    parameter.with_writing = dpg.get_value("cwws")
    parameter.with_forwarding = dpg.get_value("cwf")
    parameter.lidar_speed = dpg.get_value("ls")
    parameter.with_geolocalization = dpg.get_value("wgeo")

    parameter.velo_ip = dpg.get_value("veloip")
    parameter.velo_port = dpg.get_value("velopo")

    parameter.lidar_1_dev = dpg.get_value("l1d")
    parameter.lidar_2_dev = dpg.get_value("l2d")

def callback_event():
    parameter.run = dpg.get_value("bclo")

def callback_path():
    parameter.path_ssd = dpg.get_value("ssdp")
    parameter.path_name = dpg.get_value("pnam")
    saving.determine_path()

def callback_device():
    devices = device.get_all_device()
    dpg.set_value("l1d", devices)
    dpg.set_value("l2d", devices)

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(parameter.wallet_add)):
        if(adress == parameter.wallet_add[i]):
            parameter.velo_ip = parameter.wallet_ip[i]
    dpg.set_value("veloip", parameter.velo_ip)
