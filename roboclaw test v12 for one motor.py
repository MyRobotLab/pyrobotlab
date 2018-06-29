# roboclaw testing June 28 2018
# when only having one encoder on it works
# publishing 2nd encoder the routine fails to end

import time
import sys

# constants
port = "COM30"
#n = 0

# make sure we have a python service named 'python'
Runtime.start('python','Python')

# create our roboclaw
rc = Runtime.start('rc','RoboClaw')

# reset the encoders
rc.resetEncoders()
time.sleep( .020 )			# seems to need 20ms

# allow buffering of commands - default false  I dont see any diff
rc.setBuffer(True)
#rc.setBuffer( False )
time.sleep(.01)

# start encoder 1 and 2 publishing
rc.startEncoderM1()
time.sleep( .01 )
#rc.startEncoderM2()
#time.sleep( .01 )

# create callback to handle subscription
def onEncoderData(data):
    global n
#    print("EncData - %s" % data);			# show for testing
    n = (data, 'utf-8')
    
def RCwait():
#   looks like n is bytes  need asci string   really just want number
   global n
   global M1
   global M2
   strlen = ( sys.getsizeof( n ) )
#   print "wiat routine encoder=", n, "length=", strlen 
   a = ( n [0] )
   new = str(a)
#   print "rc wait new ", new
   strlen = ( sys.getsizeof( new) )	# need to find end of string
   if new[ 4 ] == '1':				# only looking for M1
      encnum = new[ 6:strlen ]		# slicing operator
#      print encnum
      M1 = int( encnum )
      if M1 != 0:
        print "** M1=",M1
#   if new[ 4 ] == '2':				# only looking for M2
#      encnum = new[ 6:strlen ]		# slicing operator
#      print encnum
#      M2 = int( encnum )
#      if M2 != 0:
#        print "(**** M2=",M2
   
# rc.setSampleRate( 8000 )		# does not work

# subscribe to encoder events
python.subscribe( rc, 'publishEncoderData' )

# connect it
rc.connect(port)

# velocity and pid constants M1
d = 10
p = 20
i = 10
qpps = 2300			# works at 2200
deadzone = 10
minPos = -500000
maxPos =  500000
# speed accel and deccel
speed = 2000	
accel = 1000
deccel = 1000

# set all the constants for pid qpps min and max
print('setting constants')
rc.setPidQppsDeadzoneMinMaxM1(p, i, d, qpps, deadzone, minPos, maxPos)
time.sleep(.02)
print('pid now reads %s' % rc.readPidM1())
time.sleep( .02 )

# start publishing encoder data
rc.startEncoderM1()
time.sleep( .02 )

print( 'encoders reset' )  	# reset the encoders
rc.resetEncoders()
time.sleep( .02 )			# .01 = 10ms
print( 'initial encoder reads %s' % rc.readEncoderM1() )
time.sleep(.02)

# initial position
global M1, M2
pos = 2222
M1 = 0

# move the motor
rc.driveSpeedAccelDeccelPosM1(speed, accel, deccel, pos)
for s in range( 0, 1000 ):
  M1old = M1
  sleep( .5 )
  RCwait()
  if abs(M1) > 0:
    if abs(M1) == abs(M1old):
      print "m1=",M1,"  M1old=",M1old
      break
time.sleep( 5 )      
# see how close we came
print('motor target %s motor actual %s' % (pos, rc.readEncoderM1()))
time.sleep( .02 )

print( 'encoders reset' )  	# reset the encoders
rc.resetEncoders()
time.sleep( .02 )			# .01 = 10ms
print( 'initial encoder reads %s' % rc.readEncoderM1() )
time.sleep(.02)

# change pos
pos = -3333
M1 = 0

# move in the other direction
rc.driveSpeedAccelDeccelPosM1(speed, accel, deccel, pos)
for s in range( 0, 1000 ):
  M1old = M1
  sleep( .5 )
  RCwait()
  if abs(M1) > 0:
    if abs(M1) == abs(M1old):
      print "m1=",M1,"  M1old=",M1old
      break
time.sleep( 5 )         
# see how close we came
print('motor target %s motor actual %s' % (pos, rc.readEncoderM1()))
time.sleep( .02 )

# reset the encoders
#rc.resetEncoders()
#time.sleep( .020 )			# seems to need 20ms

# continue polling encoder for .1 seconds
sleep( .1 )
rc.stopPolling()
print( "End roboclaw test" )

