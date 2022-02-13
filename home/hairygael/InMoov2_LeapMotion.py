# Leap + InMoov2 hand version MRL Nixie
Platform.setVirtual(False)
i01 = Runtime.createAndStart("i01","InMoov2")
arduino = Runtime.start('arduino', 'Arduino')
arduino.connect("ttyACM0")
i01.startRightHand()
i01.rightHand.startPeers()

# make sure the pins are set before attaching
i01_rightHand_thumb.setPin("2")
i01_rightHand_index.setPin("3")
i01_rightHand_majeure.setPin("4")
i01_rightHand_ringFinger.setPin("5")
i01_rightHand_pinky.setPin("6")
i01_rightHand_wrist.setPin("7")

# develop this for each servo mappings
#i01_rightHand_thumb.map(0.0,180.0,0.0,180.0)

# we set the speed for each servo of the hand 
i01.setRightHandSpeed(500,500,500,500,500,500)

# we attach the the controller
arduino.attach("i01.rightHand.thumb")
arduino.attach("i01.rightHand.index")
arduino.attach("i01.rightHand.majeure")
arduino.attach("i01.rightHand.ringFinger")
arduino.attach("i01.rightHand.pinky")
arduino.attach("i01.rightHand.wrist")
sleep(1)
leap = Runtime.createAndStart("leap","LeapMotion")
leap.startPeers()
leap.addLeapDataListener(i01.rightHand)
leap.startTracking()
