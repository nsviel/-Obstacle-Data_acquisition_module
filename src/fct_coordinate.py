#! /usr/bin/python
#---------------------------------------------

from src import fct_param

def check_position():
    #-------------

    if(fct_param.geo_coordinate >= geo_border):
        fct_param.velo_IP = fct_param.IP["EDGE France"]
        fct_param.geo_country = "France"
    else:
        fct_param.velo_IP = fct_param.IP["EDGE Espagne"]
        fct_param.geo_country = "Espagne"

    #-------------
