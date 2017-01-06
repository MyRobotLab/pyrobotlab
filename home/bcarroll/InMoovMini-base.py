#

from time import sleep

# Create OpenCV Service for Vision
cameraIndex = 0
opencv = Runtime.createAndStart("opencv", "OpenCV")
opencv.publishOpenCVData(True)
opencv.setCameraIndex(cameraIndex)
opencv.addFilter("PyramidDown", "PyramidDown") # Scale down captured image (speeds up drawing to display)
opencv.addFilter("rotate_90degrees", "Transpose") #Rotate captured image 90 degrees (Camera is mounted 270 degrees off)
opencv.addFilter("rotate_180degrees", "Transpose") #Rotate captured image 90 degrees (Camera is mounted 270 degrees off)
opencv.addFilter("rotate_270degrees", "Transpose") #Rotate captured image 90 degrees (Camera is mounted 270 degrees off)
opencv.capture() # start capturing from the camera


# Jaw movement when speaking vaiables
delaytime = .05
delaytimestop = .45
delaytimeletter = .1
delaytimebeforespeaking = .6 # when mouth.say() is called, delay this amount (seconds) before moving the jaw.

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("/dev/ttyUSB0")

# Start the Adafruit16CServodriver that can be used for all PCA9685 devices
adafruit16c = Runtime.createAndStart("adafruit16c","Adafruit16CServoDriver")
adafruit16c.setController("arduino","1","0x40")

######################################################################
# mouth service, speech synthesis - takes a minute to load
mouth = Runtime.createAndStart("mouth", "MarySpeech")
mouth.setVoice("dfki-obadiah-hsmm")

# Jaw Servo (mouth open/close)
jawServoPort = 0  
jaw_min      = 85
jaw_max      = 155
jaw_rest     = 88
jaw = Runtime.create("jaw", "Servo")
jaw.attach(adafruit16c, jawServoPort)
jaw.setMinMax(jaw_min,jaw_max)
jaw.map(0,180,jaw_min,jaw_max)
jaw.setRest(jaw_rest)
jaw.moveTo(jaw_rest)

# Head Servo (head left/right)
headServoPort = 1
head_min      = 30
head_max      = 175
head_rest     = 100
head = Runtime.createAndStart("head", "Servo")
head.attach(adafruit16c, headServoPort)
head.setMinMax(head_min,head_max)
head.map(0,180,head_min,head_max)
head.setRest(head_rest)
head.moveTo(head_rest)

# Neck Servo (head up/down)
neckServoPort = 2  
neck_min      = 25
neck_max      = 175
neck_rest     = 150
neck = Runtime.create("neck", "Servo")
neck.attach(adafruit16c, neckServoPort)
neck.setMinMax(neck_min,neck_max)
neck.map(0,180,neck_min,neck_max)
neck.setRest(neck_rest)
neck.moveTo(neck_rest)

# Right Shoulder Servo (up/down)
right_shoulderServoPort = 3
right_shoulder_min      = 0
right_shoulder_max      = 180
right_shoulder_rest     = 180
right_shoulder = Runtime.create("right_shoulder", "Servo")
right_shoulder.attach(adafruit16c, right_shoulderServoPort)
right_shoulder.setRest(right_shoulder_rest)
right_shoulder.moveTo(right_shoulder_rest)

# Right Shoulder Rotational Servo (front/back)
right_shoulderRotServoPort = 4
right_shoulderRot_min      = 0
right_shoulderRot_max      = 180
right_shoulderRot_rest     = 180
right_shoulderRot = Runtime.create("right_shoulderRot", "Servo")
right_shoulderRot.attach(adafruit16c, right_shoulderRotServoPort)
right_shoulderRot.setRest(right_shoulderRot_rest)
right_shoulderRot.moveTo(right_shoulderRot_rest)

# Right Bicep Rotational Servo (left/right)
right_bicepRotServoPort = 5
right_bicepRot_min      = 0
right_bicepRot_max      = 180
right_bicepRot_rest     = 180
right_bicepRot = Runtime.create("right_bicepRot", "Servo")
right_bicepRot.attach(adafruit16c, right_bicepRotServoPort)
right_bicepRot.setRest(right_bicepRot_rest)
right_bicepRot.moveTo(right_bicepRot_rest)

# Right Elbow Servo (in right bicep)
right_elbowServoPort = 6
right_elbow_min      = 0
right_elbow_max      = 180
right_elbow_rest     = 90
#right_elbow = Runtime.create("right_elbow", "Servo")
#right_elbow.attach(adafruit16c, right_elbowServoPort)
#right_elbow.setRest(right_elbow_rest)
#right_elbow.moveTo(right_elbow_rest)

######################################################################
# helper function to help debug recognized speech from webkit/sphinx
######################################################################
def speech_in(data):
	print "Speech Recognition Data:"+str(data)

inmoovWebKit = Runtime.createAndStart("inmoovWebKit", "ProgramAB")
inmoovWebKit.startSession("Brett", "inmoovWebKit")
######################################################################
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

######################################################################
# the "ear" of the inmoov
ear = Runtime.createAndStart("speechRecognition", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "speech_in");
ear.addMouth(mouth)
ear.setLanguage("en-EN")
python.subscribe(ear.getName(),"publishText")

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
ear.addTextListener(inmoovWebKit)
inmoovWebKit.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

def say(text):
	#replacement for MouthControl Service
	mouth.speak(text)
	#print "say(" + text + ")"
	sleep(delaytimebeforespeaking) #in case speech output does not start immediately
	#what to do when speaking
	ison = False
	for w in text.split():
		if w.endswith("es"):
			#print "   endswith es"
			w = w[0:len(w)-2]
		elif w.endswith("e"):
			#print "   endswith e"
			w = w[0:len(w)-1]

		for x in list(w):
			#print x
			if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y' and not ison:
				jaw.moveTo(jaw_max) # move the servo to the open position
				ison = True
				sleep(delaytime)
				jaw.moveTo(jaw_min) # close the servo
			elif x == '.':
				ison = False
				sleep(delaytimestop)
			elif x == ',':
				sleep(delaytimestop)
			else:
				ison = False
				sleep(delaytimeletter)

say("Ready")
