# Script for the head of my InMoov
# Supposed to start when powered in, so the startup seqence may seem a bit strange
# First it starts the eye servos and move the eyes around a bit to make him "awake"
# Then the speech service is started so that the robot can explan talk about the rest of the
# startup sequence
# 
# Start the Arduino service and connect to it
def lookSideways(degrees):
	eyeLeft.moveTo(eyeLeft.getRest() + degrees)
	eyeRight.moveTo(eyeRight.getRest() + degrees)
	neck.moveTo(neck.getRest() - degrees)
# 
arduino = Runtime.start("arduino","Arduino")
arduino.connect("/dev/ttyACM0")
#
# Start all the eye servos
eyes = Runtime.start("eyes","Servo")
eyeLeft = Runtime.start("eyeLeft","Servo")
eyeRight = Runtime.start("eyeRight","Servo")
neck = Runtime.start("neck","Servo")
eyes.setMinMax(50,120)
eyes.setRest(90)
eyes.attach("arduino",12)
eyes.rest()

eyeRight.setMinMax(70,130)
eyeRight.setRest(100)
eyeRight.attach("arduino",11)
eyeRight.rest()

eyeLeft.setMinMax(40,100)
eyeLeft.setRest(70)
eyeLeft.attach("arduino",10)
eyeLeft.rest()

neck.setMinMax(0,180)
neck.setRest(90)
neck.attach("arduino",8)
neck.setVelocity(20)
neck.rest()

speech = Runtime.start("speech","MarySpeech")
voice = 'cmu-bdl-hsmm'
speech.setVoice(voice)
lookSideways(10)
speech.speakBlocking("Hello")
lookSideways(-10)
speech.speakBlocking("My name is InMoov")
lookSideways(20)
speech.speakBlocking("I was designeg by Gael Langevin in Paris")
lookSideways(-20)
speech.speakBlocking("All the parts in my body has been printed on a 3d printer")
lookSideways(30)
speech.speakBlocking("I have a Raspberry PI in the head that is my brain")
lookSideways(-30)
speech.speakBlocking("A second PI is mounted in my back. It acts as my gut feeling")
lookSideways(30)
speech.speakBlocking("My head also contains an Arduino that drives the servos for my eyes, mouth and neck")	
lookSideways(-30)
speech.speakBlocking("In each arm I have a small board that drives the servos for my arm and hand")	
lookSideways(0)
speech.speakBlocking("There is a camera in my eye so that I can see")	
lookSideways(30)
speech.speakBlocking("As you can hear I also can speak")	
lookSideways(30)
speech.speakBlocking("I also have a microphone,so that I can hear")	
lookSideways(30)
speech.speakBlocking("It will soon be replace with a microphone array, so that I can detect where the sound is coming from")	
lookSideways(0)
webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(False)
webgui.start()