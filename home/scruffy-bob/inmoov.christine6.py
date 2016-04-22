from java.lang import String
import random
import time

leftPort = "COM3"
rightPort = "COM4"
mic = 1
blind = 1
lastname = "None"
start = 0
greetinglist = ["Hello", "Hi", "Good to see you", "I think I see", "Howdy", "Good afternoon", "I may be able to recognize"]

# CameraIndex = 0 -> internal PC webcam, = 1 -> external webcam
cameraIndex = 1

def headfront():
    inMoov.head.neck.moveTo(45)
    inMoov.head.rothead.moveTo(110)

def eyesfront():
    inMoov.head.eyeX.moveTo(90)
    inMoov.head.eyeY.moveTo(45)

def randommovement():
    #
    # Pick a random servo, move it in a random direction
    #
    x = random.randint(1, 5)
    if (x==1) or (x==2):
        x = random.randint(-20,20)
        inMoov.head.neck.moveTo(inMoov.head.neck.getPos() + x)
    elif (x==3):
        x = random.randint(-30,30)
        inMoov.head.rothead.moveTo(inMoov.head.rothead.getPos() + x)
    elif (x==4):
        x = random.randint(-10,10)
        inMoov.head.eyeX.moveTo(inMoov.head.eyeX.getPos() + x)
    elif (x==5):
        x = random.randint(-5,5)
        inMoov.head.eyeY.moveTo(inMoov.head.eyeY.getPos() + x)  

def onFace(data):
    global lastname, start
    print "OnFace:", data
    randommovement()   
    #
    # Limit speaking to once every 10 seconds to prevent it from consuming all available time
    # and really becoming annoyings
    #

    end = time.time()
    elapsed = end - start
    if (elapsed > 5):
        if (lastname != data):
            x = random.randint(0, len(greetinglist))
            inMoov.mouth.speak(greetinglist[x]+data)
            lastname = data
            start = end
      
#
# Start the necessary services
#
# The keyboard can be used to input commands, see the input() function
#
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

#
# Starting InMoov itself
#
inMoov = Runtime.createAndStart("inMoov", "InMoov")

webgui = Runtime.createAndStart("webgui", "WebGui")
sleep(2)

#
# Wksr is the natural language processing part.  This takes speech input and translates
# it to text, then passes it on to other processes (alice and python)
#
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
sleep(2)

#
# Alice is the "chatbot".   It takes input from wksr and determines an appropriate response
# The response is fed to both the mouth
#
alice = Runtime.createAndStart("alice", "ProgramAB")
alice.startSession()
sleep(2)

#
# The htmlfilter simply strips off HTML tags from text being returned from the internet searches
#
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("inMoov.mouth", "AcapelaSpeech")
mouth.setVoice("peter")
sleep(2)

# We have two services listening to the input
# 1.   Alice the chatbot.  This will generally respond to anything necessary
# 2.   A Python function called onText() - This will be used to intercept
#      local commands for execution.   We SHOULD be getting all the text from
#      wksr, but for some reason, we're not.
wksr.addTextListener(alice)
wksr.addListener("publishText","python","onText")
sleep(2)

alice.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
sleep(2)

inMoov.startHead(leftPort)
sleep(2)

inMoov.startMouth()
inMoov.startMouthControl(leftPort)
sleep(2)

# For now, don't do eye tracking since we're doing facial recognition
#inMoov.startEyesTracking(leftPort)
#inMoov.startHeadTracking(leftPort)
#
# Tweak the eye tracking PID values
#
#inMoov.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
#inMoov.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
#inMoov.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
#inMoov.headTracking.pid.setPID("neck",12.0,5.0,0.1)

#
# Start by looking forward
#
headfront()
eyesfront()
inMoov.mouth.speak("InMoov ready for commands")

#
# Face recognition
# The onFace python function should be called whenever we see a new face.
#
inMoov.opencv.setCameraIndex(cameraIndex)
inMoov.opencv.capture()
fr=inMoov.opencv.addFilter("FaceRecognizer")
inMoov.opencv.setDisplayFilter("FaceRecognizer")
inMoov.opencv.addListener("publishRecognizedFace","python","onFace")
fr.train()# it takes some time to train and be able to recognize face

