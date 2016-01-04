i01 = Runtime.createAndStart("i01","InMoov")

#Set here the port of your InMoov Left Hand Arduino , in this case COM5
leftHand = i01.startLeftHand("COM5")

#==============================
#Set the min/max values for fingers

i01.leftHand.thumb.setMinMax( 0, 61)
i01.leftHand.index.map(0 , 89)
i01.leftHand.majeure.map(0 , 89)
i01.leftHand.ringFinger.map(0 , 104)
i01.leftHand.pinky.map(0 , 91)
#===============================

#Start the Leap Tracking
i01.leftHand.starLeapTracking()

#stop leap tracking
#i01.leftHand.stopLeapTracking()
