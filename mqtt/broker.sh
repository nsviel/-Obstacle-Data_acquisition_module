#!/bin/bash

# Kill previous mosquitto sessions if any
echo -e "[\e[92mok\e[0m] Kill previous processes"
ps -ef | grep mosquitto | grep -v grep | awk '{print $2}' | xargs sudo  kill

# Start MQTT mosquitto session
echo -e "[\e[92mok\e[0m] Start MQTT broker"
sudo mosquitto

