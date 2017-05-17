# Leap + InMoov hand version MRL above 2000 
inmoov = Runtime.createAndStart("inmoov","InMoov")
inmoov.startRightHand("COM7","atmega2560")
inmoov.rightHand.index.setMap(0,180,0,160)
inmoov.rightHand.thumb.setMap(0,180,55,135)
inmoov.rightHand.majeure.setMap(0,180,50,170)
inmoov.rightHand.ringFinger.setMap(0,180,48,145)
inmoov.rightHand.pinky.setMap(0,180,30,168)
inmoov.rightHand.wrist.setMap(0,180,10,170)#rollwrist
inmoov.rightHand.setVelocity(-1,-1,-1,-1,-1)
sleep(1)
inmoov.rightHand.startLeapTracking()
# inmoov.rightHand.stopLeapTracking()
