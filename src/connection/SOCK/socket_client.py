#---------------------------------------------
import socket


class Socket_client():
    def __init__(self):
        self.socket = None
        self.create_socket()

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_packet(self, packet, dest, source):
        packet = packet[len(packet) - 1206:]
        [ip, port] = socket.network_info(dest, source)
        if(packet != None):
            self.socket.sendto(packet, (ip, port))
