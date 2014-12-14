# testing serial commands to eddie control board
# trying to read analog votages on eddie control board evry time not just once

import time
#import serial

ser = Runtime.start("serial","Serial")
ser.connect("COM4",115200, 8, 1, 0)

#lights on in head cycle
lightpin = 1
for i in range(1,8):
 ser.write("HDLT " + str(lightpin) + "\r")
 lightpin = lightpin << 1
 print(str(lightpin))
 time.sleep(.25)
ser.write("HDLT 0\r")
print("lights off")

#remove any junk in input buffer on serial port before issuing command
code = 1
while (ser.read() != 0):
   code = ser.read()
   print("junk=" + chr(code) + " " + str(code))

# need ser.flushInput()
ser.write("ADC\r")
time.sleep(1)
serdata = ""
code=1
for i in range(1,45):
#    print( chr(serial.read()))
    code = ser.read()
    code = (code & 0xFF)
#    print("read " + chr(code))
    serdata += chr(code)
    if ((code == 0x0D)):
      print("exit")
      break
print("raw data=" + str(serdata))

volts1 = (int((serdata[28]), base=16)) * 256
volts = (int((serdata[29]), base=16)) * 16
volts = (volts1 + volts + (int((serdata[30]), base=16))) / 256.4
print("batt =" + str( volts) + "VDC")
if (volts < 10 ):
    i01.mouth.speak("danger battery low")

distcen = (int((serdata[0]), base=16)) * 256
distcen1 = (int((serdata[1]), base=16)) * 16
distcen = (1000 - (distcen + distcen1 + (int(serdata[2], base=16)))) / 27
print("IR right =" + str(distcen) + "in")
if (distcen < 10 ):
  i01.mouth.speak("danger right")

distcen = (int((serdata[4]), base=16)) * 256
distcen1 = (int((serdata[5]), base=16)) * 16
distcen = (1000 - (distcen + distcen1 + (int(serdata[6], base=16)))) / 27
print("IR center =" + str(distcen) + "in")
if (distcen < 12 ):
   i01.mouth.speak("danger center")

distcen = (int((serdata[8]), base=16)) * 256
distcen1 = (int((serdata[9]), base=16)) * 16
distcen = (1000 - (distcen + distcen1 + (int(serdata[10], base=16)))) / 27
print("IR left =" + str(distcen) + "in")
if (distcen < 10 ):
  i01.mouth.speak("danger left")
print("done here")
