#---------------------------------------------
from src.param import param_py
from src.interface import capture
from src.interface import lidar


def manage_command(lvl1, lvl2, lvl3):
    if(lvl1 == "hubium" and lvl2 == "ip"):
        param_py.state_py["hubium"]["ip"] = lvl3
    elif(lvl1 != None and lvl1 != "null"):
        param_py.state_py[lvl1][lvl2] = lvl3
        if(str(lvl2) == "device"):
            capture.restart_capture()
        if(str(lvl2) == "ip"):
            capture.restart_capture()
        if(str(lvl2) == "speed"):
            lidar.start_l1_motor()
            lidar.start_l2_motor()
    elif(lvl1 == "null"):
        if(str(lvl2) == "lidar_1"):
            if(str(lvl3) == "start"):
                lidar.start_l1_motor()
            if(str(lvl3) == "stop"):
                lidar.stop_l1_motor()
        if(str(lvl2) == "lidar_2"):
            if(str(lvl3) == "start"):
                lidar.start_l2_motor()
            if(str(lvl3) == "stop"):
                lidar.stop_l2_motor()
