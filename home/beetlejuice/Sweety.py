# Sweety's service

Runtime.createAndStart("sweety", "Sweety")
sweety.arduino.setBoard("atmega2560")
sweety.connect("COM8")
sleep(1) # give a second to the arduino for connect
sweety.attach()
sweety.startPosition()
sweety.mouthState("smile")
sleep(1)
# set delays for led sync (delayTime, delayTimeStop, delayTimeLetter)
sweety.setdelays(50,200,50)
sweety.saying("Hello,i am ready to work.")
