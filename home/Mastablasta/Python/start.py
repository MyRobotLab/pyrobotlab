import random
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
from java.lang import String
from time import sleep
from org.myrobotlab.net import BareBonesBrowserLaunch
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
elias = Runtime.createAndStart("elias", "ProgramAB")
elias.startSession("elias")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Graham")
wksr.addTextListener(elias)
elias.addTextListener(htmlfilter)
htmlfilter.addTextListener(acapelaSpeech)

def BT():
    global c
    c = b - a
    sleep(2)
    print c
    if (c == 2):
       resp = elias.getResponse("AUTORESPOND1")          
    if (c == 4):
	  resp = elias.getResponse("AUTORESPOND2")           
    if (c == 6):
       resp = elias.getResponse("AUTORESPOND3")           
    if (c == 8):
       resp = elias.getResponse("AUTORESPOND4")        
    if (c == 10):
       speech.speakBlocking("I will tell myself a joke.")
       sleep(4)
       resp = elias.getResponse("TELL ME A JOKE")
    if (c == 12):
       resp = elias.getResponse("AUTORESPOND5")          
    if (c == 14):
       resp = elias.getResponse("AUTORESPOND6")
            #i01.headTracking.faceDetect()
            #i01.eyesTracking.faceDetect()
            #sleep(30)
            #i01.headTracking.stopTracking()
            #i01.eyesTracking.stopTracking()
    if (c == 16):
        speech.speakBlocking("I will listen to some music.")
        sleep(5)
        x = (random.randint(1, 6))
        if x == 1:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=ozBHgQA4Jlk")
        if x == 2:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=Fw6k0kMVcCI")
        if x == 3:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=OQIYEPe6DWY")  
        if x == 4:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=DZiJQL9OLqI")
        if x == 5:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=fpWNimba344")  
        if x == 6:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=tFXYuw96d0c")   
    if (c == -58):
       resp = elias.getResponse("AUTORESPOND1")  
    if (c == -56):
       resp = elias.getResponse("AUTORESPOND2")  
    if (c == -54):
       resp = elias.getResponse("AUTORESPOND3")  
    if (c == -52):
       resp = elias.getResponse("AUTORESPOND4")  
    if (c == -50):
       speech.speakBlocking("I will tell myself a joke.")
       sleep(4)
       resp = elias.getResponse("TELL ME A JOKE")
    if (c == -48):
       resp = elias.getResponse("AUTORESPOND5") 
    if (c == -46):
       resp = elias.getResponse("AUTORESPOND6") 
       #i01.headTracking.faceDetect()
       #i01.eyesTracking.faceDetect()
       #sleep(30)
       #i01.headTracking.stopTracking()
       #i01.eyesTracking.stopTracking()
    if (c == -44):    
        speech.speakBlocking("I will listen to some music.")
        sleep(5)
        x = (random.randint(1, 6))
        if x == 1:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=ozBHgQA4Jlk")
        if x == 2:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=Fw6k0kMVcCI")
        if x == 3:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=OQIYEPe6DWY")  
        if x == 4:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=DZiJQL9OLqI")
        if x == 5:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=fpWNimba344")  
        if x == 6:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=tFXYuw96d0c")                                                           
    else:
        sleep(54)
        resp = elias.getResponse("CHECKTIME")
        sleep(4)
        resp = elias.getResponse("7OF9")

def PO():
    i01.powerUp()

def detachall():
    i01.detach()

def attachall():
    i01.attach()

def detachhead():
    i01.head.detach()

def attachhead():
    i01.head.attach()

def detachrighthand():
    i01.rightHand.detach()

def attachrighthand():
    i01.rightHand.attach()

def detachrightarm():
    i01.rightArm.detach()

def attachrightarm():
    i01.rightArm.attach()
