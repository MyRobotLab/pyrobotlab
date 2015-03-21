#########################################################
# Example Script to show using OculusRift
# with the InMoov head, having 2 cameras
# It will display the camera video streams in the Rift (Side-By-Side)
# It will also subscribe to the head tracking data to update servo positions
# The neck servo tracks pitch
# the rothead servo tracks yaw
# roll is implemented with the OpenCV Affine filter.
#
# TODO: add leap motion & inverse kinematics :) woot!
# 
# JVM args ? maybe not necessary
# -Djna.library.path=myrobotlab\libraries\native  (needs to find the OVR_C.dll native library)

# Com port for arduino
comPort = "COM19"
# neck servo pin
neckPin = 12
# got head servo pin
rotheadPin = 13

# Create the Rift 
rift= Runtime.createAndStart("rift", "OculusRift")
# create the arduino
arduino = Runtime.createAndStart("arduino", "Arduino")
# create the 2 servos for pan/tilt
neck = Runtime.createAndStart("neck", "Servo")
rothead = Runtime.createAndStart("rothead", "Servo")
# connect to the arduino
arduino.connect(comPort)
# Attach the servos 
neck.attach("arduino", neckPin)
rothead.attach("arduino", rotheadPin)

# Define a callback method for the oculus head tracking info
def headTracking(data):
    # amplify the pitch recorded from the rift by a factor of 3 
    # To account for gear ratio of neck piston in inmoov (adjust as needed) 
    pitch = data.pitch * 3
    # the center position for the neck is 90 degre3es
    neckOffset = 90
    # update the neck position
    neck.moveTo(pitch + neckOffset)
    
    # track the yaw
    yaw = data.yaw
    # center position (yaw = 0 / servo = 90 degrees)
    rotHeadOffset = 90
    # turn head left/right to track yaw
    rothead.moveTo(rotHeadOffset + yaw)
    # Debugging info
    print(data)
    # TODO: track the affine filters for roll

# add the callback to python from the rift.
rift.addListener("publishOculusData", "python", "headTracking")





