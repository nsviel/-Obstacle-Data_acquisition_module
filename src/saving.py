#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_li

from gui import gui_update

from datetime import datetime

import dearpygui.dearpygui as dpg
import pandas as pd
import psutil


def determine_path():
    date = get_formated_time()
    param_py.path_capture = os.path.join(param_py.ssd_path, "capture")
    param_py.path_dir_l1 = os.path.join(param_py.path_capture, "lidar_1")
    param_py.path_dir_l2 = os.path.join(param_py.path_capture, "lidar_2")
    param_li.path_file_l1 = os.path.join(param_py.path_dir_l1, "capture_" + date + "_" + param_li.path_name + ".pcap")
    param_li.path_file_l2 = os.path.join(param_py.path_dir_l2, "capture_" + date + "_" + param_li.path_name + ".pcap")
    dpg.set_value("l1p", param_li.path_file_l1)
    dpg.set_value("l2p", param_li.path_file_l2)

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    param_py.wallet_add = list()
    param_py.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_py.wallet_add.append(str(X[0][i]))
        param_py.wallet_ip.append(str(X[1][i]))

def test_is_ssd():
    if(os.path.exists(param_py.ssd_path)):
        param_py.ssd_connected = True
        hdd = psutil.disk_usage(param_py.ssd_path)
        param_py.ssd_space_used = int(hdd.used / (2**30))
        param_py.ssd_space_total = int(hdd.total / (2**30))
        gui_update.update_ssd_info()
    else:
        param_py.ssd_connected = False
        param_py.ssd_space_used = 0
        param_py.ssd_space_total = 0
        gui_update.update_ssd_info()


def check_directories():
    #Check existence, or create, directories
    #-------------

    # Create directory capture
    if(param_py.ssd_connected):
        if(os.path.exists(param_py.path_capture) == False):
            os.mkdir(param_py.path_capture)
            print("[\033[92mSSD\033[0m] Directory capture created")
        # Create directory 1
        if(os.path.exists(param_py.path_dir_1) == False):
            os.mkdir(param_py.path_dir_1)
            print("[\033[92mSSD\033[0m] Directory 1 created")
        # Create directory 2
        if(os.path.exists(param_py.path_dir_2) == False):
            os.mkdir(param_py.path_dir_2)
            print("[\033[92mSSD\033[0m] Directory 2 created")
