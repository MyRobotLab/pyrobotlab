##############################################
# This script creates the parts of a ROFI and 
# attaches them to MRL
#from org.myrobotlab.service import UltrasonicSensor
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
from org.myrobotlab.service import Swing
from org.myrobotlab.service import Speech
from time import sleep

# we need a dictionary of arrays which store calibration data for each servo/joint
calib = {}

# create the services
speech = Runtime.createAndStart("speech","Speech") # For voice feedback
#ear = Runtime.createAndStart("listen","Sphinx") # For hearing spoken commands

gui = Runtime.start("gui", "Swing")
keyboard = Runtime.start("keyboard", "Keyboard") # For getting user confirmation

#keyboard.addKeyListener(python)

# Arduino to connect everything to like a spinal cord
arduino = Runtime.createAndStart("arduino","Arduino")

#sr04 = Runtime.start("sr04", "UltrasonicSensor") # For an ultrasonic view of the world

# 6 joints in the Right leg
rAnkle = Runtime.createAndStart("R Ankle","Servo")
rLowLeg = Runtime.createAndStart("R Low Leg","Servo")
rKnee = Runtime.createAndStart("R Knee","Servo")
rMidLeg = Runtime.createAndStart("R Mid Leg","Servo")
rUpLeg = Runtime.createAndStart("R Up Leg","Servo")
rHip  = Runtime.createAndStart("R Hip","Servo")

#6 joints in the Left leg
lAnkle	= Runtime.createAndStart("L Ankle","Servo")
lLowLeg = Runtime.createAndStart("L Low Leg","Servo")
lKnee = Runtime.createAndStart("L Knee","Servo")
lMidLeg = Runtime.createAndStart("L Mid Leg","Servo")
lUpLeg = Runtime.createAndStart("L Up Leg","Servo")
lHip  = Runtime.createAndStart("L Hip","Servo")

# arduino.connect("COM10", 57600, 8, 1, 0) # For Windows users
arduino.connect("/dev/tty.usbmodem1411", 57600, 8, 1, 0) # For Mac users
sleep(2) # Give the service time to connect

gui.undockPanel(keyboard.getName()) # undock the keyboard panel to make it easy to use later.

# attach servos to Arduino
# right leg first
rAnkle.attach(arduino.getName(), 22)
rLowLeg.attach(arduino.getName(), 24)
rKnee.attach(arduino.getName(), 26)
rMidLeg.attach(arduino.getName(), 28)
rUpLeg.attach(arduino.getName(), 30)
rHip.attach(arduino.getName(), 32)

# left leg next
lAnkle.attach(arduino.getName(), 38)
lLowLeg.attach(arduino.getName(), 40)
lKnee.attach(arduino.getName(), 42)
lMidLeg.attach(arduino.getName(), 44)
lUpLeg.attach(arduino.getName(), 46)
lHip.attach(arduino.getName(), 48)

# time for the ultrasonic sensor
# I have a 4 pin HC-SR04 
#sr04.attach(arduino,"/dev/tty.usbmodem1411", 7, 8) # (comm dev, trigger pin, echo pin)
 
#sr04.addRangeListener(python);
# IMPORTANT - I've added my python service as a listener
# SO I BETTER HAVE a def publishRange(data) somewhere
 
joints = [ rAnkle, rLowLeg, rKnee, rMidLeg, rUpLeg, rHip, lAnkle, lLowLeg, lKnee, lMidLeg, lUpLeg, lHip ]
inlineJoints = [ rLowLeg, rKnee, rMidLeg, rUpLeg, lLowLeg, lKnee, lMidLeg, lUpLeg ]
rollJoints = [ rAnkle, rHip, lAnkle, lHip ]



########################################################################################
# Down below are all of the Python functions we've defined for repeatable tasks we don't
# want cluttering up all the stuff we're doing above.
def waitForInput():
  print "Press the C key to continue\n"
  speech.speak("Press the C key in the keyboard panel to continue")
  keypress = keyboard.readKey()
  while keypress != 'C': #loop until space
    keypress = keyboard.readKey()

