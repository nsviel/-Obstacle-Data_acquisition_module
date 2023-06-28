#---------------------------------------------
from src.param import param_capture
from src.connection.HTTPS import https_client_fct
from src.utils import terminal



#Test module_edge HTTP connection
def test_hu_con():
    [ip, port] = https_client_fct.network_info("edge")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_hu_con.hu_has_been_deco):
        test_hu_con.hu_has_been_co = True
        test_hu_con.hu_has_been_deco = False
        terminal.addConnection("edge", "on")
        param_capture.state_capture["edge"]["connected"] = True
    elif(connected == False and test_hu_con.hu_has_been_co):
        test_hu_con.hu_has_been_co = False
        test_hu_con.hu_has_been_deco = True
        terminal.addConnection("edge", "off")
        param_capture.state_capture["edge"]["connected"] = False

test_hu_con.hu_has_been_co = False
test_hu_con.hu_has_been_deco = True
