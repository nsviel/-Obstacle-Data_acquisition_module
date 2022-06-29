#! /usr/bin/python
#---------------------------------------------

from src import parameter
from datetime import datetime


def determine_path():
    date = get_formated_time()
    parameter.path_capture = os.path.join(parameter.path_ssd, "capture")
    parameter.path_dir_l1 = os.path.join(parameter.path_capture, "lidar_1")
    parameter.path_dir_l2 = os.path.join(parameter.path_capture, "lidar_2")
    parameter.path_file_l1 = os.path.join(parameter.path_dir_l1, date + ".pcap")
    parameter.path_file_l2 = os.path.join(parameter.path_dir_l2, date + ".pcap")

def get_formated_time():
    date = datetime.now().strftime('_%d-%m-%Y_%Hh%M')
    return str(date)
