#! /usr/bin/python
#---------------------------------------------

import pcapy


def get_all_device():
    return pcapy.findalldevs()


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
