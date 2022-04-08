#!/bin/bash

#Parameters
broker_ip=127.0.0.1
broker_topic=ai_obstacle

#display parameters
echo -e "[\e[92mok\e[0m] Subscribe to broker \e[32m$broker_ip\e[0m at \e[32m$broker_topic\e[0m topic"

# Subscribe localhost broker at Obstacle topic
mosquitto_sub -h $broker_ip -t $broker_topic

