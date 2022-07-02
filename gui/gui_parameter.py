#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from src import io
from src import lidar
from src import saving
from src import loop

from gui import callback_gui
from gui import gui_runtime

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def build_parameter():
    with dpg.collapsing_header(label="Parameter"):
        with dpg.group(horizontal=True):
            build_option()
            build_device()
    with dpg.collapsing_header(label="Lidar"):
        build_lidar()
    with dpg.collapsing_header(label="File saving"):
        build_saving()

def build_option():
    with dpg.group():
        dpg.add_text("Parameter", color=(125, 125, 125))
        dpg.add_checkbox(tag="wgeo", label="With geolocalization", default_value=parameter.with_geolocalization, callback=callback_gui.callback_parameter);
        dpg.add_checkbox(tag="cwf", label="With Lidar forwarding", default_value=parameter.with_forwarding, callback=callback_gui.callback_parameter);
        dpg.add_checkbox(tag="cwtl", label="With two lidar", default_value=parameter.with_two_lidar, callback=callback_gui.callback_parameter);
        dpg.add_checkbox(tag="cwws", label="With writing on SSD", default_value=parameter.with_writing, callback=callback_gui.callback_parameter);

        dpg.add_text("")
        saving.read_wallet()
        dpg.add_combo(parameter.wallet_add, tag="comboip", label="Adresse", default_value="localhost", width=125, callback=callback_gui.callback_comboip)
        dpg.add_input_text(tag="hubiump", label="Hubium IP", default_value=parameter.hubium_ip, width=125, callback=callback_gui.callback_parameter);
        dpg.add_input_int(tag="hubiumpos", label="Hubium socket port", default_value=parameter.hubium_sock_port, min_value=0, min_clamped=True, width=125, callback=callback_gui.callback_parameter);
        dpg.add_input_int(tag="hubiumpoh", label="Hubium HTTP port", default_value=parameter.hubium_http_port, min_value=0, min_clamped=True, width=125, callback=callback_gui.callback_parameter);

def build_lidar():
    dpg.add_input_int(tag="ls", label="Lidar speed", default_value=parameter.lidar_speed, step=60, min_value=0, max_value=1200, width=100, min_clamped=True, max_clamped=True, callback=callback_gui.callback_parameter);
    dpg.add_input_text(tag="l1ip", label="Lidar 1 IP", default_value=parameter.ip_l1, width=300, callback=callback_gui.callback_parameter);
    dpg.add_input_text(tag="l2ip", label="Lidar 2 IP", default_value=parameter.ip_l2, width=300, callback=callback_gui.callback_parameter);

def build_device():
    with dpg.group():
        with dpg.group(horizontal=True):
            dpg.add_text("Device", color=(125, 125, 125))
            dpg.add_button(label="Refresh", callback=callback_gui.callback_refresh_device)
        with dpg.group(horizontal=True):
            devices = device.get_all_device()
            with dpg.group():
                dpg.add_text("Lidar 1")
                dpg.add_listbox(devices, tag="l1d", callback=callback_gui.callback_choice_device, default_value=parameter.device_l1, width=150, num_items=len(devices))

            with dpg.group():
                dpg.add_text("Lidar 2")
                dpg.add_listbox(devices, tag="l2d", callback=callback_gui.callback_choice_device, default_value=parameter.device_l2, width=150, num_items=len(devices))

def build_saving():
    dpg.add_separator()
    dpg.add_text("Saving", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Capture ID: [")
        dpg.add_text(parameter.capture_ID, color=(31, 140, 250))
        dpg.add_text("]")
    dpg.add_input_text(tag="ssdp", label="Path SSD", default_value=parameter.path_ssd, width=200, callback=callback_gui.callback_path);
    dpg.add_input_text(tag="pnam", label="Path name", default_value=parameter.path_name, width=200, callback=callback_gui.callback_path);
    dpg.add_text(parameter.path_file_l1, tag="l1p", color=(31, 140, 250));
    dpg.add_text(parameter.path_file_l2, tag="l2p", color=(31, 140, 250));
