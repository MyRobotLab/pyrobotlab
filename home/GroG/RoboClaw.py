import time

ser = Runtime.start( "serial","Serial" )
print ser.getPortNames()
ser.getPortNames()

port = "COM6"
# I use udev rules to always make it the same port
#port = "/dev/ftdi0"
#port = "/dev/ttyACM1"
# port = "/dev/ttyUSB0"

print( 'RoboClaw test' )

roboclaw = Runtime.start( "roboclaw", "RoboClaw" )
m1 = Runtime.start( "m1", "MotorPort" )
m2 =  Runtime.start( "m2", "MotorPort" )

m1.setPort( "m1" )
m2.setPort( "m2" )

roboclaw.connect(port)

# attach services
roboclaw.attach(m1)
roboclaw.attach(m2)

# roboclaw.resetQuadratureEncoderCounters()
# roboclaw.restoreDefaults()
m1.stop()
m2.stop()

# sleep here
time.sleep( .5 )
# read encoders
pos1 = roboclaw.readEncoderM1()
pos2 = roboclaw.readEncoderM2()
print( 'enc 1:', pos1, ' enc 2:', pos2 )

for i in range( 0, 20 ):
   m1.move( 0.1 * i )
   time.sleep( .1 )
   m2.move( 0.1 * i )
   print( 'cnt= ', i )
   time.sleep( .1 )

m1.move( 0 )
time.sleep( .01 )
m2.move( 0 )

# sleep here
time.sleep( .5 )
# read encoders
pos1 = roboclaw.readEncoderM1()
pos2 = roboclaw.readEncoderM2()
print( 'enc 1:', pos1, ' enc 2:', pos2 )

roboclaw.resetQuadratureEncoderCounters()

# sleep here
time.sleep( .5 )
# read encoders
pos1 = roboclaw.readEncoderM1()
pos2 = roboclaw.readEncoderM2()
print( 'enc 1:', pos1, ' enc 2:', pos2 )

# roboclaw.readEncoderCount()
# roboclaw.read
# roboclaw.bufferedDriveM1WithSignedSpeedAccelDeccelPosition(500,500,500,10000,1)
# roboclaw.
# time.sleep( .01 )
# roboclaw.driveM1WithSignedDutyAndAccel( 255, 255 )
# time.sleep( .01 )
