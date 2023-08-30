#---------------------------------------------
# Terminal output functions
#---------------------------------------------
from src.param import param_capture

import time


def addLog(type, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     "+ message)
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    "+ message)
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] "+ message)
    elif(type == "com"):
        print("[\033[1;38mCOM\033[0m]  "+ message)
    elif(type == "post"):
        print("[\033[1;30mPOST\033[0m]  "+ message)
    time.sleep(param_capture.tic_message)

def addCstLog(type, message):
    if(type == "cap"):
        print("[\033[1;34mCAP\033[0m]   "+ message, end="\r")

def addConnection(dest, state):
    if(dest == "edge"):
        dest = "Edge"
    elif(dest == "capture"):
        dest = "Capture"
    elif(dest == "ve"):
        dest = "SLAM"
    elif(dest == "ai"):
        dest = "AI"

    if(state == "on"):
        print("[\033[1;36mCON\033[0m]   Connection \033[1;32mON\033[0m  - "+ dest)
    elif(state == "off"):
        print("[\033[1;36mCON\033[0m]   Connection \033[1;31mOFF\033[0m - "+ dest)

def add_post_command(dest, c1, c2, c3):
    if(dest == "capture"):
        message = "Received [%s, %s, %s]"%(c1, c2, c3)
    else:
        message = "To %s [%s, %s, %s]"%(dest, c1, c2, c3)
    if(c1 == "" and c2 == "" and c3 == ""):
        message = dest

    print("[\033[1;30mPOST\033[0m]  " + message)
    time.sleep(param_capture.tic_message)

def addDaemon(type, status, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     Daemon ", flush=True, end='')
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    Daemon ", flush=True, end='')
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] Daemon ", flush=True, end='')

    if(status == "ON"):
        print("\033[1;32mON\033[0m - "+message)
    elif(status == "OFF"):
        print("\033[1;31mOFF\033[0m - "+message)
    elif(status == "restart"):
        print("\033[1;30mRESTART\033[0m - "+message)

    time.sleep(param_capture.tic_message)

def addLine():
    print("")

def shutdown():
    addLine()
    addLine()
    print("[\033[1;32mOK\033[0m]    Program shutdown ...",)

def delai():
    print("[\033[1;34m#\033[0m]     Daemon closing", flush=True, end='')
    print("...2", flush=True, end='')
    time.sleep(1)
    print("...1", flush=True)
    time.sleep(1)

def fatal_error():
    print("\033[1;31m--- Fatal error ---\033[0m")
