#! /usr/bin/python
#---------------------------------------------

from src import fct_param

import os


#Check existence, or create, directories
def check_directories():
    sucess = True
    #-------------

    if(os.path.exists(fct_param.path_ssd) == False):
        print("[\033[91mERR\033[0m] No SSD detected: " + fct_param.path_ssd)
        fct_param.ssd_connected = False
    else:
        fct_param.ssd_connected = True

    # Create directory capture
    if(fct_param.ssd_connected):
        if(os.path.exists(fct_param.path_capture) == False):
            os.mkdir(fct_param.path_capture)
            print("[\033[92mSSD\033[0m] Directory capture created")

        # Create directory 1
        if(os.path.exists(fct_param.path_dir_1) == False):
            os.mkdir(fct_param.path_dir_1)
            print("[\033[92mSSD\033[0m] Directory 1 created")

        # Create directory 2
        if(os.path.exists(fct_param.path_dir_2) == False):
            os.mkdir(fct_param.path_dir_2)
            print("[\033[92mSSD\033[0m] Directory 2 created")

        #End message
        print("[\033[92mSSD\033[0m] Directories OK")

    #-------------

def capture_save_name():
    if(fct_param.with_manual_naming):
        #LiDAR 1 capture name
        name = input("[\033[92mNAM\033[0m] Name for \033[96mLiDAR 1\033[0m [y]: " + fct_param.capture_L1_name)
        if(name != "" and name != "y" and name != "Y"):
            fct_param.capture_L1_name = name

        #LiDAR 2 capture name
        name = input("[\033[92mNAM\033[0m] Name for \033[96mLiDAR 2\033[0m [y]: " + fct_param.capture_L2_name)
        if(name != "" and name != "y" and name != "Y"):
            fct_param.capture_L2_name = name
