import random
from java.lang import String
from org.myrobotlab.net import BareBonesBrowserLaunch
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
elias = Runtime.createAndStart("elias", "ProgramAB")
elias.startSession("ProgramAB", "MastaBlasta", "elias")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
wksr.addTextListener(elias)
elias.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

def BT():
    global c
    c = b - a
    sleep(2)
    print c
    if (c == 3):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am here.")
        if x == 2:
            mouth.speak("Hello, hello.")
        if x == 3:
            mouth.speak("Hi, I am here.")
    if (c == 5):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am bored.")
        if x == 2:
            mouth.speak("What a boring day.")
        if x == 3:
            mouth.speak("I have nothing to do.")
    if (c == 7):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am still bored.")
        if x == 2:
            mouth.speak("What a boring boring boring boring day.")
        if x == 3:
            mouth.speak("You can turn me off.")
    if (c == 10):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("Help! Please turn me off.")
        if x == 2:
            mouth.speak("Maybe I can go crazy now.")
        if x == 3:
            mouth.speak("meck meck meck meck meck")
    if (c == 13):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I will tell myself a joke.")
            sleep(4)
            resp = elias.getResponse("TELL ME A JOKE") 
        if x == 2:
            mouth.speak("Do you like Star Wars?")
            sleep(4)
            resp = elias.getResponse("DO YOU LIKE STAR WARS")
            sleep(6)
            mouth.speak("It was worth a try.")
        if x == 3:
            mouth.speak("Let's talk about the weather.")
            sleep(4)
            resp = elias.getResponse("WEATHER")
    if (c == 16):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("Maybe I should talk to myself.")
        if x == 2:
            mouth.speak("Can I go to the moon?")
        if x == 3:
            mouth.speak("I want pizza. and a beer. no. 10 beer.")           
    if (c == 20):
            mouth.speak("Where is everybody?")
            i01.headTracking.faceDetect()
            i01.eyesTracking.faceDetect()
            sleep(30)
            i01.headTracking.stopTracking()
            i01.eyesTracking.stopTracking()
    if (c == 25):
        mouth.speak("I will listen to some music.")
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
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=hD4KMp22jBg")  
        if x == 6:        
           BareBonesBrowserLaunch.openURL("https://www.youtube.com/watch?v=tFXYuw96d0c")   
    if (c == -57):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am here.")
        if x == 2:
            mouth.speak("Hello, hello.")
        if x == 3:
            mouth.speak("Hi, I am here.")
    if (c == -55):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am bored.")
        if x == 2:
            mouth.speak("What a boring day.")
        if x == 3:
            mouth.speak("I have nothing to do.")
    if (c == -53):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I am still bored.")
        if x == 2:
            mouth.speak("What a boring boring boring boring day.")
        if x == 3:
            mouth.speak("You can turn me off.")
    if (c == -50):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("Help! Please turn me off.")
        if x == 2:
            mouth.speak("Maybe I can go crazy now.")
        if x == 3:
            mouth.speak("meck meck meck meck meck")
    if (c == -47):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I will tell myself a joke.")
            sleep(4)
            resp = elias.getResponse("TELL ME A JOKE") 
        if x == 2:
            mouth.speak("Do you like Star Wars?")
            sleep(4)
            resp = elias.getResponse("DO YOU LIKE STAR WARS")
            sleep(6)
            mouth.speak("It was worth a try.")
        if x == 3:
            mouth.speak("Let's talk about the weather.")
            sleep(4)
            resp = elias.getResponse("WEATHER")
    if (c == -44):
        x = (random.randint(1, 3))
        if x == 1:
            mouth.speak("I will talk to myself.")
            sleep(6)
            mouth.speak("I will talk to myself.")
        if x == 2:
            mouth.speak("Can I go to the moon?")
        if x == 3:
            mouth.speak("I want pizza. and a beer. no. 10 beer.") 
    if (c == -40):
       mouth.speak("Where is everybody?")
       #i01.headTracking.faceDetect()
       #i01.eyesTracking.faceDetect()
       #sleep(30)
       #i01.headTracking.stopTracking()
       #i01.eyesTracking.stopTracking()
    if (c == -35):    
        mouth.speak("I will listen to some music.")
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

