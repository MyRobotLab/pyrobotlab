# File : Robyn Inmoov

import random

#create a Serial service named serial
serial = Runtime.createAndStart("serial","Serial")
serial.connect('COM7')

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

leftPort = "COM3"
rightPort = "COM6"

i01 = Runtime.createAndStart("i01", "InMoov")

i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

right.setBoard("mega2560") # atmega168 | mega2560 | etc

thumbgripp = Runtime.create("thumbgripp","Servo")
thumbfine = Runtime.create("thumbfine","Servo")
indexfine = Runtime.create("indexfine","Servo")
majeurefine = Runtime.create("majeurefine","Servo")

thumbgripp.startService()
thumbfine.startService()
indexfine.startService()
majeurefine.startService()

thumbgripp.attach("i01.left", 30)  # thumbgripp
thumbfine.attach("i01.left", 31)  # thumbfine
indexfine.attach("i01.left", 32)  # indexfine
majeurefine.attach("i01.left", 33)  # majeurefine

thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)

i01.mouth.speak("okay you can do a system check now")
sleep(3)
#############################################################################################

i01.mouth.setVoice("Laura")

######################################################################
# Markus Mod

i01.leftArm.omoplate.map(10,80,65,15)
i01.rightArm.omoplate.map(10,80,80,15)
i01.leftArm.shoulder.map(0,180,170,15)
i01.rightArm.shoulder.map(0,180,190,50)
i01.leftArm.rotate.map(40,180,155,20)
i01.rightArm.rotate.map(40,180,155,20)
i01.leftArm.bicep.map(5,90,90,20)
i01.rightArm.bicep.map(5,90,90,20)
i01.head.rothead.map(30,150,150,30)
i01.torso.topStom.map(60,120,83,118)
i01.head.eyeX.setMinMax(50,100)
i01.head.eyeX.map(60,100,55,100)
#lefteye.setMinMax(40,90)
#lefteye.map(60,100,40,90)
i01.head.eyeY.map(50,100,95,60)
i01.head.neck.map(20,160,160,20)
i01.leftHand.thumb.map(0,180,20,160)
i01.leftHand.index.map(0,180,30,160)
i01.leftHand.majeure.map(0,180,0,170)
i01.leftHand.ringFinger.map(0,180,0,120)
i01.leftHand.pinky.map(0,180,40,180)

i01.rightHand.thumb.map(0,180,160,20)
i01.rightHand.index.map(0,180,160,20)
i01.rightHand.majeure.map(0,180,190,40)
i01.rightHand.ringFinger.map(0,180,0,180)
i01.rightHand.pinky.map(0,180,0,140)

thumbfine.map(0,180,138,0)
indexfine.map(0,180,138,0)
majeurefine.map(0,180,138,0)

############################################################

mem = 1

openclosehands = 3

##################################################################
# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.9, 0.9)
i01.setTorsoSpeed(1.0, 1.0, 1.0)
i01.moveArm("left",5,90,30,10)
i01.moveArm("right",5,90,30,15)
i01.moveTorso(90,90,90)
thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)

i01.mouth.speak("working on full speed")

##########################################################################################

def input(cmd):

    if (cmd == "R"):
        if openclosehands == 1:
            righthandopen()
            global openclosehands
            openclosehands = 2
        elif openclosehands == 2:
            lefthandopen()
            global openclosehands
            openclosehands = 3
        elif openclosehands == 3:
            righthandclose()
            global openclosehands
            openclosehands = 4
        elif openclosehands == 4:
            lefthandclose()
            global openclosehands
            openclosehands = 1
            
    if (cmd == "Upp"):
        i01.head.neck.moveTo(i01.head.neck.getPos() + 1)
        i01.head.eyeY.moveTo(i01.head.eyeY.getPos() + 1)

    if (cmd == "Nedpil"):
        i01.head.neck.moveTo(i01.head.neck.getPos() - 1)
        i01.head.eyeY.moveTo(i01.head.eyeY.getPos() - 1)

    if (cmd == u"Vänster"):
        i01.head.rothead.moveTo(i01.head.rothead.getPos() + 1)
        i01.head.eyeX.moveTo(i01.head.eyeX.getPos() + 1)            
  
    if (cmd == u"Höger"):
        i01.head.rothead.moveTo(i01.head.rothead.getPos() - 1)
        i01.head.eyeX.moveTo(i01.head.eyeX.getPos() - 1)

    if (cmd == "1"):
        headfront()
        eyesfront()  

    if (cmd == "Q"):               
        serial.write("7")              

    if (cmd == "E"):
        serial.write("9")
                                 
    if (cmd == "W"):
        serial.write("8")    

    if (cmd == "Z"):
        serial.write("2")

    if (cmd == "A"):
        serial.write("4")    
     
    if (cmd == "D"):
        serial.write("6")

    if (cmd == "S"):
        serial.write("5")     
    
    if (cmd == "Y"):
        i01.mouth.speak("yes")

    if (cmd == "F"):
        i01.mouth.speak("goodbye")
        x = (random.randint(1, 4))
        if x == 1:
          i01.mouth.speak("see you soon")
        if x == 2:
          i01.mouth.speak("thanks for visiting me")
        if x == 3:
          i01.mouth.speak("i am so glad you stopped by")
        if x == 4:
          i01.mouth.speak("have a nice day")
                    
    if (cmd == "N"):
        i01.mouth.speak("no")

    if (cmd == "H"):
        hello()

    if (cmd == "I"):
        x = (random.randint(1, 5))
        if x == 1:
          i01.mouth.speak("hello")
        if x == 2:
          i01.mouth.speak("hi")
        if x == 3:
          i01.mouth.speak("welcome") 
        if x == 4:
          i01.mouth.speak("nice to meet you")
        if x == 5:
          i01.mouth.speak("what a lovely day")
        x = (random.randint(1, 4))
        if x == 1:
          i01.mouth.speak("i'm robyn inmoov")
        if x == 2:
          i01.mouth.speak("my name is robyn") 
        if x == 3:
          i01.mouth.speak("my name is robyn inmoov")
        if x == 4:
          i01.mouth.speak("i'm robyn") 
                              
    if (cmd == "X"):
        pose()

    if (cmd == "T"):
        armsdown()
       
