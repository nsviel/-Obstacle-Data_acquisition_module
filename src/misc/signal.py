#---------------------------------------------
from src.misc import connection
from src.misc import terminal
from src.param import param_capture

import socket
import platform
import signal
import time
import os
import sys


# Manage Ctrl+C input
def handler(signum, frame):
    param_capture.run_loop = False
    print("")
    print("")

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

def system_clear():
    os.system('clear')

def check_for_root():
    if not os.geteuid() == 0:
        terminal.addLog("error", "Only root can run this script")
        sys.exit()

def system_information(prog_name):
    check_for_root()

    #Info
    program = prog_name
    ip = connection.get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()

    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()

    #Header
    #Header
    print('%-12s' '\033[1;34m%s\033[0m' % ("[Obstacle]", program))
    print("-----------------------")
    print('%-12s' '\033[1;34m%s\033[0m' % ("IP", ip))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Hostname", hostname))
    print('%-12s' '\033[1;34m%s\033[0m, \033[1;34m%s\033[0m' % ("Arch", arch, proc))
    print('%-12s' '\033[1;34m%s\033[0m' % ("OS", OS))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Core", core))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Python", python))
    print("-----------------------")
