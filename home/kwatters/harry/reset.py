#!/usr/bin/python


import serial
from time import sleep
##################################################
#
##################################################
port = "/dev/ttyACM0"
baud = 57600

# Open the serial port.
ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
  print(ser.name + ' is open...')


port = "/dev/ttyACM1"
# Open the serial port.
ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
  print(ser.name + ' is open...')

