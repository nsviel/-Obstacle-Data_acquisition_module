#!/bin/sh

GREEN='\033[92m'
NC='\033[0m'

printf "${GREEN}--------------${NC}\n"
printf "${GREEN} Pull & build ${NC}\n"
printf "${GREEN}--------------${NC}\n"

git reset --hard HEAD
git pull
cd docker
./build.sh
cd ..

printf "${GREEN}---------${NC}\n"
printf "${GREEN} Updated ${NC}\n"
printf "${GREEN}---------${NC}\n"
