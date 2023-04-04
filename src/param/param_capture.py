#---------------------------------------------

# State
state_capture = {}
state_network = {}

# Thread
run_loop = True;
run_thread_con = False
run_thread_perf = False
run_thread_l1 = False
run_thread_l2 = False
run_thread_perf = False

# Tic delay
tic_loop = 1
tic_message = 0.05
tic_connection = 0.5
tic_network = 0.5
tic_throughput = 0.05

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
path_state_capture = "src/state/state_capture.json"
path_state_network = "src/state/state_network.json"
path_config = "config.json"
