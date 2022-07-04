#! /usr/bin/python
#---------------------------------------------

from src import param_py

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    param_py.run_loop = False

signal.signal(signal.SIGINT, handler)
