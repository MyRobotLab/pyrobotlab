#!/bin/bash 

cd /home/pi/mjpg-streamer
export LD_LIBRARY_PATH="$(pwd)"


# start the left eye
# ./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -y -r 640x480 -f 2" -o "./output_http.so -p 8080 -w /usr/local/www"
./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -y -r 320x240 -f 2" -o "./output_http.so -p 8080 -w /usr/local/www"
# ./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -y -r 160x120 -f 10" -o "./output_http.so -p 8080 -w /usr/local/www"














