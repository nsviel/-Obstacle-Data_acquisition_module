#/bin/bash!

#kill program
kill -9 $(ps -A | grep python | awk '{print $1}')
