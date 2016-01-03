# testing serial commands to eddie control board
# trying to read analog votages on eddie control board every time not just sometimes
# the problem was extra characaters in the input receive buffer
# Dec 16 2014

import time

ser = Runtime.start("serial","Serial")
ser.connect("COM4",115200, 8, 1, 0)

#lights on in head  each write command get a 0x0D cr returned to input buffer
# and the input buffer sometimes has ERROR cr
print("lights on")
lightpin = 1
for i in range(1,8):
 ser.write("HDLT " + str(lightpin) + "\r")
#shift bit for next light   each bit runs one light
 lightpin = lightpin << 1
 time.sleep(.25)
ser.write("HDLT 0\r")
print("lights off")

#changing delay after light command seems to make no difference in buffer extra bytes
time.sleep(1)

#send command to read 8 channel atod
ser.write("ADC\r")

#remove any junk in input buffer on serial port
#this was solved by adding a character to the start of data being sent that I could reconize
code = 1
codeb = 1
#looking for J which is the start of the ADC data
#every command to the eddie bd gets some kind of characters sent back
for i in range(1,30): 
  code = ser.read()
#  print("junk=" + chr(code) + " " + str(code))
  if(code == 0x41) and (codeb == 0x34):
#       print("found end")
       break
  codeb = code

# next sleep line does not appear to make a differance tied .1 to 10 with same results
time.sleep(1)

#read data from ADC and end when you see cr
serdata = ""
code=1
for i in range(0,31):
    code = (ser.read() & 0xFF)
    serdata += chr(code)
    if ((code == 0x0D)):
#      print("exit")
      break
print("raw data=" + str(serdata))

#get right values from character stream
#the calculation figures out to be .0039volt per count or 1/.0039=256.4
#using that number shows a voltage that is lower than I see on a voltmeter
#so I adjusted the divisor to match my meter and then round it to 2 places
volts1 = (int((serdata[28]), base=16)) * 256
volts = (int((serdata[29]), base=16)) * 16
volts = (volts1 + volts + (int((serdata[30]), base=16))) / 238.2
print("batt =" + str(round(volts,2)) + "VDC")

# 3 I/R sensors on platform measure from 10 to 80cm or 3.94 to 31.5inches
# ADC is 12 bit or FFF but eddie bd only uses 10 bits or 1024 counts
# note spec says out voltage at 80cm is .25 to .55v and at 10cm is 1.85 to 2.7v
# so these are more like on off for set distance not very accurate for real distance
# 30cm or 11.8 inches should be good starting point or about 1 volt for center
# may want closer for sides    want to be able to go through doors
# 1 volt should be around 1024 cnts/5v or about 205 counts
# remember higher voltage is closer so above 205 is to close

distcen = (int((serdata[0]), base=16)) * 256
distcen1 = (int((serdata[1]), base=16)) * 16
distcen = (distcen + distcen1 + (int(serdata[2], base=16)))
print("IR right =" + str(distcen))
if(distcen > 205):
  print("close right")
  
distcen = (int((serdata[4]), base=16)) * 256
distcen1 = (int((serdata[5]), base=16)) * 16
distcen = (distcen + distcen1 + (int(serdata[6], base=16)))
print("IR center =" + str(distcen))
if(distcen > 205):
  print("close center")

distcen = (int((serdata[8]), base=16)) * 256
distcen1 = (int((serdata[9]), base=16)) * 16
distcen = (distcen + distcen1 + (int(serdata[10], base=16)))
print("IR left =" + str(distcen))
if(distcen > 205):
  print("close left")

# print("done here")
