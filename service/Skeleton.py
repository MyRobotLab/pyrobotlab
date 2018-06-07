#########################################
# Skeleton.py
# more info @: http://myrobotlab.org/service/Skeleton
#########################################

# this script is provided as a basic scripting guide for control multiple servo group
# or attach things to the InMoov service
# although this script is very short you can still
# do voice control of a servo group
# It uses WebkitSpeechRecognition by default, so you need to use Chrome as your default browser for this script to work

## THIS IS SAMPLE FOR USING INMOOV RIGHT HAND

##############
# Hardware setup ( Arduino nervoboard right hand setup as a sample )
# Any compatible controller should work
rightPort="COM42"
# start optional virtual arduino service, used for internal test and virtual inmoov
#virtual=True
if ('virtual' in globals() and virtual):
    virtualArduinoRight = Runtime.start("virtualArduinoRight", "VirtualArduino")
    virtualArduinoRight.connect(rightPort)
# end used for internal test

# start your compatible controller, here it is Arduino
rightArduino = Runtime.createAndStart("rightArduino", "Arduino")
rightArduino.connect(rightPort)

# start your servos or diyServo
# 6 servos for hand is standardized sample, you can use 1 or 99...
rightThumb = Runtime.start("rightThumb", "Servo")
rightIndex = Runtime.start("rightIndex", "Servo")
rightMajeure = Runtime.start("rightMajeure", "Servo")
rightRingFinger = Runtime.start("rightRingFinger", "Servo")
rightPinky = Runtime.start("rightPinky", "Servo")
rightWrist = Runtime.start("rightWrist", "Servo")
#otherServo = Runtime.start(otherServo,Servo)

# you can use servo Gui to calibrate and tweak them in live after script start, it is easier
# or override here like it :
# rightThumb.map(0,180,64,135)
# rightThumb.setRest(0)
# rightThumb.setVelocity(40) > -1 is fullspeed / no velocity control



##############
# Start other optional services
inMoov = Runtime.start("inMoov", "InMoov2")
rightHand = Runtime.start("rightHand", "Skeleton")

mouth = Runtime.start("mouth", "MarySpeech")
ear = Runtime.start("ear", "WebkitSpeechRecognition")


##############
# Attach things !

# servo to arduino
rightThumb.attach(rightArduino, 2)
rightIndex.attach(rightArduino, 3)
rightMajeure.attach(rightArduino, 4)
rightRingFinger.attach(rightArduino, 5)
rightPinky.attach(rightArduino, 6)
rightWrist.attach(rightArduino, 7)
# sub joints to main member
rightHand.attach(rightThumb,rightIndex,rightMajeure,rightRingFinger,rightPinky,rightWrist)
# various services to InMoov
inMoov.attach(rightHand,"hand","right")
inMoov.attach(mouth)
inMoov.attach(ear)



#################
# verbal commands

ear.addCommand("rest", "inMoov.rightHand", "rest")#hardcoded gesture
ear.addCommand("relax", "python", "relax")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")


# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def relax():
  inMoov.setHandVelocity("right", 30, 30, 30, 30, 30, 30)
  inMoov.moveHand("right",90,90,90,90,90,140)
  inMoov.mouth.speak(u"Goodtime")

def handopen():
  inMoov.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  inMoov.moveHand("right",0,0,0,0,0,0)
  inMoov.mouth.speak(u"ok I open my hand")

def handclose():
  inMoov.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  inMoov.moveHand("right",180,180,180,180,180,180)
  inMoov.mouth.speak(u"a nice and closed hand that is")

#set the hand to relax() at launch
relax() 
#inMoov.loadGestures()