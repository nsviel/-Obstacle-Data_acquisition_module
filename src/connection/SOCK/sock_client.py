#---------------------------------------------
from src.connection.SOCK import sock_client_fct
from src.utils import terminal


def connection():
    try:
        sock_client_fct.create_socket()
        terminal.addLog("#", "Socket client created")
    except:
        print("[\033[1;32merror\033[0m]   Socket client")

def send_packet_l1(packet):
    sock_client_fct.send_packet_l1(packet)

def send_packet_l2(packet):
    sock_client_fct.send_packet_l2(packet)
