#! /usr/bin/python
#---------------------------------------------

from src import fct_param

import pcapy


def select_lidar_devices():
    #-------------

    #LiDAR 1 device
    fct_param.lidar_1_dev = select_device("LiDAR 1", fct_param.lidar_1_dev)

    #LiDAR 2 device
    if(fct_param.with_two_lidar):
        fct_param.lidar_2_dev = select_device("LiDAR 2", fct_param.lidar_2_dev)

    #-------------


#ask user to enter device name to sniff
def select_device(name, default):
    #-------------
    devices = pcapy.findalldevs()

    print("[\033[92mOPT\033[0m] - Devices for \033[96m" + name + "\033[0m are:")
    print("\033[90m----------------------\033[0m")

    cpt = 0
    for d in devices :
        if(d == default):
            print(cpt, ' - \033[92m', d, '\033[0m')
        else:
            print(cpt, ' - ', d)
        cpt += 1

    print("\033[90m----------------------\033[0m")
    in_dev = input("Enter device to sniff [\033[92m" + default + "\033[0m]: ")

    #Check for default
    if(in_dev == ""):
        print("Selected default \033[92m" + default + "\033[0m")
        return default;

    #Check if input is an integer
    try:
        val = int(in_dev)
    except ValueError:
        print('[\033[91mERR\033[0m] An integer is required')
        exit()

    #Check for good selected command
    good_choice = False
    cpt = 0
    dev = 0
    for d in devices:
        if(int(in_dev) == cpt):
            dev = d
            good_choice = True
        cpt += 1;

    if(good_choice == False):
        print('[\033[91mERR\033[0m] Not in list')
        exit();

    print("Selected device \033[92m" + dev + "\033[0m")

    return dev
    #-------------
