#!/usr/bin/env python3
#---------------------------------------------
from src import loop
from src.misc import signal


signal.system_clear()
signal.system_information("Data Acquisition Module")
#-------------

loop.program()

#-------------
print("-----------------------")
print("Program \033[1;34mexit\033[0m")
