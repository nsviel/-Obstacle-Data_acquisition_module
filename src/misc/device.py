#---------------------------------------------
from src.param import param_py
import pcapy


def update_list():
    devices = get_all_device()
    cpt = 0
    for d in devices :
        y = {str(cpt): str(d)}
        param_py.state_py["device"].update(y)
        cpt = cpt + 1

def get_all_device():
    devices = pcapy.findalldevs()
    for d in devices :
        if(d == "any"):
            devices.remove("any")
        elif(d == "lo"):
            devices.remove("lo")
        elif(d == "docker0"):
            devices.remove("docker0")
        elif(d == "dbus-system"):
            devices.remove("dbus-system")
        elif(d == "dbus-session"):
            devices.remove("dbus-session")
        elif(d == "bluetooth0"):
            devices.remove("bluetooth0")
        elif(d == "bluetooth-monitor"):
            devices.remove("bluetooth-monitor")
        elif(d == "nflog"):
            devices.remove("nflog")
        elif(d == "nfqueue"):
            devices.remove("nfqueue")

    return devices

def check_if_device_exists(name):
    devices = get_all_device()
    exist = False
    for d in devices :
        if(d == name):
            exist = True
            break
    return exist
