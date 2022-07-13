#! /usr/bin/python
#---------------------------------------------


# State
state_py = {}

# Thread
run_loop = True;
run_thread_con = False
run_thread_l1 = False
run_thread_l2 = False

# Socket
sock_connected = False
sock_client = None
socket_server = 999
http_verbose = False

# Path
path_state_py = "state/state_py.json"
path_config = "param/config.json"
