#---------------------------------------------

# State
state_py = {}
state_perf = {}

# Thread
run_loop = True;
run_thread_con = False
run_thread_perf = False
run_thread_l1 = False
run_thread_l2 = False
run_thread_perf = False

# Socket
sock_client = None
sock_client_ok = False
sock_server_port = 1

# HTTP
https_server = None
http_server_daemon = None

# Network
has_been_connected = False
has_been_deconnected = False
interruption_time = 0

# Path
path_state_py = "src/state/state_py.json"
path_state_perf = "src/state/state_perf.json"
path_config = "src/param/config.json"
