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
print("-----------------------")
print("Program: \033[1;34m%s\033[0m"% program)
print("IP: \033[1;34m%s\033[0m"% ip)
print("Hostname: \033[1;34m%s\033[0m"% hostname)
print("-----------------------")
#-------------

loop.program()

#-------------
print("-----------------------")
print("\033[1;34mExit\033[0m")
print("-----------------------")
