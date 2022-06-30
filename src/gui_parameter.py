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


def build_parameter():
    with dpg.group(horizontal=True):
        build_option()
        build_device()
    build_saving()

def build_option():
    with dpg.group():
        dpg.add_text("Parameter", color=(125, 125, 125))
        dpg.add_checkbox(tag="wgeo", label="With geolocalization", default_value=parameter.with_geolocalization, callback=callback.callback_parameter);
        dpg.add_checkbox(tag="cwf", label="With LiDAR forwarding", default_value=parameter.with_forwarding, callback=callback.callback_parameter);
        dpg.add_checkbox(tag="cwtl", label="With two lidar", default_value=parameter.with_two_lidar, callback=callback.callback_parameter);
        dpg.add_checkbox(tag="cwws", label="With writing on SSD", default_value=parameter.with_writing, callback=callback.callback_parameter);

        dpg.add_text("")
        dpg.add_input_int(tag="ls", label="Lidar speed", default_value=parameter.lidar_speed, step=60, min_value=0, max_value=1200, width=100, min_clamped=True, max_clamped=True, callback=callback.callback_parameter);

        dpg.add_text("")
        saving.read_wallet()
        dpg.add_combo(parameter.wallet_add, tag="comboip", label="Adresse", default_value="localhost", width=125, callback=callback.callback_comboip)
        dpg.add_input_text(tag="veloip", label="Velodium IP", default_value=parameter.velo_ip, width=125, callback=callback.callback_parameter);
        dpg.add_input_int(tag="velopo", label="Velodium port", default_value=parameter.velo_port, min_value=0, min_clamped=True, width=125, callback=callback.callback_parameter);

def build_device():
    with dpg.group():
        dpg.add_text("Device", color=(125, 125, 125))
        with dpg.group(horizontal=True):
            devices = device.get_all_device()
            with dpg.group():
                dpg.add_text("LiDAR 1")
                dpg.add_listbox(devices, tag="l1d", callback=callback.callback_parameter, default_value=parameter.lidar_1_dev, width=150, num_items=len(devices))

            with dpg.group():
                dpg.add_text("LiDAR 2")
                dpg.add_listbox(devices, tag="l2d", callback=callback.callback_parameter, default_value=parameter.lidar_2_dev, width=150, num_items=len(devices))
        dpg.add_button(label="Refresh", callback=callback.callback_device)

def build_saving():
    dpg.add_separator()
    dpg.add_text("Saving", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Capture ID: [")
        dpg.add_text(parameter.capture_ID, color=(31, 140, 250))
        dpg.add_text("]")
    dpg.add_input_text(tag="ssdp", label="Path SSD", default_value=parameter.path_ssd, width=200, callback=callback.callback_path);
    dpg.add_input_text(tag="pnam", label="Path name", default_value=parameter.path_name, width=200, callback=callback.callback_path);
    dpg.add_text(parameter.path_file_l1, tag="l1p", color=(31, 140, 250));
    dpg.add_text(parameter.path_file_l2, tag="l2p", color=(31, 140, 250));
