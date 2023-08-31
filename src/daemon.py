#---------------------------------------------
from src.connection import connection
from src.network import network
from src.network import throughput


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
    daemon_connection.stop_daemon()
    daemon_network.stop_daemon()
    daemon_throughput_l1.stop_daemon()
    daemon_throughput_l2.stop_daemon()
