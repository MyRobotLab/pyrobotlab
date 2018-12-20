#########################################
# InMoov.py
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# a very minimal script for InMoov
# this script is provided as a basic guide for InMoov service
# InMoov now can be started in modular pieces through the skeleton.config from full script
# although this script is very short you can still
# do voice control of a FingerStarter or hand
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# virtual = True

rightPort = "COM8"
leftPort = "COM10"

i01 = Runtime.start("i01", "InMoov")

if ('virtual' in globals() and virtual):
    leftPortvirtualArduino = Runtime.start("leftPortvirtualArduino", "VirtualArduino")
    leftPortvirtualArduino.connect(leftPort)
    rightPortvirtualArduino = Runtime.start("rightPortvirtualArduino", "VirtualArduino")
    rightPortvirtualArduino.connect(rightPort)

# starting parts
i01.startAll(leftPort,rightPort)
if ('virtual' in globals() and virtual):i01.startVinMoov()

# verbal commands
ear = i01.ear

ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def handopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)