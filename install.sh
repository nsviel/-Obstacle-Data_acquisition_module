#/bin/bash!

#Install dependancies
sudo apt install -y python3 python3-pip python3-scapy python3-pcapy libiperf0 iputils-ping
sudo python3 -m pip install scapy requests pandas psutil iperf3
pip install psutil
