#---------------------------------------------
from src.param import param_capture
from src.connection.HTTPS.client import https_client_fct
from src.utils import terminal



#Test module_edge HTTP connection
def test_connection_edge():
    [ip, port] = https_client_fct.network_info("edge")
    connected = https_client_fct.send_https_ping(ip, port)
    param_capture.state_ground["interface"]["edge"]["http_connected"] = connected
    if(connected == True and test_connection_edge.hu_has_been_deco):
        test_connection_edge.hu_has_been_co = True
        test_connection_edge.hu_has_been_deco = False
        terminal.addConnection("edge", "on")
    elif(connected == False and test_connection_edge.hu_has_been_co):
        test_connection_edge.hu_has_been_co = False
        test_connection_edge.hu_has_been_deco = True
        terminal.addConnection("edge", "off")

test_connection_edge.hu_has_been_co = False
test_connection_edge.hu_has_been_deco = True
