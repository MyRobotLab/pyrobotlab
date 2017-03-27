from com.leapmotion.leap.Finger import Type
# from __future__ import division

#####################################################
#
# this simple script will print in the python tab the grab strength 
# of your left hand
#
# LeapMotion finger types are defined
# as the following:
# Type.TYPE_THUMB 
# Type.TYPE_INDEX 
# Type.TYPE_MIDDLE
# Type.TYPE_RING 
# Type.TYPE_PINKY

leap = Runtime.createAndStart("leap","LeapMotion")

leap.addLeapDataListener(python)

def onLeapData(data):
 
 
 print (data.rightHand.index)
 
leap.startTracking()

