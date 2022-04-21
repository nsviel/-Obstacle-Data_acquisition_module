#---------------------------------------------
#Python program fro port forwarding LiDAR data
#---------------------------------------------

import socket



#Create new client socket
def create_client_socket():
    #-------------

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return client_sock
    #-------------






