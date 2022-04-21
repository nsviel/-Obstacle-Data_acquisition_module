#!/bin/bash

echo -e "[\e[92mok\e[0m] Start SSH server installation"

sudo apt-get install -y openssh-server 2>&1 >/dev/null
sudo systemctl enable ssh 2>&1 >/dev/null
sudo systemctl start ssh 2>&1 >/dev/null

echo -e "[\e[92mok\e[0m] SSH server installed and running"
