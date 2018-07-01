# roboclaw testing July 1 2018
# reading both encoders but moving only one motor ok
# added setting pid for 2nd motor ok
# added moving 2nd motor seems to be running in reverse counting is negative but telling it positive

import time
import sys

port = "COM30"		# my port on desktop pc

# create callback to handle subscription
def onEncoderData(data):
    print("EncData - %s" % data);			# show for testing

# read encoders and put result in M1 and M2
def RCwait():
#   looks like n is bytes  need asci string   really just want number
   global M1, M2
   
   n1 = ( (rc.readEncoderM1()),'utf-8') 	# read encoders and fix bytes
   n2 = ( (rc.readEncoderM2()),'utf-8') 
#   print( 'M1= %s   M2= %s'  % (n1, n2 ))	# for testing show me

   new = str( n1 [0] )				# change to string
   strlen = ( sys.getsizeof( new) )	# need to find length of string
#   print "rc wait M1 ", new, "length ", strlen	# for testing show me
   if (new[ 4 ] == '1') and (strlen > 0):		# only looking for M1
      encnum = new[ 6:strlen ]		# slicing operator
#      print encnum					# for testing show me
      M1 = int( encnum )
#      if M1 != 0:					# do we have real number
#        print "M1=",M1
        
   new = str( n2 [0] )				# change to string
   strlen = ( sys.getsizeof( new) )	# need to find length of string
#   print "rc wait M1 ", new, "length ", strlen	# for testing show me
   if (new[ 4 ] == '2') and (strlen > 0):		# only looking for M2
      encnum = new[ 6:strlen ]		# slicing operator
#      print encnum					# for testing show me
      M2 = int( encnum )
#      if M2 != 0:					# do we have real number
#        print "M2=", M2

# reset encoders
def EncReset():
  rc.resetEncoders()
  time.sleep( .015 )			# .01 = 10ms this delay is NEEDED!
  print( 'reset encoders M1=%s  M2=%s' % (rc.readEncoderM1(), rc.readEncoderM2() ))

print( "roboclaw testing" )
# make sure we have a python service named 'python'
Runtime.start('python','Python')

# create our roboclaw
rc = Runtime.start('rc','RoboClaw')

# allow buffering of commands - default false  I dont see any diff
#rc.setBuffer(True)
rc.setBuffer( False )

# start encoder 1 and 2
rc.startEncoderM1()
time.sleep( .01 )
rc.startEncoderM2()
time.sleep( .01 )

# rc.setSampleRate( 8000 )		# does not work

# subscribe to encoder events
# python.subscribe( rc, 'publishEncoderData' )

# connect it
rc.connect(port)

# velocity and pid constants M1
d = 10
p = 20
i = 10
qpps = 2200			# works at 2200
deadzone = 10
minPos = -500000
maxPos =  500000
# speed accel and deccel
speed = 2000	
accel = 1000
deccel = 1000
# set all the constants for pid qpps min and max
print('setting constants M1')
rc.setPidQppsDeadzoneMinMaxM1(p, i, d, qpps, deadzone, minPos, maxPos)
time.sleep(.02)
print('pid now reads %s' % rc.readPidM1())

# velocity and pid constants M2
d = 10
p = 20
i = 10
qpps = 7800	
deadzone = 8
minPos = -500000
maxPos =  500000
# speed accel and deccel
speed = 5000	
accel = 2000
deccel = 2000
# set all the constants for pid qpps min and max
print('setting constants M2')
rc.setPidQppsDeadzoneMinMaxM2(p, i, d, qpps, deadzone, minPos, maxPos)
time.sleep(.02)
print('pid now reads %s' % rc.readPidM2())

# reset the encoders
EncReset()

# initial position
global M1, M2
pos = 1111
M1 = 0
# move motor M1
rc.driveSpeedAccelDeccelPosM1(speed, accel, deccel, pos)
for s in range( 0, 1000 ):
  M1old = M1				# save current positon
  sleep( .5 )
  RCwait()				# get new position
  if abs(M1) > 0:			# seems to set at 0 for awhile and we dont want to stop at 0
    if abs(M1) == abs(M1old):	# are the positons the same?
      print "m1=",M1,"  M1old=",M1old  # yes then we are done
      break
time.sleep( 1 )     		# time for motor to stop 
# see how close we came
print( 'motor target %s motor actual %s  loops %s' % (pos, rc.readEncoderM1(), s) )

pos = 3210
M2 = 0
# move motor M2
rc.driveSpeedAccelDeccelPosM2(speed, accel, deccel, pos)
for s in range( 0, 1000 ):
  M2old = M2				# save current positon
  sleep( .5 )
  RCwait()				# get new position
  if abs(M2) > 0:			# seems to set at 0 for awhile
    if abs(M2) == abs(M2old):	# are the positons the same?
      print "m2=",M2,"  M2old=",M2old  # yes then we are done
      break
time.sleep( 1 )     		# time for motor to stop 
# see how close we came
print( 'motor target %s motor actual %s  loops %s' % (pos, rc.readEncoderM2(), s) )

EncReset()

# change pos
pos = -1234
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
time.sleep( 1 )       		# time for motor to stop       
# see how close we came
print('motor target %s motor actual %s' % (pos, rc.readEncoderM1()))
time.sleep( .02 )

EncReset()

# continue polling encoder for .1 seconds
sleep( .1 )
rc.stopPolling()
print( "End roboclaw test" )

