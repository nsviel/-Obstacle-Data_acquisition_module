#! /usr/bin/python
#---------------------------------------------

import pcapy


def get_all_device():
    return pcapy.findalldevs()


#ask user to enter device name to sniff
def check_if_device_exists(name):
    devices = get_all_device()
    exist = False
    for d in devices :
        if(d == name):
            exist = True
            break
    return exist
