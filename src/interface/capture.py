#---------------------------------------------
from src.param import param_capture
from src.connection.SOCK import socket_client
from src.interface import device
from src.connection import connection
from src.utils import terminal

import threading
import pcapy
import re
import subprocess
import os


def start_lidar_capture():
    thread_l1 = threading.Thread(target = start_l1_capture)
    thread_l2 = threading.Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()
def stop_lidar_capture():
    param_capture.run_thread_l1 = False
    param_capture.run_thread_l2 = False
    param_capture.run_thread_lidar_simulation = False
def restart_lidar_capture():
    terminal.addDaemon("#", "restart", "LiDAR capture")
    stop_lidar_capture()
    start_lidar_capture()

def start_l2_capture():
    l2_device = param_capture.state_ground["lidar_2"]["info"]["device"]
    l2_port = param_capture.state_ground["capture"]["socket"]["server_l2_port"]
    socket = socket_client.Socket_client()
    simulated = param_capture.state_ground["lidar_1"]["info"]["simulated"]

    # Check device
    device_ok = device.check_if_device_exists(l2_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l2_device)
        return

    # Start capture
    connected = param_capture.state_ground["lidar_2"]["info"]["connected"]
    if(connected and device_ok):
        param_capture.state_ground["lidar_2"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_2"]["motor"]["running"] = True
        param_capture.run_thread_l2 = True
        ip = param_capture.state_edge["hub"]["info"]["ip"]
        port = param_capture.state_edge["hub"]["socket"]["server_l2_port"]

        listener = pcapy.open_live(l2_device, 1500, 0 , 1)
        filter = "udp port 2368 or 2369 or port 8308 or port 8309"
        listener.setfilter(filter)
        terminal.addDaemon("#", "ON", "LiDAR 2 capture on [\033[1;32m%s\033[0m]"%l2_device)

        while param_capture.run_thread_l2 and param_capture.state_ground["lidar_2"]["info"]["connected"]:
            if(param_capture.state_ground["lidar_2"]["info"]["activated"]):
                (header, packet) = listener.next()
                if(packet != None):
                    socket.socket.sendto(packet, (ip, port))
                    if(len(packet) == 1248):
                        param_capture.state_ground["lidar_2"]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_capture.state_ground["lidar_2"]["packet"]["value"])
        terminal.addDaemon("#", "OFF", "LiDAR 2 capture")

def start_l1_capture():
    port_dest = param_capture.state_edge["hub"]["socket"]["server_l1_port"]
    socket = socket_client.Socket_client()

    # Check device
    device_ok = check_device(device)
    start_capture(socket, "lidar_1", port_dest)
    start_loop_over_pcap(socket, "lidar_1", port_dest)

def check_device(lidar_device):
    device_ok = device.check_if_device_exists(lidar_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% lidar_device)
    return device_ok
def start_capture(socket, lidar_ID, port_dest):
    lidar_device = param_capture.state_ground[lidar_ID]["info"]["device"]
    simulated = param_capture.state_ground[lidar_ID]["info"]["simulated"]
    connected = param_capture.state_ground[lidar_ID]["info"]["connected"]
    activated = param_capture.state_ground[lidar_ID]["info"]["activated"]
    ip_dest = param_capture.state_edge["hub"]["info"]["ip"]

    if(connected and device_ok and simulated == False):
        param_capture.state_ground["lidar_1"]["packet"]["value"] = 0
        param_capture.state_ground["lidar_1"]["motor"]["running"] = True
        param_capture.run_thread_l1 = True

        listener = pcapy.open_live(lidar_device , 1500, 0, 1)
        filter = "udp port 2368 or 2369 or port 8308 or port 8309"
        listener.setfilter(filter)
        terminal.addDaemon("#", "ON", "%s capture on [\033[1;32m%s\033[0m]"%{lidar_ID, lidar_device})

        while param_capture.run_thread_l1 and connected:
            if(activated):
                (header, packet) = listener.next()
                if(packet != None):
                    socket.socket.sendto(packet, (ip_dest, port_dest))
                    if(len(packet) == 1248):
                        param_capture.state_ground[lidar_ID]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "%s: [\033[1;32m%s\033[0m] packets"%{lidar_ID, param_capture.state_ground["lidar_2"]["packet"]["value"]})
        terminal.addDaemon("#", "OFF", "%s capture"% lidar_ID)
def start_loop_over_pcap(socket, lidar_ID, port_dest):
    simulated = param_capture.state_ground[lidar_ID]["info"]["simulated"]
    connected = param_capture.state_ground[lidar_ID]["info"]["connected"]
    activated = param_capture.state_ground[lidar_ID]["info"]["activated"]
    ip_dest = param_capture.state_edge["hub"]["info"]["ip"]
    path = param_capture.path_pcap

    if(simulated):
        # Get the initial file size
        initial_file_size = os.path.getsize(path)
        terminal.addDaemon("#", "ON", "LiDAR 1 simulation")
        param_capture.run_thread_lidar_simulation = True

        while param_capture.run_thread_lidar_simulation:
            # Run tcpdump and read the packet details, but redirect output to subprocess.DEVNULL
            process = subprocess.Popen(['tcpdump', '-r', path, '-n', '-v', '-tttt', '-l'], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

            try:
                # Loop over each line (packet) and process it continuously
                while param_capture.run_thread_lidar_simulation:
                    line = process.stderr.readline()
                    packet = line.strip()
                    if not packet:
                        break  # Break the loop if there's no more output
                    if(packet != None):
                        socket.socket.sendto(packet.encode(), (ip_dest, port_dest))
                        if(len(packet) == 1248):
                            param_capture.state_ground["lidar_1"]["packet"]["value"] += 1
                            terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets"% param_capture.state_ground["lidar_2"]["packet"]["value"])
            finally:
                # Ensure the tcpdump process is terminated when the loop is done
                process.terminate()

            # Reset the file position to the beginning after reaching the end
            with open(path, 'rb') as file:
                file.seek(initial_file_size)
        terminal.addDaemon("#", "OFF", "LiDAR 1 simulation")