#while True:
#    sleep(random.randint(1,10))
#    randommovement()   


# Basic commands

def lookforward():
  inMoov.setHeadSpeed(0.65, 0.75)
  inMoov.moveHead(74,90)
 
def lookright():
  inMoov.setHeadSpeed(0.65, 0.75)
  inMoov.moveHead(60,150)

def input(cmd):
    print "Keyboard input:", cmd
    randommovement()   

    if (cmd == "Up"):
        inMoov.head.neck.moveTo(inMoov.head.neck.getPos() + 1)
        inMoov.head.eyeY.moveTo(inMoov.head.eyeY.getPos() + 1)

    if (cmd == "Down"):
        inMoov.head.neck.moveTo(inMoov.head.neck.getPos() - 1)
        inMoov.head.eyeY.moveTo(inMoov.head.eyeY.getPos() - 1)

    if (cmd == "Right"):
        inMoov.head.rothead.moveTo(inMoov.head.rothead.getPos() + 1)
        inMoov.head.eyeX.moveTo(inMoov.head.eyeX.getPos() + 1)            
  
    if (cmd == "Left"):
        inMoov.head.rothead.moveTo(inMoov.head.rothead.getPos() - 1)
        inMoov.head.eyeX.moveTo(inMoov.head.eyeX.getPos() - 1)

    if (cmd == "1"):
        headfront()
        eyesfront()    
    
    if (cmd == "Y"):
        inMoov.mouth.speak("yes")

    if (cmd == "N"):
        inMoov.mouth.speak("no")

    if (cmd == "D"):
        facetrack()

    if (cmd == "R"):
        facerecognize()

    if (cmd == "F"):
        inMoov.mouth.speak("goodbye")
        x = (random.randint(1, 4))
        if x == 1:
          inMoov.mouth.speak("see you soon")
        if x == 2:
          inMoov.mouth.speak("thanks for visiting me")
        if x == 3:
          inMoov.mouth.speak("i am so glad you stopped by")
        if x == 4:
          inMoov.mouth.speak("have a nice day")        

    if (cmd == "H"):
        hello()

    if (cmd == "I"):
        x = (random.randint(1, 5))
        if x == 1:
          inMoov.mouth.speak("hello")
        if x == 2:
          inMoov.mouth.speak("hi")
        if x == 3:
          inMoov.mouth.speak("welcome") 
        if x == 4:
          inMoov.mouth.speak("nice to meet you")
        if x == 5:
          inMoov.mouth.speak("what a lovely day")
        x = (random.randint(1, 4))
        if x == 1:
          inMoov.mouth.speak("i'm Jarvis")
        if x == 2:
          inMoov.mouth.speak("my name is Jarvis") 
        if x == 3:
          inMoov.mouth.speak("my name is Jarvis")
        if x == 4:
          inMoov.mouth.speak("i'm Jarvis")
          
        if (cmd == "M"):
          global mic
          if mic == 1:
            ear.lockOutAllGrammarExcept("robin")
            inMoov.mouth.speak("i'm not listening")
            mic = 0
          elif mic == 0:
            ear.clearLock()
            inMoov.mouth.speak("i can hear again")
            global mic
            mic = 1

