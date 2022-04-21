#! /usr/bin/python
#---------------------------------------------

from src import fct_param

import signal
import time


def handler(signum, frame):
    print("[\033[92mLID\033[0m] - Stop LiDAR loop")
    fct_param.run = False

signal.signal(signal.SIGINT, handler)
