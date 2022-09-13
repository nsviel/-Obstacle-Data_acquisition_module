#!/bin/sh

cd ..
git reset --hard HEAD
git pull
cd docker
./build.sh
./run.sh
