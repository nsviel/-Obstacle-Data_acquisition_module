#---------------------------------------------
from scapy.all import *

import pcapy


def get_nb_paquet(pcap):
    nb = 0
    for pkt in pcap:
        if pkt.haslayer(UDP):
            nb += 1
    return nb
