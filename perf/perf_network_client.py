#---------------------------------------------
from param import param_py
from threading import Thread
from src import signal

import multiprocessing as mp

import iperf3
import time
import os


def start_daemon():
    thread_con = Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_py.run_thread_net = False

def thread_perf_server():
    param_py.run_thread_net = True
    while param_py.run_thread_net :
        ip = param_py.state_py["hubium"]["ip"]
        port = param_py.state_py["hubium"]["iperf_port"]
        process_net = mp.Process(target = process_perf_server, args = (ip, port))
        process_net.start()
        process_net.join()
        time.sleep(1)

def process_perf_server(ip, port):
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = ip
    client.port = port
    client.blksize = 1240
    client.protocol = 'udp'
    client.verbose = False
    client.json_output = True
    result = client.run()
    print_result(client, result)
    del client

def print_result(client, result):
    if(result != None and result.error == None):
        print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
        print('')
        print('Test completed:')
        print('  started at         {0}'.format(result.time))
        print('  bytes transmitted  {0}'.format(result.bytes))
        print('  jitter (ms)        {0}'.format(result.jitter_ms))
        print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

        print('Average transmitted data in all sorts of networky formats:')
        print('  bits per second      (bps)   {0}'.format(result.bps))
        print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
        print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
        print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
        print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
