#---------------------------------------------
from src.param import param_py
from src.HTTPS import https_client_fct


#Test Hubium HTTP connection
def test_hu_con():
    [ip, port] = https_client_fct.network_info("hu")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        param_py.state_py["hubium"]["connected"] = True
    else:
        param_py.state_py["hubium"]["connected"] = False
