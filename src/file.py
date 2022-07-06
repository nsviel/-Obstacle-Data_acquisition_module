#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from param import param_py
from param import param_li

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    param_py.socket_listen = parser_json.upload_state_lvl2_json(param_py.path_config, "pywardium", "socket_listen")
    param_py.with_two_lidar = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "with_two_lidar")
    param_py.with_writing = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "with_writing")
    param_py.ip_l1 = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "ip_l1")
    param_py.ip_l2 = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "ip_l2")
    param_py.device_l1 = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "device_l1")
    param_py.device_l2 = parser_json.upload_state_lvl2_json(param_py.path_config, "lidar", "device_l2")
    param_hu.hubium_ip = parser_json.upload_state_lvl2_json(param_py.path_config, "hubium", "ip")
    param_hu.hubium_sock_port = parser_json.upload_state_lvl2_json(param_py.path_config, "hubium", "port_sock")
    param_hu.hubium_httpd_port = parser_json.upload_state_lvl2_json(param_py.path_config, "hubium", "port_http")

def update_state_file():
    parser_json.update_state_lvl1_json(param_py.path_state_py, "status", param_py.status)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "pywardium", "socket_listen", param_py.socket_listen)

    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "with_two_lidar", param_py.with_two_lidar)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "with_writing", param_py.with_writing)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "ip_l1", param_py.ip_l1)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "ip_l2", param_py.ip_l2)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "device_l1", param_py.device_l1)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "lidar", "device_l2", param_py.device_l2)

    parser_json.update_state_lvl2_json(param_py.path_state_py, "hubium", "ip", param_hu.hubium_ip)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "hubium", "port_sock", param_hu.hubium_sock_port)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "hubium", "port_http", param_hu.hubium_httpd_port)

    parser_json.update_state_lvl2_json(param_py.path_state_py, "connection", "lidar_1", param_li.l1_connected)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "connection", "lidar_2", param_li.l2_connected)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "connection", "hu_sock", param_py.socket_connected)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "connection", "hu_http", param_py.http_connected)
    parser_json.update_state_lvl2_json(param_py.path_state_py, "connection", "ssd", param_py.ssd_connected)
