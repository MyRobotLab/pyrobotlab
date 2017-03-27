##################################################################
# Leap Motion Example Script
##################################################################

# when leap motion data is detected, it will be passed in here
def onLeapData(data):
  if (data.rightHand):
    # if the data has a right hand, print out some info about it.
    print("Right Thumb =" + str(data.rightHand.thumb))   
    print("Right Index =" + str(data.rightHand.index))
    print("Right Middle =" + str(data.rightHand.middle))
    print("Right Ring =" + str(data.rightHand.ring))
    print("Right Pinky =" + str(data.rightHand.pinky))
    print("Right Hand Position: x=" + str(data.rightHand.posX) + " y=" + str(data.rightHand.posY) + " z=" + str(data.rightHand.posZ))
  else:
    # the right hand wasn't found.
    print("Right hand not detected.")
    
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
