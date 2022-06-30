#! /usr/bin/python
#---------------------------------------------

from src import parameter
from datetime import datetime

import dearpygui.dearpygui as dpg
import pandas as pd


def determine_path():
    date = get_formated_time()
    parameter.path_capture = os.path.join(parameter.path_ssd, "capture")
    parameter.path_dir_l1 = os.path.join(parameter.path_capture, "lidar_1")
    parameter.path_dir_l2 = os.path.join(parameter.path_capture, "lidar_2")
    parameter.path_file_l1 = os.path.join(parameter.path_dir_l1, "capture_" + date + "_" + parameter.path_name + ".pcap")
    parameter.path_file_l2 = os.path.join(parameter.path_dir_l2, "capture_" + date + "_" + parameter.path_name + ".pcap")
    dpg.set_value("l1p", parameter.path_file_l1)
    dpg.set_value("l2p", parameter.path_file_l2)

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    parameter.wallet_add = list()
    parameter.wallet_ip = list()
    for i in range(0, len(X[0])):
        parameter.wallet_add.append(str(X[0][i]))
        parameter.wallet_ip.append(str(X[1][i]))

def check_directories():
    #Check existence, or create, directories
    #-------------
    parameter.ssd_connected = False

    if(parameter.with_writing):
        if(os.path.exists(parameter.path_ssd) == False):
            print("[\033[91mERR\033[0m] No SSD detected: " + parameter.path_ssd)
        else:
            parameter.ssd_connected = True

    # Create directory capture
    if(parameter.ssd_connected):
        if(os.path.exists(parameter.path_capture) == False):
            os.mkdir(parameter.path_capture)
            print("[\033[92mSSD\033[0m] Directory capture created")
        # Create directory 1
        if(os.path.exists(parameter.path_dir_1) == False):
            os.mkdir(parameter.path_dir_1)
            print("[\033[92mSSD\033[0m] Directory 1 created")
        # Create directory 2
        if(os.path.exists(parameter.path_dir_2) == False):
            os.mkdir(parameter.path_dir_2)
            print("[\033[92mSSD\033[0m] Directory 2 created")
