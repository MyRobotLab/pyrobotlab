######################################################
# Robots For Good
# This script will run in the hospital
# it displays the remote video in the oculus
# it also sends head tracking info back to
# the remote inmoov for servo control.
######################################################
# TODO: replace me with RemoteAdapeter
import urllib

######################################################
# This script will load the oculus &
# the inmoov arms so that you can teleoperate
# kwatters
# Env specific config
######################################################
leftCameraIndex = 1
leftCameraAngle = 180
rightCameraIndex = 0
rightCameraAngle = 0
# mjpeg-streamer seems to work well on ras pi, these are the urls
leftCameraUrl = "http://192.168.4.112:8081/?action=stream"
rightCameraUrl = "http://192.168.4.112:8080/?action=stream"
# The remote uri for MyRobotLab running on the InMoov
inMoovAddress = "tcp://192.168.4.112:6767"

######################################################
# HELPER FUNCTIONS
######################################################
def readUrl(url):
  u = urllib.urlopen(url)
  # just send the request, ignore the response
  u.read(0)
  u.close()
  
# Define a callback method for the oculus head tracking info
def onOculusData(data):
    print(data)
    # amplify the pitch recorded from the rift by a factor of 3 
    # To account for gear ratio of neck piston in inmoov (adjust as needed) 
    pitch =  -1 * data.pitch * 3
    # the center position for the neck is 90 degre3es
    neckOffset = 130
    neckPos = int(pitch + neckOffset)
    # update the neck position
    neckUrl = "http://192.168.4.112:8888/api/service/i01.head.neck/moveTo/" + str(neckPos)
    print neckUrl
    readUrl(neckUrl)
    # neck.moveTo(neckPos)
    # track the yaw
    yaw = data.yaw
    yaw = -1 * yaw
    # center position (yaw = 0 / servo = 90 degrees)
    rotHeadOffset = 90
    rotheadPos = int(rotHeadOffset + yaw)
    rotheadUrl = "http://192.168.4.112:8888/api/service/i01.head.rothead/moveTo/" + str(rotheadPos)
    print rotheadUrl
    readUrl(rotheadUrl)    
    # turn head left/right to track yaw
    # rothead.moveTo(rotHeadPos)
    # Track the Roll in software
    rollgain = 1
    roll = data.roll * rollgain
    # left camera is 180 degrees rotated from the right camera
    # as you roll clockwise, this counter balances that 
    # by rolling the camera counter clockwise
    # rift.leftOpenCV.getFilter("left").setAngle(-roll+180);
    # rift.rightOpenCV.getFilter("right").setAngle(-roll) 
    # TODO: track the affine filters for roll

######################################################
# Create the Rift 
rift = Runtime.createAndStart("rift", "OculusRift")
rift.setLeftCameraIndex(leftCameraIndex)
rift.setLeftCameraAngle(leftCameraAngle)
rift.setRightCameraIndex(rightCameraIndex)
rift.setRightCameraAngle(rightCameraAngle)
# TODO: other calibration as necessary / desired.
# set the frame grabber
rift.setFrameGrabberType("org.myrobotlab.opencv.MJpegFrameGrabber");
rift.setLeftEyeURL(leftCameraUrl)
rift.setRightEyeURL(rightCameraUrl)
rift.setCvInputSource("network")
# TODO: rename this .. this is a lame name.
rift.initContext()
# Create the remote adapter for distributed MRL.
# remoteInMoov = Runtime.createAndStart("remoteInMoov", "RemoteAdapter")
# remoteInMoov.connect(inMoovAddress)
    
# add the callback to python from the rift.
rift.addListener("publishOculusData", "python", "onOculusData")


# lets add a joystick that can handle some inputs to the arms.