############################################################
    
def pose(): 
    i01.setHeadSpeed(0.9, 0.9)
    x = (random.randint(1, 6))
    if mem == x:
      pose()
    if x == 1:
      i01.moveHead(90,145,80,90,10)
      i01.moveArm("left",85,159,32,70)
      i01.moveArm("right",55,50,35,40)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 2:
      i01.moveHead(90,90,80,90,10)
      i01.moveArm("left",85,159,32,70)
      i01.moveArm("right",70,159,35,70)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 3:
      i01.moveHead(90,31,80,90,10)
      i01.moveArm("left",65,41,32,45)
      i01.moveArm("right",70,159,35,70)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 4:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",65,41,32,45)
      i01.moveArm("right",70,48,35,50)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 5:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",65,67,44,20)
      i01.moveArm("right",40,84,38,20)
      i01.moveHand("left",0,0,0,0,0,90)
      i01.moveHand("right",180,180,180,180,180,90)
      i01.moveTorso(90,90,90)
    if x == 6:
      i01.moveHead(90,81,80,90,10)
      i01.moveArm("left",90,83,70,20)
      i01.moveArm("right",75,100,62,20)
      i01.moveHand("left",0,0,0,0,0,90)
      i01.moveHand("right",0,0,0,0,0,90)
      i01.moveTorso(90,90,90)
    global mem
    mem = x 
          
##########################################################################################

def hello():
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("hello")
  if x == 2:
      i01.mouth.speak("hi")
  if x == 3:
      i01.mouth.speak("welcome") 
  if x == 4:
      i01.mouth.speak("nice to meet you")
  if x == 5:
      i01.mouth.speak("what a lovely day")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i'm glad i have your attention")
  if x == 2:
      i01.mouth.speak("i'm robyn inmoov")
  if x == 3:
      i01.mouth.speak("my name is robyn") 
  if x == 4:
      i01.mouth.speak("i'm a inmoov robot")
  if x == 5:
      i01.mouth.speak("i'm made in sweden")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i'm a humanoid robot")
  if x == 2:
      i01.mouth.speak("my body is made of plastic")
  if x == 3:
      i01.mouth.speak("i'm 3 d printed") 
  if x == 4:
      i01.mouth.speak("my robot lab is the software that controls me") 
  if x == 5:
      i01.mouth.speak("there are 2 arduino mega on my back") 

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i have pressure sensors on my forearms")
  if x == 2:
      i01.mouth.speak("i have cameras in my eyes")
  if x == 3:
      i01.mouth.speak("i have a kinect in my chest") 
  if x == 4:
      i01.mouth.speak("i have voice recognition") 
  if x == 5:
      i01.mouth.speak("i have mecanum wheels")

  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("and i have a lot of servos")
  if x == 2:
      i01.mouth.speak("and can be controlled from a keyboard")
  if x == 3:
      i01.mouth.speak("and microphones in my ears") 
  if x == 4:
      i01.mouth.speak("and i have face recognition")
  if x == 5:
      i01.mouth.speak("and a computer on my back")
      
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("i can move very human like")
  if x == 2:
      i01.mouth.speak("please take a look at my mechanics")
  if x == 3:
      i01.mouth.speak("i'm a open source project") 
  if x == 4:
      i01.mouth.speak("please take a look at my electronics") 
  if x == 5:
      i01.mouth.speak("we can be friends on facebook")
      
  x = (random.randint(1, 5))
  if x == 1:
      i01.mouth.speak("you can ask my maker if you have any questions")
  if x == 2:
      i01.mouth.speak("this is great")
  if x == 3:
      i01.mouth.speak("i really like being here") 
  if x == 4: 
      i01.mouth.speak("i am having so much fun") 
  if x == 5:
      i01.mouth.speak("take a look on my videos on youtube")
##########################################################################################

def handopen():
    i01.moveHand("left",0,0,0,0,0)
    i01.moveHand("right",0,0,0,0,0)

def lefthandopen():
    i01.moveHand("left",0,0,0,0,0)

def righthandopen():
    i01.moveHand("right",0,0,0,0,0)

def handclose():
    i01.setHandSpeed("right", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("left", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    i01.moveHand("right",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    i01.moveHand("right",180,180,180,180,180)

def lefthandclose():
    i01.setHandSpeed("left", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("left",180,180,180,180,180)

def righthandclose():
    i01.setHandSpeed("right", 0.8, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("right",180,180,180,180,180)
    sleep (0.3)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.moveHand("right",180,180,180,180,180)

def headfront():
    i01.head.neck.moveTo(90)
    i01.head.rothead.moveTo(80)

def eyesfront():
    i01.head.eyeX.moveTo(70)
    i01.head.eyeY.moveTo(85)
        
def armsdown():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,15)

def fullspeed():
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
            
##########################################################################################
    
