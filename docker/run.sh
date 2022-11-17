#!/bin/sh

sudo docker run -it \
     -p 314:314 \
     -p 6970:6970 \
     pywardium
