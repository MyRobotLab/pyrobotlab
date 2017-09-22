#!/bin/bash

cd /home/pi
./stop_harry.sh
rm -rf mrl
mkdir mrl
cd mrl
wget "http://34.201.4.170/deploy/develop/myrobotlab.jar"
java -jar myrobotlab.jar -install


