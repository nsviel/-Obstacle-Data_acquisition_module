#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu
from param import param_li

from src import lidar

from gui import scheme_callback

import dearpygui.dearpygui as dpg


def node_pywardium(color_info):
    with dpg.node(label="Pywardium", tag="node_py", pos=[10, 75]):
        with dpg.node_attribute(tag="py_server", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Server")
        with dpg.node_attribute(tag="py_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Client")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_py.pywardium_ip, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_button(label="False alarm", tag="but_fal", callback=scheme_callback.callback_false_alarm)

def node_hubium(color_info):
    with dpg.node(label="Hubium", tag="node_hu", pos=[210, 175]):
        with dpg.node_attribute(tag="hu_stockage", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Stockage")
        with dpg.node_attribute(tag="hu_server", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Server")
        with dpg.node_attribute(tag="hu_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.hubium_ip, color=color_info);
        with dpg.node_attribute(tag="hu_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Socket port:");
                dpg.add_text(param_hu.hubium_httpd_port, color=color_info);
        with dpg.node_attribute(tag="hu_httpd_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("HTTP port:");
                dpg.add_text(param_hu.hubium_httpd_port, color=color_info);

def node_hardware(color_info):
    with dpg.node(label="Train", tag="node_train", pos=[210, 10]):
        with dpg.node_attribute(tag="l1_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Lidar 1:");
                dpg.add_text(param_li.nb_packet_l1, tag="l1_packet", color=color_info);
                dpg.add_button(label="Start", callback=lidar.start_l1_motor)
                dpg.add_button(label="Stop", callback=lidar.stop_l1_motor)
        with dpg.node_attribute(tag="l2_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Lidar 2:");
                dpg.add_text(param_li.nb_packet_l2, tag="l2_packet", color=color_info);
                dpg.add_button(label="Start", callback=lidar.start_l2_motor)
                dpg.add_button(label="Stop", callback=lidar.stop_l2_motor)
        with dpg.node_attribute(tag="geo_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Geo: [")
                dpg.add_text(param_py.geo_country, color=color_info)
                dpg.add_text("]")
        with dpg.node_attribute(tag="ssd_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("SSD:");
                dpg.add_text(param_py.ssd_space_used, tag="ssd_used", color=color_info);
                dpg.add_text("/");
                dpg.add_text(param_py.ssd_space_total, tag="ssd_total", color=color_info);
                dpg.add_text("Gb");

def node_edge(color_info):
    with dpg.node(label="Edge", tag="node_ed", pos=[430, 115]):
        with dpg.node_attribute(tag="ed_client", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Client");
        with dpg.node_attribute(tag="ed_server", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Server")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.edge_ip, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Socket port:");
                dpg.add_text(param_hu.edge_port, color=color_info);

def node_edge_local(color_info):
    with dpg.node(label="Local", tag="node_local", pos=[430, 10]):
        with dpg.node_attribute(tag="ve_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Velodium");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, color=color_info);
        with dpg.node_attribute(tag="ai_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("AI");

def node_sncf(color_info):
    with dpg.node(label="SNCF", tag="node_sncf", pos=[430, 240]):
        with dpg.node_attribute(tag="sncf_mqtt_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("MQTT");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.mqtt_ip, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("topic:");
                dpg.add_text(param_hu.mqtt_topic, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.mqtt_port, color=color_info);

def node_valeo(color_info):
    with dpg.node(label="Valeo", tag="node_valeo", pos=[10, 225]):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.valeo_ip, color=color_info);
        with dpg.node_attribute(tag="va_httpd_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("HTTP port:");
                dpg.add_text(param_hu.mqtt_port, color=color_info);