def hello():
  randommovement()   

  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("hello")
  if x == 2:
      inMoov.mouth.speak("hi")
  if x == 3:
      inMoov.mouth.speak("welcome") 
  if x == 4:
      inMoov.mouth.speak("nice to meet you")
  if x == 5:
      inMoov.mouth.speak("what a lovely day")

  randommovement()   

  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("i'm glad i have your attention")
  if x == 2:
      inMoov.mouth.speak("i'm Jarvis")
  if x == 3:
      inMoov.mouth.speak("my name is Jarvis") 
  if x == 4:
      inMoov.mouth.speak("i'm a inmoov robot")
  if x == 5:
      inMoov.mouth.speak("i'm made in the U S A")

  randommovement()   

  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("i'm a humanoid robot")
  if x == 2:
      inMoov.mouth.speak("my body is made of plastic")
  if x == 3:
      inMoov.mouth.speak("i'm 3 d printed") 
  if x == 4:
      inMoov.mouth.speak("my robot lab is the software that controls me") 
  if x == 5:
      inMoov.mouth.speak("there are 2 arduino mega microprocessors on my back") 
  randommovement()   

  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("i have voice synthesis")
  if x == 2:
      inMoov.mouth.speak("i have cameras in my eyes")
  if x == 3:
      inMoov.mouth.speak("i have a kinect in my chest") 
  if x == 4:
      inMoov.mouth.speak("i have voice recognition capabilities") 
  if x == 5:
      inMoov.mouth.speak("i am connected to the internet")

  randommovement()   

  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("and i have a lot of servos")
  if x == 2:
      inMoov.mouth.speak("and can be controlled from a keyboard")
  if x == 3:
      inMoov.mouth.speak("and microphones in my ears") 
  if x == 4:
      inMoov.mouth.speak("and i have facial recognition capabilities")
  if x == 5:
      inMoov.mouth.speak("and a computer on my back")

  randommovement()   
     
  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("i can move very human like")
  if x == 2:
      inMoov.mouth.speak("please take a look at my mechanics")
  if x == 3:
      inMoov.mouth.speak("i'm a open source project") 
  if x == 4:
      inMoov.mouth.speak("please take a look at my electronics") 
  if x == 5:
      inMoov.mouth.speak("we can be friends on facebook")
  randommovement()   
    
  x = (random.randint(1, 5))
  if x == 1:
      inMoov.mouth.speak("you can ask my maker if you have any questions")
  if x == 2:
      inMoov.mouth.speak("this is great")
  if x == 3:
      inMoov.mouth.speak("i really like being here") 
  if x == 4: 
      inMoov.mouth.speak("i am having so much fun") 
  if x == 5:
      inMoov.mouth.speak("take a look on my videos on youtube")

def onText(data):
     print "onText()", data
     randommovement()   

     if (data == "start face recognition"):
         # Bring up the facial recognition
         inMoov.detach()

     if (data == "stop face recognition"):
         # Bring up the facial recognition
         inMoov.detach()

     if (data == "start face detection"):
         # Bring up the facial detection
         inMoov.detach()

     if (data == "stop face detection"):
         # Bring up the facial recognition
         inMoov.detach()

     if (data == "detach") or (data == "disconnect"):
         inMoov.detach()
         
     if (data == "attach") or (data == "connect"):
         inMoov.attach()
         
     if (data == "look forward"):
         headfront()
         eyesfront()
         
     if (data == "look to your left") or (data == " look to your left"):
         headleft()
         
     if (data == "look to your right") or (data == " look to your right"):
         headright()
         
     if (data == "look up") or (data == " look up"):
         headup()
         
     if (data == "look down") or (data == " look down"):
         headdown()
         
     if (data == "who are you") or (data == " who are you"):
         madeby2()
         
     if (data == "tell me something about yourself") or (data == " tell me something about yourself"):
         hello()

def madeby2():
    inMoov.moveHead(80,86)
    #inMoov.moveArm("left",5,90,30,10)
    #inMoov.moveArm("right",5,90,30,10)
    #inMoov.moveHand("left",45,40,30,25,35,90)
    #inMoov.moveHand("right",55,2,50,48,30,90)
    #inMoov.moveTorso(90,90,90)
    sleep(2)
    inMoov.moveHead(80,98)
    #inMoov.moveArm("left",5,90,30,10)
    #inMoov.moveArm("right",5,90,30,10)
    #inMoov.moveHand("left",45,40,30,25,35,90)
    #inMoov.moveHand("right",55,2,50,48,30,90)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(90,89)
    #inMoov.moveArm("left",42,104,30,10)
    #inMoov.moveArm("right",33,116,30,10)
    #inMoov.moveHand("left",45,40,30,25,35,120)
    #inMoov.moveHand("right",55,2,50,48,30,40)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(80,98)
    #inMoov.moveArm("left",5,99,30,16)
    #inMoov.moveArm("right",5,94,30,16)
    #inMoov.moveHand("left",120,116,110,115,98,73)
    #inMoov.moveHand("right",114,146,125,113,117,109)
    #inMoov.moveTorso(90,90,90)
    madeby3()

