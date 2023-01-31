#---------------------------------------------
from src.param import param_py
from src.misc import connection
from src.misc import parser_json
from src.misc import terminal
from src.misc import device

def load_configuration():
    load_json_file()
    init_state_py()
    init_state_perf()
    load_config_file()
    upload_state()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_py.state_py = parser_json.load_state(param_py.path_state_py)
    param_py.state_perf = parser_json.load_state(param_py.path_state_perf)

def init_state_py():
    param_py.state_py["self"]["ip"] = connection.get_ip_adress()

    param_py.state_py["lidar_1"]["connected"] = False
    param_py.state_py["lidar_1"]["running"] = False
    param_py.state_py["lidar_2"]["connected"] = False
    param_py.state_py["lidar_2"]["running"] = False

    param_py.state_py["lidar_1"]["packet"]["value"] = 0
    param_py.state_py["lidar_1"]["packet"]["min"] = 0
    param_py.state_py["lidar_1"]["packet"]["mean"] = 0
    param_py.state_py["lidar_1"]["packet"]["max"] = 0
    param_py.state_py["lidar_1"]["packet"]["sent"] = 0

    param_py.state_py["lidar_1"]["throughput"]["value"] = 0
    param_py.state_py["lidar_1"]["throughput"]["min"] = 0
    param_py.state_py["lidar_1"]["throughput"]["mean"] = 0
    param_py.state_py["lidar_1"]["throughput"]["max"] = 0

    param_py.state_py["lidar_2"]["packet"]["value"] = 0
    param_py.state_py["lidar_2"]["packet"]["min"] = 0
    param_py.state_py["lidar_2"]["packet"]["mean"] = 0
    param_py.state_py["lidar_2"]["packet"]["max"] = 0
    param_py.state_py["lidar_2"]["packet"]["sent"] = 0

    param_py.state_py["lidar_2"]["throughput"]["value"] = 0
    param_py.state_py["lidar_2"]["throughput"]["min"] = 0
    param_py.state_py["lidar_2"]["throughput"]["mean"] = 0
    param_py.state_py["lidar_2"]["throughput"]["max"] = 0

def init_state_perf():
    param_py.state_perf["local_cloud"]["time"] = 0
    param_py.state_perf["local_cloud"]["bandwidth"]["value"] = 0
    param_py.state_perf["local_cloud"]["bandwidth"]["min"] = 0
    param_py.state_perf["local_cloud"]["bandwidth"]["max"] = 0
    param_py.state_perf["local_cloud"]["bandwidth"]["mean"] = 0
    param_py.state_perf["local_cloud"]["latency"]["value"] = 0
    param_py.state_perf["local_cloud"]["latency"]["min"] = 0
    param_py.state_perf["local_cloud"]["latency"]["max"] = 0
    param_py.state_perf["local_cloud"]["latency"]["mean"] = 0
    param_py.state_perf["local_cloud"]["jitter"]["value"] = 0
    param_py.state_perf["local_cloud"]["jitter"]["min"] = 0
    param_py.state_perf["local_cloud"]["jitter"]["max"] = 0
    param_py.state_perf["local_cloud"]["jitter"]["mean"] = 0
    param_py.state_perf["local_cloud"]["reliability"]["value"] = 0
    param_py.state_perf["local_cloud"]["reliability"]["min"] = 0
    param_py.state_perf["local_cloud"]["reliability"]["max"] = 0
    param_py.state_perf["local_cloud"]["reliability"]["mean"] = 0
    param_py.state_perf["local_cloud"]["interruption"]["value"] = 0
    param_py.state_perf["local_cloud"]["interruption"]["min"] = 0
    param_py.state_perf["local_cloud"]["interruption"]["max"] = 0
    param_py.state_perf["local_cloud"]["interruption"]["mean"] = 0

    param_py.state_perf["cloud_local"]["time"] = 0
    param_py.state_perf["cloud_local"]["bandwidth"]["value"] = 0
    param_py.state_perf["cloud_local"]["bandwidth"]["min"] = 0
    param_py.state_perf["cloud_local"]["bandwidth"]["max"] = 0
    param_py.state_perf["cloud_local"]["bandwidth"]["mean"] = 0
    param_py.state_perf["cloud_local"]["latency"]["value"] = 0
    param_py.state_perf["cloud_local"]["latency"]["min"] = 0
    param_py.state_perf["cloud_local"]["latency"]["max"] = 0
    param_py.state_perf["cloud_local"]["latency"]["mean"] = 0
    param_py.state_perf["cloud_local"]["jitter"]["value"] = 0
    param_py.state_perf["cloud_local"]["jitter"]["min"] = 0
    param_py.state_perf["cloud_local"]["jitter"]["max"] = 0
    param_py.state_perf["cloud_local"]["jitter"]["mean"] = 0
    param_py.state_perf["cloud_local"]["reliability"]["value"] = 0
    param_py.state_perf["cloud_local"]["reliability"]["min"] = 0
    param_py.state_perf["cloud_local"]["reliability"]["max"] = 0
    param_py.state_perf["cloud_local"]["reliability"]["mean"] = 0

    param_py.state_perf["end_to_end"]["time_slam"] = 0
    param_py.state_perf["end_to_end"]["time_ai"] = 0
    param_py.state_perf["end_to_end"]["time_total"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_py.path_config)
    param_py.state_py["self"]["http_server_port"] = config["self"]["http_server_port"]
    param_py.state_py["self"]["l1_port"] = config["self"]["l1_port"]
    param_py.state_py["self"]["l2_port"] = config["self"]["l2_port"]

    param_py.state_py["perf"]["iperf_activated"] = config["perf"]["iperf_activated"]
    param_py.state_py["perf"]["iperf_port"] = config["perf"]["iperf_port"]

    param_py.state_py["lidar_1"]["ip"] = config["lidar_1"]["ip"]
    param_py.state_py["lidar_1"]["port"] = config["lidar_1"]["port"]
    param_py.state_py["lidar_1"]["activated"] = config["lidar_1"]["activated"]
    param_py.state_py["lidar_1"]["speed"] = config["lidar_1"]["speed"]

    param_py.state_py["lidar_2"]["ip"] = config["lidar_2"]["ip"]
    param_py.state_py["lidar_2"]["port"] = config["lidar_2"]["port"]
    param_py.state_py["lidar_2"]["activated"] = config["lidar_2"]["activated"]
    param_py.state_py["lidar_2"]["speed"] = config["lidar_2"]["speed"]

    param_py.state_py["hubium"]["sock_server_l1_port"] = config["hubium"]["sock_server_l1_port"]
    param_py.state_py["hubium"]["sock_server_l2_port"] = config["hubium"]["sock_server_l2_port"]
    param_py.state_py["hubium"]["iperf_port"] = config["hubium"]["iperf_port"]

    # Check if existing device exists, else take the config one
    if(device.check_if_device_exists(param_py.state_py["lidar_1"]["device"]) == False):
        param_py.state_py["lidar_1"]["device"] = config["lidar_1"]["device"]
    if(device.check_if_device_exists(param_py.state_py["lidar_2"]["device"]) == False):
        param_py.state_py["lidar_2"]["device"] = config["lidar_2"]["device"]

def upload_state():
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    parser_json.upload_file(param_py.path_state_perf, param_py.state_perf)
