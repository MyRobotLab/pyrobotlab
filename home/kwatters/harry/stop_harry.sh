#!/bin/bash


echo "Kill all java processes."
killall -9 java 
sleep 1
echo "Resetting serial ports"
/home/pi/reset.py
echo "Stopped"

