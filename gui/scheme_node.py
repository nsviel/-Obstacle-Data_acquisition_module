#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import callback_node

import dearpygui.dearpygui as dpg


def node_pywardium(color_info):
    with dpg.node(label="Pywardium", tag="node_py", pos=[10, 75]):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(parameter.pywardium_ip, color=color_info);
        with dpg.node_attribute(tag="py_sock_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Client")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_button(label="False alarm", tag="but_fal", callback=callback_node.callback_false_alarm)

def node_hubium(color_info):
    with dpg.node(label="Hubium", tag="node_hu", pos=[210, 150]):
        with dpg.node_attribute(tag="hu_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(parameter.hubium_ip, color=color_info);
        with dpg.node_attribute(tag="hu_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Socket port:");
                dpg.add_text(parameter.hubium_http_port, color=color_info);
        with dpg.node_attribute(tag="hu_http_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("HTTP port:");
                dpg.add_text(parameter.hubium_http_port, color=color_info);

def node_hardware(color_info):
    with dpg.node(label="Hardware", tag="node_hard", pos=[210, 10]):
        with dpg.node_attribute(tag="l1_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Lidar 1");
        with dpg.node_attribute(tag="l2_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Lidar 2");
        with dpg.node_attribute(tag="ssd_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("SSD");

def node_edge(color_info):
    with dpg.node(label="Edge", tag="node_ed", pos=[430, 10]):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(parameter.edge_ip, color=color_info);
        with dpg.node_attribute(tag="ed_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Socket port:");
                dpg.add_text(parameter.edge_port, color=color_info);

def node_edge_local(color_info):
    with dpg.node(label="Local", tag="node_local", pos=[430, 105]):
        with dpg.node_attribute(tag="ve_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Velodium");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(parameter.hubium_http_port, color=color_info);
        with dpg.node_attribute(tag="ai_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("AI");

def node_sncf(color_info):
    with dpg.node(label="SNCF", tag="node_sncf", pos=[430, 220]):
        with dpg.node_attribute(tag="sncf_mqtt_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("MQTT");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(parameter.mqtt_ip, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("topic:");
                dpg.add_text(parameter.mqtt_topic, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(parameter.mqtt_port, color=color_info);

def node_valeo(color_info):
    with dpg.node(label="Valeo", tag="node_valeo", pos=[10, 225]):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(parameter.valeo_ip, color=color_info);
        with dpg.node_attribute(tag="va_http_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("HTTP port:");
                dpg.add_text(parameter.mqtt_port, color=color_info);
