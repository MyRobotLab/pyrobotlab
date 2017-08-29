# testing jhs may 31 2016 this works on some pins on the mega board
# getting digital input back from arduino into Python
# testing with PIR sensor
# the uno board seems to think pins are type 1 and does not work

import time
import datetime

arduino = Runtime.createAndStart("arduino","Arduino")
# working test bench with mega and PIR
arduino.connect("COM8")

timespir = 0		# added so i can limit how often PIR goes off like debounce

#readDigitalPin = 2	# on mega board works sees type as 2
readDigitalPin = 12	# on mega board works sees type as 2
#readDigitalPin = 30	# on mega board does not works see type as 1
#readDigitalPin = 15	# on mega board does not work sees type as 1

# set the sampling rate 1 = fastest - 32767 = slowest
arduino.setSampleRate(8000)

arduino.addListener("publishPin", "python", "publishPin")

#note parallax pir is active high, small radio shack pir is active low
def publishPin(pin):
  global timespir
  if (pin.value == 0):
#    print pin.pin, pin.value, pin.type, pin.source
    timespir = timespir + 1	#added because it was going off to often
    if (timespir > 5):
      timespir = 0		#reset counter for pir
      print 'pin=', pin.pin, ' value=', pin.value, ' type=', pin.type, ' source=', pin.source
      print '***    some one is here    ***'
#      print( datetime.datetime.now())
      now = datetime.datetime.now()
      moment = now.time()
      print 'time:', moment.hour, ':', moment.minute, ':', moment.second
      arduino.digitalReadPollingStop(readDigitalPin)  
        
arduino.digitalReadPollingStart(readDigitalPin)
