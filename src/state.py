#! /usr/bin/python
#---------------------------------------------

from param import param_py
from src import connection
from src import parser_json


def load_configuration():
    load_json_file()
    init_state()
    load_config_file()
    upload_state()

def load_json_file():
    param_py.state_py = parser_json.load_file(param_py.path_state_py)

def init_state():
    param_py.state_py["self"]["status"] = "Offline"
    param_py.state_py["self"]["ip"] = connection.get_ip_adress()

    param_py.state_py["lidar_1"]["connected"] = False
    param_py.state_py["lidar_1"]["nb_packet"] = 0
    param_py.state_py["lidar_1"]["bandwidth"] = 0

    param_py.state_py["lidar_2"]["connected"] = False
    param_py.state_py["lidar_2"]["nb_packet"] = 0
    param_py.state_py["lidar_2"]["bandwidth"] = 0

def load_config_file():
    config = parser_json.load_file(param_py.path_config)
    param_py.state_py["self"]["http_server_port"] = config["self"]["http_server_port"]
    param_py.state_py["self"]["l1_port"] = config["self"]["l1_port"]
    param_py.state_py["self"]["l2_port"] = config["self"]["l2_port"]

    param_py.state_py["lidar_1"]["ip"] = config["lidar_1"]["ip"]
    param_py.state_py["lidar_1"]["port"] = config["lidar_1"]["port"]
    param_py.state_py["lidar_1"]["device"] = config["lidar_1"]["device"]
    param_py.state_py["lidar_1"]["speed"] = config["lidar_1"]["speed"]

    param_py.state_py["lidar_2"]["ip"] = config["lidar_2"]["ip"]
    param_py.state_py["lidar_2"]["port"] = config["lidar_2"]["port"]
    param_py.state_py["lidar_2"]["device"] = config["lidar_2"]["device"]
    param_py.state_py["lidar_2"]["speed"] = config["lidar_2"]["speed"]

    param_py.state_py["hubium"]["sock_server_ip"] = config["hubium"]["sock_server_ip"]
    param_py.state_py["hubium"]["sock_server_l1_port"] = config["hubium"]["sock_server_l1_port"]
    param_py.state_py["hubium"]["sock_server_l2_port"] = config["hubium"]["sock_server_l2_port"]

def upload_state():
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
