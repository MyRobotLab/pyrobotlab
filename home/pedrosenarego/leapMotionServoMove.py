##################################################################
# Leap Motion Example Script
##################################################################

# when leap motion data is detected, it will be passed in here
def onLeapData(data):
  # make sure we get the global scope of the servo service here.
  global servo01
  # process the data that came in.
  # right hand first
  if (data.rightHand):
    # if the data has a right hand, print out some info about it.
    print("Right Thumb =" + str(data.rightHand.thumb))   
    print("Right Index =" + str(data.rightHand.index))
    print("Right Middle =" + str(data.rightHand.middle))
    print("Right Ring =" + str(data.rightHand.ring))
    print("Right Pinky =" + str(data.rightHand.pinky))
    print("Right Hand Position: x=" + str(data.rightHand.posX) + " y=" + str(data.rightHand.posY) + " z=" + str(data.rightHand.posZ))
    # update a position of
    indexarino = ((100-data.rightHand.index)*1.8)
    servo01.moveTo(indexarino)
  else:
    # the right hand wasn't found.
    print("Right hand not detected.")
  # left hand data.
  if (data.leftHand):
    # print some info about the left hand
    print("Left Thumb =" + str(data.leftHand.thumb))   
    print("Left Index =" + str(data.leftHand.index))
    print("Left Middle =" + str(data.leftHand.middle))
    print("Left Ring =" + str(data.leftHand.ring))
    print("Left Pinky =" + str(data.leftHand.pinky))
    print("Left Hand Position: x=" + str(data.leftHand.posX) + " y=" + str(data.leftHand.posY) + " z=" + str(data.leftHand.posZ))
  else: 
    # print left hand not found.
    print("Left hand not detected.")

  if (data.frame):
    # this is the raw frame info from the leap if you want it.
    print(str(frame))
    
###########################################################
# MAIN Script entry point
###########################################################
# create the leap motion service
leap = Runtime.createAndStart("leap","LeapMotion")
# connect python as a listener for the onLeapData callback
leap.addLeapDataListener(python)
# start the leap motion watching for valid frames.
leap.startTracking()

# set the servo pin that we'll control
servoPin = 3
# specify a rest postion for the servo
restPosition = 90
# specify a com port for the arduino
comPort = "/dev/ttyACM0"

# create the servo & arduino services
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")

arduino.connect(comPort)
# TODO - set limits
servo01.setMinMax(0, 160)
servo01.map(0, 180, 0, 160)
servo01.setVelocity(-1)
# attach servo
servo01.attach(arduino.getName(), servoPin)
# lets move the servo to it's rest position.
servo01.moveTo(restPosition)