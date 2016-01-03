inmoov = Runtime.createAndStart("inmoov","InMoov")

inmoov.startRightHand("COM5")

inmoov.rightHand.index.setMinMax(30,89)
inmoov.rightHand.thumb.setMinMax(30,60)
inmoov.rightHand.majeure.setMinMax(30,89)
inmoov.rightHand.ringFinger.setMinMax(30,90)
inmoov.rightHand.pinky.setMinMax(30,90)

sleep(1)

inmoov.rightHand.startLeapTracking()

# inmoov.rightHand.stopLeapTracking()
