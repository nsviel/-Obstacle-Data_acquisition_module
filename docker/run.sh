#!/bin/sh

docker run -it -p 2369 --network host pywardium /bin/bash

#!/bin/sh

./build.sh

xhost +
docker run \
    -it
    --network host
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device="/dev/dri:/dev/dri" \
    --env="DISPLAY=:1" \
    pywardium bash
xhost -
