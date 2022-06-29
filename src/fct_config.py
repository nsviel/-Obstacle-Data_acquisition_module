#! /usr/bin/python
#---------------------------------------------

from src import fct_param
from src import fct_device
from src import fct_display

import pandas as pd
from collections import defaultdict

from src import fct_param

def check_position():
    #-------------

    if(fct_param.geo_coordinate >= geo_border):
        fct_param.velo_ip = fct_param.IP["EDGE France"]
        fct_param.geo_country = "France"
    else:
        fct_param.velo_ip = fct_param.IP["EDGE Spain"]
        fct_param.geo_country = "Spain"

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
    in_ip = input("Enter forwarding IP [\033[92m" + fct_param.velo_ip + "\033[0m] : ")

    #Check for default
    if(in_ip == ""):
        print("Selected default \033[92m" + fct_param.velo_ip + "\033[0m")
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
            fct_param.velo_ip = ip
        cpt = cpt + 1

    print("Selected IP \033[92m" + fct_param.velo_ip + "\033[0m")

    #-------------

def read_wallet():
    #-------------

    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)

    for i in range(0, len(X[0])):
        fct_param.IP[str(X[0][i])] = str(X[1][i])

    #-------------
