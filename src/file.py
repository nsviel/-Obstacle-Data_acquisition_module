#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import parser_json


def load_configuration():
    load_json_file()
    upload_config_file()
    reset_value()

def load_json_file():
    param_py.state_py = parser_json.load_file(param_py.path_state_py)

def upload_config_file():
    config = parser_json.load_file(param_py.path_config)
    param_py.state_py["self"]["http_server_port"] = config["self"]["http_server_port"]

    param_py.state_py["lidar_1"]["ip"] = config["lidar_1"]["ip"]
    param_py.state_py["lidar_1"]["device"] = config["lidar_1"]["device"]
    param_py.state_py["lidar_1"]["speed"] = config["lidar_1"]["speed"]

    param_py.state_py["lidar_2"]["ip"] = config["lidar_2"]["ip"]
    param_py.state_py["lidar_2"]["device"] = config["lidar_2"]["device"]
    param_py.state_py["lidar_2"]["speed"] = config["lidar_2"]["speed"]

    param_py.state_py["hubium"]["sock_server_ip"] = config["hubium"]["sock_server_ip"]
    param_py.state_py["hubium"]["sock_server_port"] = config["hubium"]["sock_server_port"]

def reset_value():
    param_py.state_py["self"]["status"] = "Offline"
    param_py.state_py["lidar_1"]["sock_connected"] = False
    param_py.state_py["lidar_2"]["connected"] = False
