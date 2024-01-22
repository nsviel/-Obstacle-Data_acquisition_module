#---------------------------------------------
from src.connection import connection
from src.network import network
from src.network import throughput
from src.param import param_capture


daemon_connection = connection.Connection()
daemon_network = network.Network()
daemon_throughput_l1 = throughput.Throughput("lidar_1")
daemon_throughput_l2 = throughput.Throughput("lidar_2")

def start_daemons():
    daemon_connection.start_daemon()
    daemon_network.start_daemon()
    daemon_throughput_l1.start_daemon()
    daemon_throughput_l2.start_daemon()

def stop_daemons():
    param_capture.run_thread_lidar_simulation = False
    daemon_connection.stop_daemon()
    daemon_network.stop_daemon()
    daemon_throughput_l1.stop_daemon()
    daemon_throughput_l2.stop_daemon()
    param_capture.run_thread_l1 = False
    param_capture.run_thread_l2 = False
    param_capture.run_thread_pcap = False
