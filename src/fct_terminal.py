#! /usr/bin/python
#---------------------------------------------

from src import fct_param

import argparse
import os
import sys


def clear():
    #-------------

    os.system('clear')

    #-------------

def compute_argument():
    #-------------

    if(len(sys.argv) > 1):
        parser = argparse.ArgumentParser()

        #Set argument
        parser.add_argument("two_lidar", default=False)

        # Parsing
        args = parser.parse_args()

        #Compute arg 
        fct_param.with_two_lidar = str2bool(args.two_lidar)

    #-------------

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
