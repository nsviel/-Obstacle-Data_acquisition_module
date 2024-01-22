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
import time

thread_l2 = None
thread_l1 = None
thread_pcap = None


def start_lidar_capture():
    thread_l1 = threading.Thread(target = start_l1_capture)
    thread_l2 = threading.Thread(target = start_l2_capture)
    thread_pcap = threading.Thread(target = start_pcap_capture)
    #thread_l1.start()
    #thread_l2.start()
    thread_pcap.start();
def stop_lidar_capture():
    param_capture.run_thread_l1 = False
    param_capture.run_thread_l2 = False
    param_capture.run_thread_pcap = False
    if thread_l1 is not None:
        thread_l1.join()
    if thread_l2 is not None:
        thread_l2.join()
    if thread_pcap is not None:
        thread_pcap.join()
def restart_lidar_capture():
    terminal.addDaemon("#", "restart", "LiDAR capture")
    stop_lidar_capture()
    start_lidar_capture()

def start_l1_capture():
    dest_port = param_capture.state_edge["hub"]["socket"]["server_l1_port"]
    socket = socket_client.Socket_client()

    # wait for lidar connection
    connected = False
    while not connected:
        connected = param_capture.state_ground["lidar_1"]["info"]["connected"]
        time.sleep(0.5)

    # Check device
    device_ok = check_device(device)
    start_capture(socket, "lidar_1", dest_port)
def start_l2_capture():
    l2_device = param_capture.state_ground["lidar_2"]["info"]["device"]
    l2_port = param_capture.state_ground["capture"]["socket"]["server_l2_port"]
    socket = socket_client.Socket_client()

    # wait for lidar connection
    connected = False
    while not connected:
        connected = param_capture.state_ground["lidar_2"]["info"]["connected"]
        time.sleep(0.5)

    # Check device
    device_ok = device.check_if_device_exists(l2_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% l2_device)
        return

    # Start capture
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
def start_pcap_capture():
    socket = socket_client.Socket_client()

    # loop check if lidar 1 & lidar 2 are not connected
    l1_connected = False
    l2_connected = False
    while not l1_connected and l2_connected:
        l1_connected = param_capture.state_ground["lidar_1"]["info"]["connected"]
        l2_connected = param_capture.state_ground["lidar_2"]["info"]["connected"]
        time.sleep(0.5)

    # Run pcap reading
    pcap_reader(socket)

def check_device(lidar_device):
    device_ok = device.check_if_device_exists(lidar_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% lidar_device)
    return device_ok
def start_capture(socket, lidar_ID, dest_port):
    lidar_device = param_capture.state_ground[lidar_ID]["info"]["device"]
    simulated = param_capture.state_ground[lidar_ID]["info"]["simulated"]
    connected = param_capture.state_ground[lidar_ID]["info"]["connected"]
    activated = param_capture.state_ground[lidar_ID]["info"]["activated"]
    dest_ip = param_capture.state_edge["hub"]["info"]["ip"]

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
                    socket.socket.sendto(packet, (dest_ip, dest_port))
                    if(len(packet) == 1248):
                        param_capture.state_ground[lidar_ID]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "%s: [\033[1;32m%s\033[0m] packets"%{lidar_ID, param_capture.state_ground["lidar_2"]["packet"]["value"]})
        terminal.addDaemon("#", "OFF", "%s capture"% lidar_ID)
def pcap_reader(socket):
    l1_connected = param_capture.state_ground["lidar_1"]["info"]["connected"]
    l2_connected = param_capture.state_ground["lidar_2"]["info"]["connected"]
    dest_ip = param_capture.state_edge["hub"]["info"]["ip"]
    dest_port = param_capture.state_edge["hub"]["socket"]["server_l1_port"]
    path = param_capture.path_pcap


    # Get the initial file size
    initial_file_size = os.path.getsize(path)
    terminal.addDaemon("#", "ON", "LiDAR 1 pcap")
    param_capture.run_thread_pcap = True

    try:
        while param_capture.run_thread_pcap:
            # Run tcpdump and read the packet details, redirecting output to subprocess.PIPE
            absolute_path = os.path.abspath(path)
            process = subprocess.Popen(['tcpdump', '-r', absolute_path, '-n', '-v', '-tttt', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Loop over each line (packet) and process it continuously
            while param_capture.run_thread_pcap:

                # loop check if lidar 1 & lidar 2 are not connected
                while not l1_connected and l2_connected:
                    time.sleep(0.5)

                # Read a single line (packet) from the subprocess output
                line = process.stdout.readline()
                packet = line.strip()
                #print(len(packet))

                if not packet:
                    # If there's no more output, break the inner loop
                    break

                if packet is not None:
                    socket.socket.sendto(packet.encode(), (dest_ip, dest_port))
                    if len(packet) == 1248:
                        param_capture.state_ground["lidar_1"]["packet"]["value"] += 1
                        terminal.addCstLog("cap", "LiDAR 2: [\033[1;32m%s\033[0m] packets" % param_capture.state_ground["lidar_2"]["packet"]["value"])

            # Ensure the tcpdump process is terminated when the inner loop is done
            process.terminate()

            # Reset the file position to the beginning after reaching the end
            with open(path, 'rb') as file:
                file.seek(initial_file_size)
    finally:
        # Ensure the tcpdump process is terminated when the loop is done
        process.terminate()

        # Reset the file position to the beginning after reaching the end
        with open(path, 'rb') as file:
            file.seek(initial_file_size)

    terminal.addDaemon("#", "OFF", "LiDAR pcap")
