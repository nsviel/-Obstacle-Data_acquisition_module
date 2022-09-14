#!/bin/sh

GREEN='\033[92m'
NC='\033[0m'

printf "${GREEN}--------------------------${NC}\n"
printf "${GREEN} Pull, build & run docker ${NC}\n"
printf "${GREEN}--------------------------${NC}\n"

cd ..
git reset --hard HEAD
git pull
cd docker
./build.sh
