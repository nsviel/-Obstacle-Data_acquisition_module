#! /usr/bin/python
#---------------------------------------------

from src import parameter

from gui import callback_node

import dearpygui.dearpygui as dpg



def build_scheme():
    create_scheme()
    init_scheme()

def create_scheme():
    editeur_size = 360
    node_size = 100
    color_info = (0, 200, 200)

    with dpg.node_editor(height = editeur_size):
        # Pywardium node
        with dpg.node(label="Pywardium", tag="node_py", pos=[10, 75]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.pywardium_ip, color=color_info);
            with dpg.node_attribute(tag="py_sock_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                dpg.add_text("Client")
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                dpg.add_button(label="False alarm", tag="but_fal", callback=callback_node.callback_false_alarm)

        # Hubium node
        with dpg.node(label="Hubium", tag="node_hu", pos=[210, 125]):
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
            with dpg.node_attribute(tag="hu_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                dpg.add_text("Client");

        # SSD node
        with dpg.node(label="SSD", tag="node_ssd", pos=[210, 25]):
            with dpg.node_attribute(tag="ssd_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                dpg.add_text("Stokage");

        # Edge node
        with dpg.node(label="Edge", tag="node_ed", pos=[430, 10]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.edge_ip, color=color_info);
            with dpg.node_attribute(tag="ed_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket port:");
                    dpg.add_text(parameter.edge_port, color=color_info);

        # Velodium node
        with dpg.node(label="Velodium", tag="node_ve", pos=[430, 100]):
            with dpg.node_attribute(tag="ve_sock_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket port:");
                    dpg.add_text(parameter.hubium_http_port, color=color_info);

        # AI node
        with dpg.node(label="AI", tag="node_ai", pos=[430, 175]):
            with dpg.node_attribute(tag="ai_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Prediction");

        # SNCF node
        with dpg.node(label="SNCF", tag="node_sncf", pos=[430, 250]):
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

        # Valeo node
        with dpg.node(label="Valeo", tag="node_valeo", pos=[10, 225]):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text(parameter.valeo_ip, color=color_info);
            with dpg.node_attribute(tag="va_http_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("HTTP port:");
                    dpg.add_text(parameter.mqtt_port, color=color_info);

        create_link()

def create_link():
    dpg.add_node_link("py_sock_port", "hu_sock_port", tag="link_py_hu_sock")
    dpg.add_node_link("py_sock_port", "hu_http_port", tag="link_py_hu_http")
    dpg.add_node_link("py_sock_port", "ssd_input", tag="link_py_ssd")
    dpg.add_node_link("va_http_port", "hu_http_port", tag="link_va_hu")
    dpg.add_node_link("hu_client", "sncf_mqtt_port", tag="link_hu_sncf")
    dpg.add_node_link("hu_client", "ve_sock_port", tag="link_hu_ve")
    dpg.add_node_link("hu_client", "ed_sock_port", tag="link_hu_ed")
    dpg.add_node_link("hu_client", "ai_input", tag="link_hu_ai")

def init_scheme():
    red = dpg.add_theme()
    with dpg.theme_component(dpg.mvButton, parent=red):
      link_theme_color = dpg.add_theme_color(dpg.mvThemeCol_Button, (117, 16, 16))

    layer_train = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_train):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (20, 82, 175), category=dpg.mvThemeCat_Nodes)

    layer_edge = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_edge):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (45, 108, 143), category=dpg.mvThemeCat_Nodes)

    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
      link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (106, 106, 105), category=dpg.mvThemeCat_Nodes)

    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_ssd", layer_train)
    dpg.bind_item_theme("node_hu", layer_edge)
    dpg.bind_item_theme("node_ve", layer_edge)
    dpg.bind_item_theme("node_ai", layer_edge)
    dpg.bind_item_theme("node_ed", layer_cloud)
    dpg.bind_item_theme("node_sncf", layer_cloud)
    dpg.bind_item_theme("but_fal", red)

def update_link(state, tag):
    if(state):
        green = dpg.add_theme()
        with dpg.theme_component(dpg.mvNodeLink, parent=green):
            link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (20, 255, 20), category=dpg.mvThemeCat_Nodes)
        dpg.bind_item_theme(tag, green)
    else:
        red = dpg.add_theme()
        with dpg.theme_component(dpg.mvNodeLink, parent=red):
          link_theme_color = dpg.add_theme_color(dpg.mvNodeCol_Link, (255, 20, 20), category=dpg.mvThemeCat_Nodes)
        dpg.bind_item_theme(tag, red)
