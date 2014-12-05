#this simple script will print in the python tab the grab strength of your left hand

from __future__ import division

leap = Runtime.createAndStart("leap","LeapMotion2")

leap.addFrameListener(python)

def onFrame(frame):
 
 strength = ((frame.hands().leftmost().grabStrength())*100)
 print strength

leap.startTracking()
