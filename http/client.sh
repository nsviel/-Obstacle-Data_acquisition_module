#!/bin/bash

echo -e "[\e[92m--- Client for HTTP image receiving ---\e[0m]"


while true
do
   curl localhost:8888 --output ./image
   sleep 1
done