def madeby3():
    inMoov.moveHead(68,90)
    #inMoov.moveArm("left",5,99,30,16)
    #inMoov.moveArm("right",85,102,38,16)
    #inMoov.moveHand("left",120,116,110,115,98,73)
    #inMoov.moveHand("right",114,146,161,132,168,19)
    #inMoov.moveTorso(90,90,90)
    sleep(0.5)
    ##inMoov.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    ##inMoov.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    #inMoov.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    #inMoov.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    ##inMoov.setHeadSpeed(1.0, 0.90)
    ##inMoov.setTorsoSpeed(1.0, 1.0, 1.0)
    inMoov.moveHead(87,94)
    #inMoov.moveArm("left",5,99,36,16)
    #inMoov.moveArm("right",81,105,42,16)
    #inMoov.moveHand("left",120,116,110,115,98,50)
    #inMoov.moveHand("right",114,118,131,132,168,19)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.mouth.speakBlocking("I was originally created by gael langevin")
    #inMoov.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    #inMoov.setHandSpeed("right", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    #inMoov.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    #inMoov.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    ##inMoov.setHeadSpeed(1.0, 0.90)
    ##inMoov.setTorsoSpeed(1.0, 1.0, 1.0)
    inMoov.moveHead(105,94)
    #inMoov.moveArm("left",5,99,36,16)
    #inMoov.moveArm("right",81,105,42,16)
    #inMoov.moveHand("left",120,116,110,115,98,50)
    #inMoov.moveHand("right",114,118,131,132,168,19)
    #inMoov.moveTorso(90,90,90)
    sleep(0.2)
    inMoov.moveHead(80,86)
    #inMoov.moveArm("left",5,96,25,10)
    #inMoov.moveArm("right",5,94,26,10)
    #inMoov.moveHand("left",110,62,56,88,81,18)
    #inMoov.moveHand("right",78,88,101,95,81,137)
    #inMoov.moveTorso(90,90,90)
    sleep(0.2)
    inMoov.moveHead(75,97)
    #inMoov.moveArm("left",85,106,25,18)
    #inMoov.moveArm("right",87,107,32,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",78,88,101,95,81,27)
    #inMoov.moveTorso(90,90,90)
    inMoov.mouth.speakBlocking("who is a french sculptor, designer")
    sleep(0.5)
    inMoov.moveHead(80,86)
    #inMoov.moveArm("left",5,96,25,10)
    #inMoov.moveArm("right",5,94,26,10)
    #inMoov.moveHand("left",110,62,56,88,81,18)
    #inMoov.moveHand("right",78,88,101,95,81,137)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(75,97)
    #inMoov.moveArm("left",6,91,22,14)
    #inMoov.moveArm("right",87,107,32,18)
    #inMoov.moveHand("left",110,62,56,88,81,0)
    #inMoov.moveHand("right",78,88,101,95,81,27)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(20,69)
    #inMoov.moveArm("left",6,91,22,14)
    #inMoov.moveArm("right",87,107,32,21)
    #inMoov.moveHand("left",110,62,56,88,81,0)
    #inMoov.moveHand("right",78,88,101,95,81,27)
    #inMoov.moveTorso(90,90,90)
    inMoov.mouth.speakBlocking("I am totally build with 3 D printed parts")
    inMoov.moveHead(75,97)
    #inMoov.moveArm("left",85,106,25,18)
    #inMoov.moveArm("right",87,107,32,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",78,88,101,95,81,27)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(33,110)
    #inMoov.moveArm("left",85,104,25,18)
    #inMoov.moveArm("right",87,41,47,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",111,75,117,125,111,143)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.moveHead(62,102)
    #inMoov.moveArm("left",85,104,25,18)
    #inMoov.moveArm("right",87,41,47,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",111,75,117,125,111,143)
    #inMoov.moveTorso(90,90,90)
    inMoov.mouth.speakBlocking("which means all my parts")
    inMoov.moveHead(79,88)
    #inMoov.moveArm("left",85,104,25,18)
    #inMoov.moveArm("right",87,59,46,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",59,75,117,125,111,113)
    #inMoov.moveTorso(90,90,90)
    inMoov.mouth.speakBlocking("are made on a home 3 D printer")
    sleep(1)
    inMoov.moveHead(40,84)
    #inMoov.moveArm("left",85,72,38,18)
    #inMoov.moveArm("right",87,64,47,18)
    #inMoov.moveHand("left",124,97,66,120,130,35)
    #inMoov.moveHand("right",59,75,117,125,111,113)
    #inMoov.moveTorso(90,90,90)
    inMoov.mouth.speakBlocking("each parts are design to fit 12 centimeter cube build area")
    sleep(1)
    inMoov.moveHead(97,80)
    #inMoov.moveArm("left",85,79,39,14)
    #inMoov.moveArm("right",87,76,42,12)
    #inMoov.moveHand("left",124,97,66,120,130,35)
    #inMoov.moveHand("right",59,75,117,125,111,113)
    #inMoov.moveTorso(90,90,90)
    sleep(0.5)
    inMoov.moveHead(75,97)
    #inMoov.moveArm("left",85,106,25,18)
    #inMoov.moveArm("right",87,107,32,18)
    #inMoov.moveHand("left",110,62,56,88,81,145)
    #inMoov.moveHand("right",78,88,101,95,81,27)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.mouth.speakBlocking("so anyone can reproduce me")
    #fullspeed()
    inMoov.moveHead(80,98)
    #inMoov.moveArm("left",5,90,30,10)
    #inMoov.moveArm("right",5,90,30,10)
    #inMoov.moveHand("left",45,40,30,25,35,90)
    #inMoov.moveHand("right",55,2,50,48,30,90)
    #inMoov.moveTorso(90,90,90)
    sleep(1)
    inMoov.mouth.speakBlocking("cool, don't you think")
    #armsdown()

