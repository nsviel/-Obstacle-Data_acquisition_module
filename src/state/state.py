#---------------------------------------------
from src.param import param_capture
from src.connection import connection
from src.utils import parser_json
from src.utils import terminal
from src.interface import device

def load_configuration():
    load_json_file()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_capture.state_ground = parser_json.load_state(param_capture.path_state_initial + "state_ground.json")
    param_capture.state_network = parser_json.load_state(param_capture.path_state_initial + "state_network.json")
    param_capture.state_edge = parser_json.load_state(param_capture.path_state_initial + "state_edge.json")
    param_capture.state_ground["capture"]["ip"] = connection.get_ip_adress()

def upload_states():
    parser_json.upload_file(param_capture.path_state_current + "state_ground.json", param_capture.state_ground)
    parser_json.upload_file(param_capture.path_state_current + "state_network.json", param_capture.state_network)
