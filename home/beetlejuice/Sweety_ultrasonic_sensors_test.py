# variables dependent on your setup

boardType = "atmega2560"  # atmega168 | atmega328p | atmega2560 | atmega1280 | atmega32u4
comPort = "COM8" # com4 for atmega328 com8 for mega2560
BtrigPin = 22
BechoPin = 23
BLtrigPin = 24
BLechoPin = 25
BRtrigPin = 26
BRechoPin = 27
FLtrigPin = 28
FLechoPin = 29
FtrigPin = 30
FechoPin = 31
FRtrigPin = 32
FRechoPin = 33

# start Arduino service named arduino
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.setBoard(boardType) # atmega168 | mega2560 | etc
arduino.connect(comPort)

# Start UltrasonicSensor named sr04
sr1 = Runtime.createAndStart("F", "UltrasonicSensor")
sr1.attach( arduino, comPort, FtrigPin, FechoPin)
sr2 = Runtime.createAndStart("FL", "UltrasonicSensor")
sr2.attach( arduino, comPort, FLtrigPin, FLechoPin)
sr3 = Runtime.createAndStart("FR", "UltrasonicSensor")
sr3.attach( arduino, comPort, FRtrigPin, FRechoPin)
sr4 = Runtime.createAndStart("B", "UltrasonicSensor")
sr4.attach( arduino, comPort, BtrigPin, BechoPin)
sr5 = Runtime.createAndStart("BL", "UltrasonicSensor")
sr5.attach( arduino, comPort, BLtrigPin, BLechoPin)
sr6 = Runtime.createAndStart("BR", "UltrasonicSensor")
sr6.attach( arduino, comPort, BRtrigPin, BRechoPin)


def publishRange(myRange):
  print myRange # call back - we will now setup the listener
 
# sr04.arduino.setLoadTimingEnabled(true); # < you can look at the load timings of the duino with this
# sr04.arduino.setLoadTimingEnabled(false);
 
#sr04.addPublishRangeListener(python);
#  IMPORTANT - I've added my python service as a listener
# SO I BETTER HAVE a def publishRange(data) somewhere

sr1.startRanging() # start ranging for 10 seconds

sr2.startRanging() # start ranging for 10 seconds
sr3.startRanging() # start ranging for 10 seconds
sr4.startRanging() # start ranging for 10 seconds
sr5.startRanging() # start ranging for 10 seconds
sr6.startRanging() # start ranging for 10 seconds
sleep(10)
sr1.stopRanging();
sr2.stopRanging();
sr3.stopRanging();
sr4.stopRanging();
sr5.stopRanging();
sr6.stopRanging();
"""
# blocking range
duration = sr1.ping()
print "sr1 duration : "
print duration
myRange = sr1.range()
print "sr1 range : "
print myRange

duration = sr1.ping()
print "sr2 duration : "
print duration
myRange = sr1.range()
print "sr2 range : "
print myRange

duration = sr1.ping()
print "sr3 duration : "
print duration
myRange = sr1.range()
print "sr3 range : "
print myRange

duration = sr1.ping()
print "sr4 duration : "
print duration
myRange = sr1.range()
print "sr4 range : "
print myRange

duration = sr1.ping()
print "sr5 duration : "
print duration
myRange = sr1.range()
print "sr5 range : "
print myRange

duration = sr1.ping()
print "sr6 duration : "
print duration
myRange = sr1.range()
print "sr6 range : "
print myRange

"""
