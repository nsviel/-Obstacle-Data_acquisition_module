#/bin/bash!

#Install dependancies
sudo apt install libiperf0
sudo python3 -m pip install wheel
sudo python3 -m pip install pandas
sudo python3 -m pip install iperf3

#Start program
sudo python3 main.py
