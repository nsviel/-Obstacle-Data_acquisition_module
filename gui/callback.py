#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import saving
from src import device
from src import socket
from src import http
from src import socket
from src import capture

from gui import gui_state

import dearpygui.dearpygui as dpg


def callback_parameter():
    parameter.with_two_lidar = dpg.get_value("cwtl")
    parameter.with_writing = dpg.get_value("cwws")
    parameter.with_forwarding = dpg.get_value("cwf")
    parameter.lidar_speed = dpg.get_value("ls")
    parameter.with_geolocalization = dpg.get_value("wgeo")

    parameter.hubium_ip = dpg.get_value("hubiump")
    parameter.hubium_sock_port = dpg.get_value("hubiumpos")
    parameter.hubium_http_port = dpg.get_value("hubiumpoh")

    parameter.ip_l1 = dpg.get_value("l1ip")
    parameter.ip_l2 = dpg.get_value("l2ip")

def callback_connection():
    http.test_connection()
    socket.test_socket_connection()
    if(parameter.http_connected):
        dpg.set_value("httpconn", "ON")
    else:
        dpg.set_value("httpconn", "OFF")
    if(parameter.socket_connected):
        dpg.set_value("socketconn", "ON")
    else:
        dpg.set_value("socketconn", "OFF")

def callback_event():
    parameter.run = dpg.get_value("bclo")

def callback_path():
    parameter.path_ssd = dpg.get_value("ssdp")
    parameter.path_name = dpg.get_value("pnam")
    saving.determine_path()

def callback_choice_device():
    parameter.device_l1 = str(dpg.get_value("l1d"))
    capture.stop_lidar_capture()
    capture.start_lidar_capture()

def callback_refresh_device():
    devices = device.get_all_device()
    dpg.set_value("l1d", devices)
    dpg.set_value("l2d", devices)

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(parameter.wallet_add)):
        if(adress == parameter.wallet_add[i]):
            parameter.hubium_ip = parameter.wallet_ip[i]
    dpg.set_value("hubiump", parameter.hubium_ip)

def callback_button():
    dpg.configure_item("layer2", color=(255,0,0))
