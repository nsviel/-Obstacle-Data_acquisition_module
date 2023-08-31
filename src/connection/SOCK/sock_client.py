#---------------------------------------------s
from src.utils import terminal


def send_packet_l1(packet):
    ip = param_capture.state_edge["hub"]["info"]["ip"]
    port = param_capture.state_ground["edge"]["socket"]["server_l1_port"]
    nb_packet = param_capture.state_ground["lidar_1"]["packet"]["sent"]

    if(packet != None and param_capture.sock_client_ok):
        param_capture.sock_client.sendto(packet, (ip, port))
        param_capture.state_ground["lidar_1"]["packet"]["sent"] = nb_packet + 1

def send_packet_l2(packet):
    ip = param_capture.state_edge["hub"]["info"]["ip"]
    port = param_capture.state_ground["edge"]["socket"]["server_l2_port"]
    nb_packet = param_capture.state_ground["lidar_2"]["packet"]["sent"]

    if(packet != None and param_capture.sock_client_ok):
        param_capture.sock_client.sendto(packet, (ip, port))
        param_capture.state_ground["lidar_2"]["packet"]["sent"] = nb_packet + 1
