#---------------------------------------------

# State
state_py = {}
state_net = {}

# Thread
run_loop = True;
run_thread_con = False
run_thread_perf = False
run_thread_l1 = False
run_thread_l2 = False
run_thread_net = False

# Socket
sock_client = None
sock_client_ok = False
sock_server_port = 1

# HTTP
https_server = None
http_server_daemon = None

# Path
path_state_py = "state/state_py.json"
path_state_net = "state/state_net.json"
path_config = "param/config.json"
