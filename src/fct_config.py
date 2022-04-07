#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from src import fct_device
from src import fct_display


def make_config():
    #-------------

    fct_display.show_parameter()

    while(fct_param.config_ok == False):
        #Specific options
        fct_param.with_two_lidar = select_boolean_option("With two lidar")
        fct_param.with_writing = select_boolean_option("With writing on SSD")
        fct_param.lidar_speed = select_integer_option(fct_param.lidar_speed, "Lidar speed")

        #Connection parameters
        select_forwarding_ip()
        fct_device.select_lidar_devices()

        #Check if ok
        fct_display.show_parameter()

    #-------------

def select_boolean_option(name):
    #-------------

    choice = input("[\033[92mOPT\033[0m] - " + name + " [\033[92mY\033[0m/n]: ")
    result = str2bool(choice)

    return result
    #-------------

def select_integer_option(option, name):
    #-------------

    choice = input("[\033[92mOPT\033[0m] - " + name + " [\033[92m" + str(option) + "\033[0m]: ")
    if(choice == ""):
        return option
    else:
        check_if_integer(choice)

    return choice
    #-------------

def select_forwarding_ip():
    #-------------

    print("[\033[92mOPT\033[0m] - Forwarding IP are:")
    print("\033[90m----------------------\033[0m")

    cpt = 0
    for name, ip in fct_param.IP.items() :
        print(cpt," - ",name, "[\033[94m", ip, "\033[0m]")
        cpt = cpt + 1

    print("\033[90m----------------------\033[0m")
    in_ip = input("Enter forwarding IP [\033[92m" + fct_param.velo_IP + "\033[0m] : ")

    #Check for default
    if(in_ip == ""):
        print("Selected default \033[92m" + fct_param.velo_IP + "\033[0m")
        return

    #Check if input is an integer
    check_if_integer(in_ip)

    #Check for good selected command
    good_choice = False
    if(int(in_ip) >= 0 and int(in_ip) < cpt):
        good_choice = True

    if(good_choice == False):
        print('[\033[91mERR\033[0m] Not in list')
        exit();

    cpt = 0
    for name, ip in fct_param.IP.items() :
        if(int(in_ip) == cpt):
            fct_param.velo_IP = ip
        cpt = cpt + 1

    print("Selected IP \033[92m" + fct_param.velo_IP + "\033[0m")

    #-------------

def check_if_integer(value):
    #Check if input is an integer
    try:
        val = int(value)
    except ValueError:
        print('[\033[91mERR\033[0m] An integer is required')
        exit()

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        return True
