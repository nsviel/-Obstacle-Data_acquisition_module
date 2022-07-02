#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import callback

import dearpygui.dearpygui as dpg



def build_state():
    create_scheme()
    init_scheme()

def create_scheme():
    node_size = 100
    color_info = (0, 200, 200)

    with dpg.node_editor(height = 400):
        # Pywardium node
        with dpg.node(label="Pywardium", tag="node_py", pos=[10, 150]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.pywardium_ip, color=color_info);
            with dpg.node_attribute(tag="py_sock_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                dpg.add_text("Socket")

        # Hubium node
        with dpg.node(label="Hubium", tag="node_hu", pos=[200, 150]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.hubium_ip, color=color_info);
            with dpg.node_attribute(tag="hu_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket port:");
                    dpg.add_text(parameter.hubium_http_port, color=color_info);
            with dpg.node_attribute(tag="hu_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                dpg.add_text("Client");

        # Edge node
        with dpg.node(label="Edge", tag="node_ed", pos=[400, 10]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.edge_ip, color=color_info);
            with dpg.node_attribute(tag="ed_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket port:");
                    dpg.add_text(parameter.edge_port, color=color_info);

        # Velodium node
        with dpg.node(label="Velodium", tag="node_ve", pos=[400, 150]):
            with dpg.node_attribute(tag="ve_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket port:");
                    dpg.add_text(parameter.hubium_http_port, color=color_info);

        # SNCF node
        with dpg.node(label="SNCF", tag="node_sncf", pos=[400, 250]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.mqtt_ip, color=color_info);
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("topic:");
                    dpg.add_text(parameter.mqtt_topic, color=color_info);
            with dpg.node_attribute(tag="sncf_mqtt_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("MQTT port:");
                    dpg.add_text(parameter.mqtt_port, color=color_info);

        create_link()

def create_link():
    dpg.add_node_link("py_sock_port", "hu_sock_port", tag="link_py_hu_sock")
    dpg.add_node_link("hu_client", "sncf_mqtt_port", tag="link_hu_sncf")
    dpg.add_node_link("hu_client", "ve_sock_port", tag="link_hu_ve")
    dpg.add_node_link("hu_client", "ed_sock_port", tag="link_hu_ed")

def init_scheme():
    layer_train = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_train):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (52, 82, 92), category=dpg.mvThemeCat_Nodes)

    layer_edge = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_edge):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (95, 128, 163), category=dpg.mvThemeCat_Nodes)

    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (146, 146, 145), category=dpg.mvThemeCat_Nodes)

    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_hu", layer_edge)
    dpg.bind_item_theme("node_ve", layer_edge)
    dpg.bind_item_theme("node_ed", layer_cloud)
    dpg.bind_item_theme("node_sncf", layer_cloud)
