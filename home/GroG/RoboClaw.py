# constants
port = "COM4"

# velocity and pid constants
d = 0
p = 15000
i = 46
qpps = 56000
deadzone = 500
minPos = 0
maxPos = 40000000

# speed accel and deccel
speed = 1000000
accel = 1000000
deccel = 1000000

# initial position
pos = 0

# make sure we have a python service named 'python'
Runtime.start('python','Python')

# create our roboclaw
rc = Runtime.start('rc','RoboClaw')

# reset the encoders
# rc.resetEncoders()

# set an encoder to a value
rc.setEncoderM1(100000)

# allow buffering of commands - default false
rc.setBuffer(True)

# start encoder 1 publishing
rc.startEncoderM1()

# create callback to handle subscription
def onEncoderData(data):
    print("onEncoderData - %s" % data);

# subscribe to encoder events
python.subscribe(rc, 'publishEncoderData')

# connect it
rc.connect(port)
print('initial encoder reads %s' % rc.readEncoderM1())
print('initial pid reads %s' % rc.readPidM1())

# set all the constants for pid qpps min and max
print('setting constants')
sleep(1)
rc.setPidQppsDeadzoneMinMaxM1(d, p, i, qpps, deadzone, minPos, maxPos)
print('pid now reads %s' % rc.readPidM1())
sleep(1)

# start publishing encoder data
rc.startEncoderM1()

# move the motor
rc.driveSpeedAccelDeccelPosM1(speed, accel, deccel, pos)
# see how close we came
print(rc.readEncoderM1())

# change pos
pos = 3000000

# move in the other direction
rc.driveSpeedAccelDeccelPosM1(speed, accel, deccel, pos)
# see how close we came
print('motor target %s motor actual %s' % (pos, rc.readEncoderM1()))

# continue polling encoder for 10 seconds
sleep(30)
rc.stopPolling()
