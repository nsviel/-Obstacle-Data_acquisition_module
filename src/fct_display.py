#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from src import fct_io

import sys
import os


def loop_nb_packet():
    #-------------

    if(fct_param.with_geolocalization):
        sys.stdout.write("[%s] \
        LiDAR 1 packet: [\033[94m%d\033[0m] - \
        LiDAR 2 packet: [\033[94m%d\033[0m]\r" \
        % (fct_param.geo_country, fct_param.lidar_1_nb_packet, fct_param.lidar_2_nb_packet))
    else:
        sys.stdout.write("\
        LiDAR 1 packet: [\033[94m%d\033[0m] - \
        LiDAR 2 packet: [\033[94m%d\033[0m]\r" \
        % (fct_param.lidar_1_nb_packet, fct_param.lidar_2_nb_packet))

    sys.stdout.flush()

    #-------------

def show_parameter():
    #-------------

    print("[\033[92mOPT\033[0m] Parameters:")
    print("\033[90m----------------------\033[0m")

    print(" path SSD - [\033[94m%s\033[0m]" % fct_param.path_ssd)
    print(" Velodium IP - [\033[94m%s\033[0m]" % fct_param.velo_IP)
    print(" Velodium port - [\033[94m%d\033[0m]" % fct_param.velo_port)
    print(" with_two_lidar - [\033[94m%s\033[0m]" % str(fct_param.with_two_lidar))
    print(" with_writing - [\033[94m%s\033[0m]" % str(fct_param.with_writing))
    print(" with_forwarding - [\033[94m%s\033[0m]" % str(fct_param.with_forwarding))
    print(" with_manual_naming - [\033[94m%s\033[0m]" % str(fct_param.with_manual_naming))
    print(" with_geolocalization - [\033[94m%s\033[0m]" % str(fct_param.with_geolocalization))
    print(" LiDAR 1 device - [\033[94m%s\033[0m]" % str(fct_param.lidar_1_dev))
    print(" LiDAR 2 device - [\033[94m%s\033[0m]" % str(fct_param.lidar_2_dev))
    print(" LiDAR speed - [\033[94m%s\033[0m]" % str(fct_param.lidar_speed))

    print("\033[90m----------------------\033[0m")
    ok = input("Accept [\033[92mY\033[0m/n/q]: ")
    fct_param.config_ok = str2bool(ok)
    if(ok == "q"):
        exit()

    #-------------

def show_stat():
    #-------------

    print("\033[90m----------------------\033[0m")
    print("[\033[92mSTA\033[0m] Statistics:")

    print(" [\033[96mCapture\033[0m] Time - [\033[94m%d\033[0m]s" % fct_param.duration)

    print(" [\033[96mLiDAR 1\033[0m] Number of packet - [\033[94m%d\033[0m]" % fct_param.lidar_1_nb_packet)
    print(" [\033[96mLiDAR 1\033[0m] Size of capture file - [\033[94m%.2f\033[0m]Gb" % fct_io.get_size_Gb(fct_param.path_lidar_1))

    print(" [\033[96mLiDAR 2\033[0m] Number of packet - [\033[94m%d\033[0m]" % fct_param.lidar_2_nb_packet)
    print(" [\033[96mLiDAR 2\033[0m] Size of capture file - [\033[94m%.2f\033[0m]Gb" % fct_io.get_size_Gb(fct_param.path_lidar_2))

    #-------------

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1', ''):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        return False