def relax():
  inMoov.moveHead(79,100,90,90,70)
  
def headfront():
    inMoov.head.neck.moveTo(90)
    inMoov.head.rothead.moveTo(80)

def headdown():
    inMoov.head.neck.moveTo(20)

def headupp():
    inMoov.head.neck.moveTo(160)
    
def headright():
    inMoov.head.rothead.moveTo(30)
    
def headleft():
    inMoov.head.rothead.moveTo(140)

def eyesfront():
    inMoov.head.eyeX.moveTo(70)
    inMoov.head.eyeY.moveTo(65)
    
def eyesfrontY():
    inMoov.head.eyeY.moveTo(65)

def eyesfrontX():
    inMoov.head.eyeX.moveTo(70)
    
def eyesdown():
    inMoov.head.eyeY.moveTo(100)
    
def eyesupp():
    inMoov.head.eyeY.moveTo(50)

def eyesright():
    inMoov.head.eyeX.moveTo(60)

def eyesleft():
    inMoov.head.eyeX.moveTo(100)

def facetrack():
    global blind
    if blind == 1:
        trackHumans()
        blind = 0  
    elif blind == 0:
        stopTracking()
        global blind
        blind = 1

def trackHumans():
     inMoov.mouth.speak("facetrack on")
     inMoov.headTracking.faceDetect()
     
def trackPoint():
     inMoov.headTracking.startLKTracking()
     inMoov.eyesTracking.startLKTracking()
     fullspeed()

def stopTracking():
     inMoov.mouth.speak("facetrack off")
     inMoov.headTracking.stopTracking()
     inMoov.eyesTracking.stopTracking()


