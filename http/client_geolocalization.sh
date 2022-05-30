#!/bin/bash

echo -e "[\e[92m--- Client for HTTP geolocalization post ---\e[0m]"


while true
do
   curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'name=cMoa' -d 'geolocalization=alaska' localhost:8888
   sleep 1
done

