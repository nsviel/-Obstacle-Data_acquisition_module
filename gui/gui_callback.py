#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu
from param import param_li
from src import saving
from src import device
from src import socket
from src import http
from src import socket
from src import capture

import dearpygui.dearpygui as dpg


def callback_parameter():
    param_li.with_two_lidar = dpg.get_value("cwtl")
    param_li.with_writing = dpg.get_value("cwws")
    param_li.with_forwarding = dpg.get_value("cwf")
    param_li.lidar_speed = dpg.get_value("ls")
    param_py.with_geolocalization = dpg.get_value("wgeo")

    param_hu.hubium_ip = dpg.get_value("hubiump")
    param_hu.hubium_sock_port = dpg.get_value("hubiumpos")
    param_hu.hubium_httpd_port = dpg.get_value("hubiumpoh")

    param_li.ip_l1 = dpg.get_value("l1ip")
    param_li.ip_l2 = dpg.get_value("l2ip")

def callback_connection():
    http.test_connection()
    socket.test_socket_connection()
    if(param_py.http_connected):
        dpg.set_value("httpconn", "ON")
    else:
        dpg.set_value("httpconn", "OFF")
    if(param_py.socket_connected):
        dpg.set_value("socketconn", "ON")
    else:
        dpg.set_value("socketconn", "OFF")

def callback_close():
    param_py.run_loop = dpg.get_value("bclo")

def callback_path():
    param_py.ssd_path = dpg.get_value("ssdp")
    param_li.path_name = dpg.get_value("pnam")
    saving.determine_path()

def callback_choice_device():
    param_li.device_l1 = str(dpg.get_value("l1d"))
    param_li.device_l2 = str(dpg.get_value("l2d"))
    capture.stop_lidar_capture()
    capture.start_lidar_capture()

def callback_refresh_device():
    devices = device.get_all_device()
    dpg.set_value("l1d", devices)
    dpg.set_value("l2d", devices)

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.hubium_ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.hubium_ip)
