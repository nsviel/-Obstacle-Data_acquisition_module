from src import loop
from src import signal
from src import connection

import socket
import os


#Clear terminal
os.system('clear')

#Header
program = "Pywardium"
hostname = socket.gethostname()
ip = connection.get_ip_adress()
print("Program: \033[1;34m%s\033[0m"% program)
print("IP: \033[1;34m%s\033[0m"% ip)
print("-----------------------")
os.system('hostnamectl')
print("-----------------------")
#-------------

loop.program()

#-------------
print("-----------------------")
print("Program \033[1;34mexit\033[0m")
