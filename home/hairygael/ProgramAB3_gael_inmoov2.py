import random
import threading
import itertools
leftPort = "COM20"
rightPort = "COM7"

from java.lang import String 
i01 = Runtime.createAndStart("i01", "InMoov")
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
inmoov2 = Runtime.createAndStart("inmoov2", "ProgramAB")
inmoov2.startSession("Gael", "inmoov2")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
wksr.addTextListener(inmoov2)
inmoov2.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

i01.startHead(leftPort)
i01.startMouth()
i01.startMouthControl(leftPort)
##############
# tweaking default settings of jaw
i01.head.jaw.setMinMax(65,90)
#i01.head.jaw.map(0,180,10,35)
i01.mouthControl.setmouth(65,90)
i01.head.jaw.setRest(90)
# tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,70,110)
i01.head.eyeY.setRest(90)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,110)
i01.head.eyeX.setRest(90)
i01.head.neck.setMinMax(0,180)
i01.head.neck.map(0,180,15,155)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(0,180)
i01.head.rothead.map(0,180,30,150)
i01.head.rothead.setRest(86)
###################
#i01.startEyesTracking(leftPort)
#i01.startHeadTracking(leftPort)
##############
#i01.startEar()

i01.mouth.speak("I think I am ready")