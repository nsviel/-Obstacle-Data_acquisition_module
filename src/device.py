#---------------------------------------------
from param import param_py
import pcapy


def update_list():
    devices = get_all_device()
    cpt = 0
    for d in devices :
        y = {str(cpt): str(d)}
        param_py.state_py["device"].update(y)
        cpt = cpt + 1

def get_all_device():
    return pcapy.findalldevs()

def check_if_device_exists(name):
    devices = get_all_device()
    exist = False
    for d in devices :
        if(d == name):
            exist = True
            break
    return exist