def calibrationRoutine():
  print "Initializing calibration routine"
  speech.speak("Initializing calibration routine")
  initializeJoints()
  print calib
  calibrateMiddle()
  print "Adjust the servos sliders to get everything squared up"
  speech.speak("Adjust the servos sliders to get everything squared up")
  # wait for confirmation
  waitForInput()    
  # grab all the center positions of all of the servos
  for joint in joints:
    print joint.getName(), "has been tweaked to:", joint.getPos()
    # got to do somethign with the new positions
    calib[joint.getName()][1] = joint.getPos()
  #print calib
    
  calibrateHigh()
  print "Adjust the servos so the hips and ankles are square and the rest are at 45 degrees forwards"
  speech.speak("Adjust the servos so the hips and ankles are square and the rest are at 45 degrees forwards")
  # wait for confirmation
  waitForInput()
  # grab all the forward positions for the inline servos
  for joint in inlineJoints:
    print joint.getName(), "has been tweaked to:", joint.getPos()
    # got to do somethign with the new positions
    calib[joint.getName()][2] = joint.getPos()
  #print calib
      
  calibrateLow()
  print "Adjust the servos so the hips and ankles are square and the rest are at 45 degrees backwards"
  speech.speak("Adjust the servos so the hips and ankles are square and the rest are at 45 degrees backwards")
  # wait for confirmation
  waitForInput()
  # grab all the backward positions for the inline servos
  for joint in inlineJoints:
    print joint.getName(), "has been tweaked to:", joint.getPos()
    # got to do somethign with the new positions
    calib[joint.getName()][0] = joint.getPos()
  #print calib
  
  calibrateHighRoll()
  print "Adjust the servos so it is doing the splits. Ankles and hips at 45 degrees and legs straight"
  speech.speak("Adjust the servos so it is doing the splits. Ankles and hips at 45 degrees and legs straight")
  # wait for confirmation
  waitForInput()
  # grab the positive roll positions
  for joint in rollJoints:
    print joint.getName(), "has been tweaked to:", joint.getPos()
    # got to do somethign with the new positions
    calib[joint.getName()][2] = joint.getPos()
  #print calib
  
  print "Hold on to the robot as we proceed to the next position so it doesn't fall over"
  speech.speak("Hold on to the robot as we proceed to the next position so it doesn't fall over")
  # wait for confirmation
  waitForInput()
  
  calibrateLowRollLeft()
  print "Adjust the servos so the legs lean to the right. The left ankle and hip should be at a 45 degrees"
  speech.speak("Adjust the servos so the legs lean to the right. The left ankle and hip should be at a 45 degrees")
  # wait for confirmation
  waitForInput()
  # grab the negative left roll positions
  print "L Ankle has been tweaked to:", lAnkle.getPos()
  print "L Hip has been tweaked to:", lHip.getPos()
  calib[lAnkle.getName()][0] = lAnkle.getPos()
  calib[lHip.getName()][0] = lHip.getPos()
  #print calib
  
  print "Keep holding the robot as we proceed to the next position so it doesn't fall over"
  speech.speak("Keep holding the robot as we proceed to the next position so it doesn't fall over")
  # wait for confirmation
  waitForInput()
  
  calibrateLowRollRight()
  print "Adjust the servos so the legs lean to the left.  The right ankle and hip should be at a 45 degrees"
  speech.speak("Adjust the servos so the legs lean to the left.  The right ankle and hip should be at a 45 degrees")
  # wait for confirmation
  waitForInput()
  # grab the negative right roll positions
  print "R Ankle has been tweaked to:", rAnkle.getPos()
  print "R Hip has been tweaked to:", rHip.getPos()
  calib[rAnkle.getName()][0] = rAnkle.getPos()
  calib[rHip.getName()][0] = rHip.getPos()
  print calib
  print "Calibration routine complete"
  speech.speak("Calibration routine complete")
  
def initializeJoints():
  for joint in joints:
    joint.setMinMax(30,150)
    joint.map(-60,60,30,150)
    joint.moveTo(0)
    print "Moved " + joint.getName() + " to start position."
    calib[joint.getName()] = [-45,0,45]

def calibrateMiddle():
  for joint in joints:
    joint.moveTo(0)
    
def calibrateHigh():
  for joint in inlineJoints:
    joint.moveTo(45)
  for joint in rollJoints:
    joint.moveTo(0)
    
def calibrateLow():
  for joint in inlineJoints:
    joint.moveTo(-45)
  for joint in rollJoints:
    joint.moveTo(0)

def calibrateHighRoll():
  for joint in inlineJoints:
    joint.moveTo(0)
  for joint in rollJoints:
    joint.moveTo(45)

def calibrateLowRollLeft():
  for joint in inlineJoints:
    joint.moveTo(0)
  rAnkle.moveTo(45)
  rHip.moveTo(45)
  lAnkle.moveTo(-45)
  lHip.moveTo(-45)

def calibrateLowRollRight():
  for joint in inlineJoints:
    joint.moveTo(0)
  lAnkle.moveTo(45)
  lHip.moveTo(45)
  rAnkle.moveTo(-45)
  rHip.moveTo(-45)

def publishRange(myRange):
  print myRange # call back - we will now setup the listener




#########################################################################################
# Time to start doing some stuff with all those things we created above ...
calibrationRoutine()
#sr04.startRanging() 
#ear.addCommand("calibration routine", "python", "calibrationRoutine")
#ear.addCommand("attention", "python", "initializeJoints")
#ear.addComfirmations("yes","correct","yeah","ya")
#ear.addNegations("no","wrong","nope","nah")
#ear.startListening()
