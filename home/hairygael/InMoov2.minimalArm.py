#file : InMoov2.minimalArm.py

# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a right Arm
# for any command which you say - you will be required to say a confirmation
# e.g. you say -> arm front, InMoov will ask -> "Did you say arm front?", you will need to
# respond with a confirmation ("yes","correct","yeah","ya")

leftPort = "COM13"  #modify port according to your board
rightPort = "COM17" #modify port according to your board

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
##############
i01.startLeftArm(leftPort)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)
#################
i01.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)
#################
# verbal commands
ear = i01.ear

ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach left arm", "i01.leftArm", "attach")
ear.addCommand("disconnect left arm", "i01.leftArm", "detach")
ear.addCommand("attach right arm", "i01.rightArm", "attach")
ear.addCommand("disconnect right arm", "i01.rightArm", "detach")
ear.addCommand("rest", "python", "rest")
ear.addCommand("arms front", i01.getName(), "armsFront")
ear.addCommand("da vinci", i01.getName(), "daVinci")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
 
ear.addComfirmations("yes","correct","ya","yeah", "yes please", "yes of course")
ear.addNegations("no","wrong","nope","nah","no thank you", "no thanks")

ear.startListening()

def rest():
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
