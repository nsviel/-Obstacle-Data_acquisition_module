#---------------------------------------------
from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet_l1(packet):
    if(len(packet) == 1248):
        sock_client_fct.send_packet_l1(packet)

def send_packet_l2(packet):
    if(len(packet) == 1248):
        sock_client_fct.send_packet_l2(packet)
