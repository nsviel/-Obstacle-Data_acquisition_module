#---------------------------------------------
from src.param import param_capture
import pcapy


def update_list():
    devices = get_all_device()

    cpt = 0
    param_capture.state_capture["device"].clear()
    for d in devices :
        y = {str(cpt): str(d)}
        param_capture.state_capture["device"].update(y)
        cpt = cpt + 1

def get_all_device():
    devices = pcapy.findalldevs()

    to_supress = []
    for d in devices :
        if(d == "any"):
            to_supress.append("any")
        elif(d == "lo"):
            to_supress.append("lo")
        elif(d == "docker0"):
            to_supress.append("docker0")
        elif(d == "dbus-system"):
            to_supress.append("dbus-system")
        elif(d == "dbus-session"):
            to_supress.append("dbus-session")
        elif(d == "bluetooth0"):
            to_supress.append("bluetooth0")
        elif(d == "bluetooth-monitor"):
            to_supress.append("bluetooth-monitor")
        elif(d == "nflog"):
            to_supress.append("nflog")
        elif(d == "nfqueue"):
            to_supress.append("nfqueue")

    for d in to_supress :
        devices.remove(d)

    return devices

def check_if_device_exists(name):
    devices = get_all_device()
    exist = False
    for d in devices :
        if(d == name):
            exist = True
            break
    return exist
