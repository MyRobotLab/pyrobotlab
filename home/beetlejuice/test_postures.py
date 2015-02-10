# Sweety's postures test
import random


Runtime.createAndStart("sweety", "Sweety")
sweety.arduino.setBoard("atmega2560")
sweety.connect("COM9")
sleep(1) # give a second to the arduino for connect
sweety.attach()

sweety.mouthState("smile")
sleep(1)
# set delays for led sync (delayTime, delayTimeStop, delayTimeLetter)
sweety.setdelays(50,200,50)
sweety.mouth.setLanguage("en")
#sweety.saying("Hello,my name is sweety.")

sweety.posture("neutral")
sweety.saying("neutral.")
sleep(2)

sweety.posture("yes")
sweety.saying("yes.")
sleep(2)

sweety.posture("concentre")
sweety.saying("concentre.")
sleep(2)

sweety.posture("showLeft")
sweety.saying("show left.")
sleep(2)

sweety.posture("showRight")
sweety.saying("show right.")
sleep(2)

sweety.posture("handsUp")
sweety.saying("hands up !")
sleep(2)

sweety.posture("carryBags")
sweety.saying("carry bags.")
sleep(2)

sweety.posture("neutral")
sweety.saying("neutral.")
