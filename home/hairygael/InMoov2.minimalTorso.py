#file : InMoov2.minimalTorso.py

# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a right Arm
# for any command which you say - you will be required to say a confirmation
# e.g. you say -> test stomach, InMoov will ask -> "Did you say test stomach?", you will need to
# respond with a confirmation ("yes","correct","yeah","ya")
from java.lang import String
from org.myrobotlab.service import Runtime
import urllib2
import os

# To set a directory
# Modify this line according to your directory and version of MRL
os.chdir("C:/myrobotlab/myrobotlab.1.0.107/audioFile/google/en_gb/audrey")

# the name of the local file
# remove the file if it already exist in the Audiofile directory
soundfilename="starting mouth.mp3";

try:
	mp3file = urllib2.urlopen('http://www.inmoov.fr/wp-content/uploads/2015/05/starting-mouth.mp3')
	output = open(soundfilename,'wb')
	output.write(mp3file.read())
	output.close()
except IOError:
	print "Check access right on the directory"
except Exception:
	print "Can't get the sound File ! Check internet Connexion"



leftPort = "COM20"  #modify port according to your board

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

mouth = Runtime.createAndStart("mouth","Speech")
i01.startMouth()
##############
torso = i01.startTorso("COM20")  #modify port according to your board
# tweaking default torso settings
torso.topStom.setMinMax(0,180)
torso.topStom.map(0,180,67,110)
torso.midStom.setMinMax(0,180)
torso.midStom.map(0,180,60,120)
#torso.lowStom.setMinMax(0,180)
#torso.lowStom.map(0,180,60,110)
#torso.topStom.setRest(90)
#torso.midStom.setRest(90)
#torso.lowStom.setRest(90)

#################
# verbal commands
ear = i01.ear

ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach torso", "i01.torso", "attach")
ear.addCommand("disconnect torso", "i01.torso", "detach")
ear.addCommand("rest", "python", "rest")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("test your stomach", "python", "teststomach")
 
ear.addComfirmations("yes","correct","ya","yeah", "yes please", "yes of course")
ear.addNegations("no","wrong","nope","nah","no thank you", "no thanks")

ear.startListening()

def teststomach():
    i01.setTorsoSpeed(0.75,0.55,0.75)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveTorso(45,90,90)
    sleep(4)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveTorso(135,90,90)
    sleep(4)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveTorso(90,45,90)
    sleep(3)
    i01.moveTorso(90,135,90)
    sleep(3)
    i01.moveTorso(90,90,45)
    sleep(3)
    i01.moveTorso(90,90,135)
    sleep(3)