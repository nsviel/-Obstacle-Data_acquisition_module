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
import shlex
import dpkt
import tempfile

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
    pcap_reader(socket)

def check_device(lidar_device):
    device_ok = device.check_if_device_exists(lidar_device)
    if(device_ok == False):
        terminal.addLog("error", "Device \033[1;32m%s\033[0m does not exists"% lidar_device)
    return device_ok
def start_capture(socket, lidar_ID, dest_port):
    lidar_device = param_capture.state_ground[lidar_ID]["info"]["device"]
    connected = param_capture.state_ground[lidar_ID]["info"]["connected"]
    activated = param_capture.state_ground[lidar_ID]["info"]["activated"]
    dest_ip = param_capture.state_edge["hub"]["info"]["ip"]

    if(connected and device_ok):
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
    dest_ip = param_capture.state_edge["hub"]["info"]["ip"]
    dest_port = param_capture.state_edge["hub"]["socket"]["server_l1_port"]
    path = param_capture.path_pcap


    # Get the initial file size
    initial_file_size = os.path.getsize(path)
    terminal.addDaemon("#", "ON", "LiDAR 1 pcap")
    param_capture.run_thread_pcap = True

    while param_capture.run_thread_pcap:
        # Run tcpdump and read the packet details, redirecting output to subprocess.PIPE
        absolute_path = os.path.abspath(path)
        command = "tcpdump -r {} -w {}".format(shlex.quote(absolute_path), "aa.dat")

        # Run the command and redirect both stdout and stderr to null devices
        with open(os.devnull, 'w') as null_device:
            process = subprocess.Popen(command, stdout=null_device, stderr=null_device, shell=True)
            process.wait()

        # Open the temporary pcap file for reading
        with open("aa.dat", 'rb') as pcap_file:
            # Loop over each packet and process it continuously
            pcap = dpkt.pcap.Reader(pcap_file)

            start_time = time.time()
            total_bytes = 0

            for ts, buf in pcap:
                packet = bytes(buf)
                socket.socket.sendto(packet, (dest_ip, dest_port))
                total_bytes += len(packet)
                time.sleep(0.0000001)

            # Calculate throughput in bytes per second
            end_time = time.time()
            elapsed_time = end_time - start_time
            throughput_bps = total_bytes / elapsed_time
            throughput_mbps = throughput_bps / 1_000_000
            param_capture.state_ground["lidar_1"]["throughput"]["value"] = throughput_mbps

            # Wait for the process to complete (optional)
            process.terminate()

    terminal.addDaemon("#", "OFF", "LiDAR pcap")
