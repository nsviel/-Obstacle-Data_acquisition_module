#!/bin/bash

ip_dest=10.201.20.106

echo -e "[\e[92mok\e[0m]" Connection SSH with "[\e[92m$ip_dest\e[0m]"
ssh -vtCX -o ConnectTimeout=1 ns@$ip_dest 'export MESA_GL_VERSION_OVERRIDE=3.3; bash -l'
echo -e "[\e[92mok\e[0m]" Connection SSH terminated


