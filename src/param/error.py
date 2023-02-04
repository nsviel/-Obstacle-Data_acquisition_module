#---------------------------------------------
from src.param import param

import time

timer_nodata_tic = 0
cpt_nodata = 0

def start_timer_nodata():
    timer_nodata_tic = time.perf_counter()

def stop_timer_nodata():
    toc = time.perf_counter()
    duration = toc - timer_nodata_tic 
