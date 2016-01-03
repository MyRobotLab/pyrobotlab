sleep(1)#file : InMoov2.Robyn Inmoov

import random


keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

 
leftPort = "COM3"
rightPort = "COM7"

 
i01 = Runtime.createAndStart("i01", "InMoov")


cleverbot = Runtime.createAndStart("cleverbot","CleverBot")

# starts everything
i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")




#############################################################################################
# Markus Mod

i01.leftArm.omoplate.map(10,80,80,20)
i01.rightArm.omoplate.map(10,80,80,10)
i01.leftArm.shoulder.map(0,180,170,15)
i01.rightArm.shoulder.map(0,180,190,50)
i01.leftArm.rotate.map(40,180,140,20)
i01.rightArm.rotate.map(40,180,140,20)
i01.leftArm.bicep.map(5,90,90,20)
i01.rightArm.bicep.map(5,90,90,20)
i01.head.rothead.map(30,150,150,30)
i01.torso.topStom.map(60,120,70,110)
i01.head.eyeX.map(60,100,90,50)
i01.head.eyeY.map(50,100,100,50)
i01.head.neck.map(20,160,160,20)

############################################################
#to tweak the default PID values
i01.headTracking.xpid.setPID(10.0,5.0,0.1)
i01.headTracking.ypid.setPID(10.0,5.0,0.1)
i01.eyesTracking.xpid.setPID(15.0,5.0,0.1)
i01.eyesTracking.ypid.setPID(15.0,5.0,0.1)
############################################################



Pin27 = 27


right.digitalReadPollingStart(Pin27)

# make friendly sample rate
right.setSampleRate(3000)

right.addListener("publishPin", "python", "publishPin")


def publishPin(pin):
#  print pin.pin, pin.value, pin.type, pin.source,

 
  if (pin.pin == 27 and pin.value == 1):
      if pin12 == 0:
          i01.mouth.speak("hello")
          global pin12
          pin12 = 1
          i01.head.attach()
          sleep(1)
          ear.clearLock()
          headfront()
          sleep(2)
          trackHumans()

#  if (pin.pin == 12 and pin.value == 0):
#      if pin12 == 1:
#          global resttimer
#          resttimer += 1
#          if resttimer == 400:
#              global resttimer
#              resttimer = 0
#              gotosleepnow() 
             
#############################################################################################

time = 0
 
pin12 = 1
#resttimer = 0

rest = 0

blind = 1

kinect = 0

dance1 = 1
dance2 = 1

helvar = 1
mic = 1

nexagroup = 1
nexa1 = 0
nexa2 = 0
nexa3 = 0
nexa4 = 0
nexa5 = 0
nexa6 = 0
nexa7 = 0
nexa8 = 0
nexa9 = 0
nexa10 = 0
nexa11 = 0
nexa12 = 0
nexa13 = 0
nexa14 = 0
nexa15 = 0
nexa16 = 0

l1="m"
l2="a"
l3="r"
l4="k"
l5="u"
l6="s"

name = l1+l2+l3+l4+l5+l6

# play rock paper scissors
robyn = 0
human = 0

i01.systemCheck()

ear = i01.ear



##################################################################
# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.8, 0.8)
i01.mouth.speak("working on full speed")

##################################################################

# commands with i01.getName() use the InMoov service methods
ear.addCommand("attach head", "i01.head", "attach")
ear.addCommand("disconnect head", "i01.head", "detach")
ear.addCommand("attach eyes", "i01.head.eyeY", "attach")
ear.addCommand("disconnect eyes", "i01.head.eyeY", "detach")
ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("attach left hand", "i01.leftHand", "attach")
ear.addCommand("disconnect left hand", "i01.leftHand", "detach")
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach left arm", "i01.leftArm", "attach")
ear.addCommand("disconnect left arm", "i01.leftArm", "detach")
ear.addCommand("attach right arm", "i01.rightArm", "attach")
ear.addCommand("disconnect right arm", "i01.rightArm", "detach")
ear.addCommand("let's do some exercise", "python", "startkinect")
ear.addCommand("you can stop now", "python", "offkinect")
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("servo", "python", "servos")

 
ear.addCommand("power down", i01.getName(), "powerDown")
ear.addCommand("power up", i01.getName(), "powerUp")
 
ear.addCommand("camera on", i01.getName(), "cameraOn")
ear.addCommand("off camera", i01.getName(), "cameraOff")
ear.addCommand("capture gesture", i01.getName(), "captureGesture")
 
# FIXME - lk tracking setpoint
ear.addCommand("track", i01.getName(), "track")
ear.addCommand("freeze track", i01.getName(), "clearTrackingPoints")
ear.addCommand("giving", i01.getName(), "giving")
ear.addCommand("be a fighter", i01.getName(), "fighter")
ear.addCommand("victory", i01.getName(), "victory")
ear.addCommand("arms up", i01.getName(), "armsUp")
ear.addCommand("arms front", i01.getName(), "armsFront")
ear.addCommand("da vinci", i01.getName(), "daVinci")

 
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("stop listening", ear.getName(), "stopListening")
 
##sets the servos back to full speed, anywhere in sequence or gestures
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("search humans", "python", "trackHumans")
ear.addCommand("go blind", "python", "stopTracking")
ear.addCommand("relax", "python", "relax")
ear.addCommand("perfect", "python", "perfect")
ear.addCommand("finger", "python", "finger")
ear.addCommand("how many fingers do you have", "python", "howmanyfingersdoihave")

# play rock paper scissors
ear.addCommand("let's play rock paper scissors", "python", "rockpaperscissors")

ear.addCommand("arms down", "python", "armsdown")
ear.addCommand("torso", "python", "Torso")
ear.addCommand("move eye", "python", "moveeye")
ear.addCommand("move your mouth", "python", "movemouth")
ear.addCommand("disco time", "python", "discotime")
ear.addCommand("move your head", "python", "movehead")
ear.addCommand("sing little teapot", "python", "littleteapot")

ear.addComfirmations("yes","correct","ya") 
ear.addNegations("no","wrong","nope","nah")
 
ear.startListening("a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | turn on number four |turn off number four  | turn on number three | turn off number three  | turn on number two | turn off number two  | turn on number one | turn off number one  | let's play again | take a rest | shut down your system | do something | do something else | be quiet | turn off the light in your stomach | red light | green light | blue light | wake up robyn | good night robyn | go to sleep now | yes | no thanks | yes let's play again | i have rock | i have paper | i have scissors | look at the people | take a look around | good morning | very good | look to your right | look to your left |look down |look up |look strait forward |how are you | sorry | robyn | can i have your attention | hello robyn | bye bye | i love you | thanks | thank you | nice | goodbye")
 
# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", "python", "heard")


##########################################################################################



# play rock paper scissors




def rockpaperscissors():
    fullspeed()
    i01.mouth.speak("lets play first to 3 points win")
    sleep(4)
    rockpaperscissors2()
    
def rockpaperscissors2():
    fullspeed()
    ear.lockOutAllGrammarExcept("i have rock")  
    ear.lockOutAllGrammarExcept("i have paper")
    ear.lockOutAllGrammarExcept("i have scissors") 
    x = (random.randint(1, 3))
    if x == 1:
        ready()
        sleep(2)
        rock()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("oh no")
            if x == 2:
                i01.mouth.speak("that don't work")
            if x == 3:
                i01.mouth.speak("no points")
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("paper beats rock")
            if x == 2:
                i01.mouth.speak("your point")
            if x == 3:
                i01.mouth.speak("you got this one")
            global human
            human += 1
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("1 point for me")
            if x == 2:
                i01.mouth.speak("going fine")
            if x == 3:
                i01.mouth.speak("rock beats scissors")
            global robyn
            robyn += 1
            sleep(1)
       
           
    if x == 2:
        ready()
        sleep(2)
        paper()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("1 point")
            if x == 2:
                i01.mouth.speak("paper beats rock")
            if x == 3:
                i01.mouth.speak("my point")
            global robyn
            robyn += 1
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("no points")
            if x == 2:
                i01.mouth.speak("ok lets try again")
                sleep(2)
            if x == 3:
                i01.mouth.speak("again")
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("oh no you get 1 point")
            if x == 2:
                i01.mouth.speak("this is not good for me")
            if x == 3:
                i01.mouth.speak("your point")
            global human
            human += 1
            sleep(1)
        
    if x == 3:
        ready()
        sleep(2)
        scissors()
        sleep(2)
        data = msg_i01_ear_recognized.data[0]
        if (data == "i have rock"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("oh no")
            if x == 2:
                i01.mouth.speak("rock beats scissors")
            if x == 3:
                i01.mouth.speak("i feel generous today")
            global human
            human += 1
            sleep(1)
        if (data == "i have paper"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("i've got you")
            if x == 2:
                i01.mouth.speak("my point")
            if x == 3:
                i01.mouth.speak("good")
            global robyn
            robyn += 1
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("no no")
            if x == 2:
                i01.mouth.speak("that don't work")
            if x == 3:
                i01.mouth.speak("no points")
            sleep(1)
    if robyn == 3 or human == 3:
        stoprockpaperscissors() 
 #   if robyn > 4 or human > 4:
 #       i01.mouth.speak("sorry there must have been something wrong with my counting")
 #       sleep(5)
 #       stoprockpaperscissors()          
    rockpaperscissors2()

            
def stoprockpaperscissors():
    armsdown()
    handopen()
    if robyn < human:
        i01.mouth.speak("congratulations you won with" + str(human - robyn) + "points")
        sleep(5)
        i01.mouth.speak(str(human) + "points to you and" + str(robyn) + "points to me")
    if robyn > human:
        i01.mouth.speak("yes yes i won with" + str(robyn - human) + "points")
        sleep(5)
        i01.mouth.speak("i've got " + str(robyn) + "points and you got" + str(human) + "points")
    if robyn == human:
        i01.mouth.speak("none of us won we both got" + str(robyn) + "points")
    global robyn
    robyn = 0
    global human
    human = 0
    ear.clearLock()
    i01.mouth.speak("that was fun")
    sleep(3)
    i01.mouth.speak("do you want to play again")
    sleep(8)
    data = msg_i01_ear_recognized.data[0]
    if (data == "yes let's play again"):
        rockpaperscissors2()
    if (data == "yes"):
        rockpaperscissors2()
    if (data == "no thanks"):
        i01.mouth.speak("maybe some other time then")
    else:
        i01.mouth.speak("ok i'll find something else to do")
    lookaroundyou()
        

def ready():
    i01.mouth.speak("ready")
    i01.mouth.speak("go")
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",65,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",100,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    
    

def rock():
    
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    
    sleep(.3)
    
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have rock what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")


def paper():
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",0,0,0,0,0,165)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have paper what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")



def scissors():
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(0.8,0.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",180,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",50,0,0,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have scissors what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")



##########################################################################################


def input(cmd):
    
    # print 'python object is',msg_[service]_[method]
    cmd = msg_keyboard_keyCommand.data[0]
    print 'python data is', cmd
    
    if (cmd == "C"):
        i01.mouth.audioFile.playFile("C:\Users\Markus\Music\markustest.mp3", False)
        sleep(12.0)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.23)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.17)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.68)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(1.44)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.2)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.22)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.59)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.22)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.27)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.65)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.61)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.68)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(12.91)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.14)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.26)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.59)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(1.46)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.16)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.22)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.61)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.16)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.25)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.69)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.66)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)
        sleep(0.62)
        i01.head.jaw.moveTo(50)
        sleep(0.2)
        i01.head.jaw.moveTo(10)




    if (cmd == "T"):
        talk()

    if (cmd == "R"):
        if rest == 0:
            shutdownyoursystem()
           
        elif rest == 1:
            robyn()
            

    if (cmd == "W"):
      i01.head.neck.moveTo(i01.head.neck.getPosFloat() + 1)

    if (cmd == "Z"):
      i01.head.neck.moveTo(i01.head.neck.getPosFloat() - 1)

    if (cmd == "A"):
      i01.head.rothead.moveTo(i01.head.rothead.getPosFloat() + 1)
    
    if (cmd == "D"):
      i01.head.rothead.moveTo(i01.head.rothead.getPosFloat() - 1)

    if (cmd == "S"):
      headfront()
       
    if (cmd == "K"):
        if kinect == 0:
            startkinect()
        elif kinect == 1:
            offkinect()

    if (cmd == "B"):
        if blind == 1:
            trackHumans()
        elif blind == 0:
            stopTracking()

    if (cmd == "Q"):
        i01.rightArm.shoulder.moveTo(i01.rightArm.shoulder.getPosFloat() + 0.5)
        

    if (cmd == "P"):
        discotime()

#################################################

    if (cmd == "5"):
        if nexagroup == 1:
            i01.mouth.speakBlocking("nexa group 2")
            global nexagroup
            nexagroup = 2
        elif nexagroup == 2:
            i01.mouth.speakBlocking("nexa group 3")
            global nexagroup
            nexagroup = 3
        elif nexagroup == 3:
            i01.mouth.speakBlocking("nexa group 4")
            global nexagroup
            nexagroup = 4
        elif nexagroup == 4:
            i01.mouth.speakBlocking("nexa group 1")
            global nexagroup
            nexagroup = 1
           

    if (cmd == "1"):
        if nexagroup == 1:
            if nexa1 == 0:
                nexa1on()
            elif nexa1 == 1:
                nexa1off()
        elif nexagroup == 2:
            if nexa5 == 0:
                nexa5on()
            elif nexa5 == 1:
                nexa5off()
        elif nexagroup == 3:
            if nexa9 == 0:
                nexa9on()
            elif nexa9 == 1:
                nexa9off()
        elif nexagroup == 4:
            if nexa13 == 0:
                nexa13on()
            elif nexa13 == 1:
                nexa13off()
                
    if (cmd == "2"):
        if nexagroup == 1:
            if nexa2 == 0:
                nexa2on()
            elif nexa2 == 1:
                nexa2off()
        elif nexagroup == 2:
            if nexa6 == 0:
                nexa6on()
            elif nexa6 == 1:
                nexa6off()
        elif nexagroup == 3:
            if nexa10 == 0:
                nexa10on()
            elif nexa10 == 1:
                nexa10off()
        elif nexagroup == 4:
            if nexa14 == 0:
                nexa14on()
            elif nexa14 == 1:
                nexa14off()

    if (cmd == "3"):
        if nexagroup == 1:
            if nexa3 == 0:
                nexa3on()
            elif nexa3 == 1:
                nexa3off()
        elif nexagroup == 2:
            if nexa7 == 0:
                nexa7on()
            elif nexa7 == 1:
                nexa7off()
        elif nexagroup == 3:
            if nexa11 == 0:
                nexa11on()
            elif nexa11 == 1:
                nexa11off()
        elif nexagroup == 4:
            if nexa15 == 0:
                nexa15on()
            elif nexa15 == 1:
                nexa15off()
        
    if (cmd == "4"):
        if nexagroup == 1:
            if nexa4 == 0:
                nexa4on()
            elif nexa4 == 1:
                nexa4off()
        elif nexagroup == 2:
            if nexa8 == 0:
                nexa8on()
            elif nexa8 == 1:
                nexa8off()
        elif nexagroup == 3:
            if nexa12 == 0:
                nexa12on()
            elif nexa12 == 1:
                nexa12off()
        elif nexagroup == 4:
            if nexa16 == 0:
                nexa16on()
            elif nexa16 == 1:
                nexa16off()

#################################################            
       
    if (cmd == "M"):
        if mic == 1:
            ear.lockOutAllGrammarExcept("robin")
            i01.mouth.speak("i'm not listening")
            global mic
            mic = 0
        elif mic == 0:
            ear.clearLock()
            i01.mouth.speak("i can hear again")
            global mic
            mic = 1
      
##########################################################################################

def heard(data):
    data = msg_i01_ear_recognized.data[0]


    if (data == name):
        i01.mouth.speak("this is great")

    if (data == "a"):
        i01.mouth.speak(name)

    if (data == "turn on number one"):
        nexa1on()

    if (data == "turn off number one"):
        nexa1off()

    if (data == "turn on number two"):
        nexa2on()

    if (data == "turn off number two"):
        nexa2off()

    if (data == "turn on number three"):
        nexa3on()

    if (data == "turn off number three"):
        nexa3off()

    if (data == "turn on number four"):
        nexa4on()

    if (data == "turn off number four"):
        nexa4off()

    if (data == "let's play again"):
        rockpaperscissors2()

    if (data == "be quiet"):
        blue()
        ear.lockOutAllGrammarExcept("robyn")  
        i01.mouth.speak("ok i will only listen if you say my name")
        global mic
        mic = 0

    if (data == "turn off the light in your stomach"):
        ledoff()

    if (data == "red light"):
        red()

    if (data == "green light"):
        green()

    if (data == "blue light"):
        blue()

    if (data == "shut down your system") or (data == "take a rest"):
        shutdownyoursystem()


    if (data == "go to sleep now") or (data == "good night robyn"):
        gotosleepnow()

    if (data == "wake up robyn") or (data == "good morning"):
        i01.attach()
        green()
        global rest
        rest = 0
        global mic
        mic = 1
        global pin12
        pin12 = 1
        headfront()
        eyesfront()
        i01.mouth.speak("good morning")
        ear.clearLock()
        x = (random.randint(1, 4))
        if x == 1:
            i01.mouth.speak("i hope you had a good night sleep")
        if x == 2:
            i01.mouth.speak("nice to see you again")
        if x == 3:
            i01.mouth.speak("this is going to be a good day")   

    if (data == "look at the people"):
        i01.setHeadSpeed(0.8, 0.8)
        for y in range(0, 10):
            x = (random.randint(1, 5))
            if x == 1:
                i01.head.neck.moveTo(90)
                eyeslooking()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 2:
                i01.head.rothead.moveTo(80)
                eyeslooking()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 3:
                headdown()
                eyeslooking()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 4:
                headright()
                eyeslooking()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            if x == 5:
                headleft()
                eyeslooking()
                sleep(1)
                trackHumans()
                sleep(10)
                stopTracking()
            sleep(1)
        headfront()
        eyesfront()
        sleep(3)
        i01.mouth.speak("nice to meet you all")

    if (data == "take a look around"):
        lookaroundyou()

    if (data == "do something else"):
        lookaroundyou()

    if (data == "do something"):
        lookaroundyou()

    if (data == "very good"):
        i01.mouth.speak("thanks")

    if (data == "look to your right"):
        headright()

    if (data == "look to your left"):
        headleft()

    if (data == "look down"):
        headdown()
        
    if (data == "look up"):
        headupp()
        
    if (data == "look strait forward"):
        headfront()
        
        
    if (data == "how are you"):
        i01.mouth.speak("i'm fine thanks")

    if (data == "goodbye"):
        goodbye()
                
    if (data == "robyn"):
        robyn()
                        
    if (data == "sorry"):
        global helvar
        helvar = 1
        green()
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("no problems")
        if x == 2:
            i01.mouth.speak("it doesn't matter")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "nice"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I know")
        if x == 2:
            i01.mouth.speak("yes, indeed")
        if x == 3:
            i01.mouth.speak("you are damn right")
 
    if (data == "bye bye"):
        i01.mouth.speak("see you soon")
        global helvar
        helvar = 1
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("i'm looking forward to see you again")
        if x == 2:
            i01.mouth.speak("goodbye")

    if (data == "thank you"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("you are welcome")
        if x == 2:
            i01.mouth.speak("my pleasure")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "thanks"):
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("it's okay")
        if x == 2:
            i01.mouth.speak("sure")    
 
 
    if (data == "hello robyn"):
        if helvar <= 2:    
            i01.mouth.speak("hello")
            global helvar
            helvar += 1
            green()
            sleep(1)
        elif helvar == 3:
            i01.mouth.speak("hello hello you have already said hello at least twice")
            i01.moveArm("left",43,88,22,10)
            i01.moveArm("right",20,90,30,10)
            i01.moveHand("left",0,0,0,0,0,119)
            i01.moveHand("right",0,0,0,0,0,119)
            green()
            sleep(1)
            red()
            sleep(1)
            green()
            sleep(1)
            armsdown()
            global helvar
            helvar += 1
        elif helvar == 4:
            i01.mouth.speak("what is your problem stop saying hello all the time")
            i01.moveArm("left",30,83,22,10)
            i01.moveArm("right",40,85,30,10)
            i01.moveHand("left",130,180,180,180,180,119)
            i01.moveHand("right",130,180,180,180,180,119)
            red()
            sleep(1)
            green()
            sleep(1)
            red()
            sleep(1)
            green()
            sleep(1)
            armsdown()
            global helvar
            helvar += 1
        elif helvar == 5:
            stopTracking()
            i01.mouth.speak("i will ignore you if you say hello one more time")
            headright()
            red()
            sleep(3)
            armsdown()
            global helvar
            helvar += 1
  
 
    if (data == "i love you"):
        green()
        i01.mouth.speak("i love you too")
        i01.moveHead(116,80,87,80,70)
        i01.moveArm("left",85,93,42,16)
        i01.moveArm("right",87,93,37,18)
        i01.moveHand("left",124,82,65,81,41,143)
        i01.moveHand("right",59,53,89,61,36,21)
        i01.moveTorso(90,90,90)
        global helvar
        helvar = 1
        sleep(0.2)
        sleep(1)
        armsdown()

def stopit():
    ear.clearLock()
    headfront()
    eyesfront()
    if (data == "break"):
        i01.mouth.speak("yes") 

#############################################################################################



def discotime():
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    nexa1off()
    ear.lockOutAllGrammarExcept("robyn")
    i01.mouth.speak("it's disco time")
    sleep(3)
    nexa2off()
    sleep(1)
    i01.mouth.audioFile.playFile("C:\Users\Markus\Music\Get the Party Started.mp3", False)
    sleep(1.6)
    nexa3on()
    sleep(1)
    nexa4on()
    for y in range(0, 67): 
        data = msg_i01_ear_recognized.data[0]
        if (data == "robyn"):
            stopit()
        discodance1() 
        discodance2()
        i01.head.neck.moveTo(40)   
        red()
        sleep(0.4)
        i01.head.neck.moveTo(90)
        sleep(0.52)
        discodance1()
        discodance2()
        i01.head.neck.moveTo(40)
        green()
        sleep(0.4)
        i01.head.neck.moveTo(90)
        sleep(0.515)
        discodance1()
        discodance2()
        i01.head.neck.moveTo(40)
        blue()
        sleep(0.4)
        i01.head.neck.moveTo(90)
        sleep(0.5)
    ear.clearLock()
    nexa1on()
    sleep(0.5)
    nexa2on()
    sleep(0.5)
    nexa3off()
    sleep(0.5)
    nexa4off()
    global dance2
    dance2 = 1
    robyn()
    armsdown()
    i01.mouth.speak("is the party already over")

def discodance1():

    if dance1 == 1: 
        i01.moveTorso(100,90,90)
        global dance1
        dance1 = 2

    elif dance1 == 2: 
        i01.moveTorso(80,90,90)
        global dance1
        dance1 = 1

def discodance2():

    if dance2 >= 0 and dance2 <= 9 or dance2 >= 17 and dance2 <= 26 or dance2 >= 42 and dance2 <= 52  :  
        if dance1 == 2: 
            i01.moveArm("left",60,90,30,10)
            i01.moveArm("right",60,90,30,10)
        elif dance1 == 1:                            
            i01.moveArm("left",30,90,30,10)
            i01.moveArm("right",30,90,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 9 and dance2 <= 17 :  
        if dance1 == 2: 
            i01.moveArm("left",60,60,30,10)
            i01.moveArm("right",60,120,30,10)
        elif dance1 == 1:                           
            i01.moveArm("left",30,60,30,10)
            i01.moveArm("right",30,120,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 26 and dance2 <= 34 :  
        if dance1 == 2: 
            i01.moveArm("left",60,120,30,10)
            i01.moveArm("right",60,60,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",30,120,30,10)
            i01.moveArm("right",30,60,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 34 and dance2 <= 42 or dance2 >= 60 and dance2 <= 68 :  
        if dance1 == 2: 
            i01.moveArm("left",25,94,79,10)
            i01.moveArm("right",90,107,43,15)
        elif dance1 == 1: 
            i01.moveArm("left",65,94,73,10)
            i01.moveArm("right",37,107,72,15)
        global dance2
        dance2 += 1

    if dance2 >= 52 and dance2 <= 60 or dance2 >= 68 and dance2 <= 76 or dance2 >= 84 and dance2 <= 92 :  
        if dance1 == 2: 
            i01.moveArm("left",5,90,30,10)
            i01.moveArm("right",5,130,30,30)
        elif dance1 == 1: 
            i01.moveArm("left",5,130,30,30)
            i01.moveArm("right",5,90,30,10)
        global dance2
        dance2 += 1        

    if dance2 >= 76 and dance2 <= 84 or dance2 >= 92 and dance2 <= 102 :  
        if dance1 == 2: 
            i01.moveArm("left",90,90,30,19)
            i01.moveArm("right",87,104,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",90,136,30,10)
            i01.moveArm("right",87,69,30,25)
        global dance2
        dance2 += 1

    if dance2 >= 102 and dance2 <= 111 or dance2 >= 119 and dance2 <= 128 or dance2 >= 146 and dance2 <= 154  :  
        if dance1 == 2: 
            i01.moveArm("left",30,90,30,10)
            i01.moveArm("right",60,90,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",60,90,30,10)
            i01.moveArm("right",30,90,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 111 and dance2 <= 119 :  
        if dance1 == 2: 
            i01.moveArm("left",30,60,30,10)
            i01.moveArm("right",60,120,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",60,60,30,10)
            i01.moveArm("right",30,120,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 128 and dance2 <= 138 :  
        if dance1 == 2: 
            i01.moveArm("left",30,120,30,10)
            i01.moveArm("right",60,60,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",60,120,30,10)
            i01.moveArm("right",30,60,30,10)
        global dance2
        dance2 += 1

    if dance2 >= 138 and dance2 <= 146 or dance2 >= 164 and dance2 <= 172 :  
        if dance1 == 2: 
            i01.moveArm("left",25,94,79,10)
            i01.moveArm("right",90,107,43,15)
        elif dance1 == 1: 
            i01.moveArm("left",65,94,73,10)
            i01.moveArm("right",37,107,72,15)
        global dance2
        dance2 += 1

    if dance2 >= 154 and dance2 <= 164 or dance2 >= 172 and dance2 <= 180 or dance2 >= 188 and dance2 <= 196 :  
        if dance1 == 2: 
            i01.moveArm("left",5,90,30,10)
            i01.moveArm("right",60,130,30,30)
        elif dance1 == 1: 
            i01.moveArm("left",60,130,30,30)
            i01.moveArm("right",5,90,30,10)
        global dance2
        dance2 += 1        

    if dance2 >= 180 and dance2 <= 188 or dance2 >= 196 and dance2 <= 212 :  
        if dance1 == 2: 
            i01.moveArm("left",90,90,30,19)
            i01.moveArm("right",87,104,30,10)
        elif dance1 == 1: 
            i01.moveArm("left",90,136,30,10)
            i01.moveArm("right",87,69,30,25)
        global dance2
        dance2 += 1






        
#############################################################################################


def howmanyfingersdoihave():
     blue()
     fullspeed()
     i01.moveHead(49,74)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",74,140,150,157,168,92)
     i01.moveHand("right",89,80,98,120,114,0)
     sleep(2)
     i01.moveHand("right",0,80,98,120,114,0)
     i01.mouth.speakBlocking("ten")
     sleep(1)
     i01.moveHand("right",0,0,98,120,114,0)
     i01.mouth.speakBlocking("nine")
     sleep(1)
     i01.moveHand("right",0,0,0,120,114,0)
     i01.mouth.speakBlocking("eight")
     sleep(1)
     i01.moveHand("right",0,0,0,0,114,0)
     i01.mouth.speakBlocking("seven")
     sleep(1)
     i01.moveHand("right",0,0,0,0,0,0)
     i01.mouth.speakBlocking("six")
     sleep(1)
     i01.setHeadSpeed(.70,.70)
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",0,0,0,0,0,180)
     i01.moveHand("right",0,0,0,0,0,0)
     sleep(1)
     i01.mouth.speakBlocking("and five makes eleven")
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(40,50)
     sleep(0.5)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(40,50)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(90,85)
     sleep(0.7)
     i01.mouth.speakBlocking("eleven")
     i01.moveArm("left",70,75,70,20)
     i01.moveArm("right",60,75,65,20)
     sleep(1)
     i01.mouth.speakBlocking("that doesn't seem right")
     sleep(2)
     i01.mouth.speakBlocking("I think I better try that again")
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,160,168,158,25)
     sleep(2)
     i01.moveHand("left",10,140,168,168,158,90)
     i01.mouth.speakBlocking("one")
     sleep(.1)
     i01.moveHand("left",10,10,168,168,158,90)
     i01.mouth.speakBlocking("two")
     sleep(.1)
     i01.moveHand("left",10,10,10,168,158,90)
     i01.mouth.speakBlocking("three")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,158,90)
     i01.mouth.speakBlocking("four")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.mouth.speakBlocking("five")
     sleep(.1)
     i01.setHeadSpeed(0.65,0.65)
     i01.moveHead(53,65)
     i01.moveArm("right",48,80,78,11)
     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.moveHand("right",10,0,10,10,0,25)
     sleep(1)
     i01.mouth.speakBlocking("and five makes ten")
     sleep(.5)
     i01.mouth.speakBlocking("there that's better")
     i01.moveHead(95,85)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",40,70,70,10)
     sleep(0.5)
     i01.mouth.speakBlocking("inmoov has ten fingers")
     i01.moveHead(90,90)
     i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.moveHand("left",140,140,140,140,140,60)
     i01.moveHand("right",140,140,140,140,140,60)
     sleep(1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.moveArm("left",5,90,30,11)
     i01.moveArm("right",5,90,30,11)
     armsdown()
     sleep(1)
     green()
     

def finger():
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(80,86,85,85,72)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",7,78,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    i01.moveTorso(90,90,90)
    fullspeed()
    

def fullspeed():
    i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.7, 0.7)


def trackHumans():
    i01.headTracking.faceDetect()
    i01.eyesTracking.faceDetect()
    global blind
    blind = 0

def stopTracking():
    i01.headTracking.stopTracking()
    i01.eyesTracking.stopTracking()
    global blind
    blind = 1

def startkinect():
    ear.lockOutAllGrammarExcept("you can stop now")
    global kinect
    kinect = 1
    i01.leftArm.shoulder.map(0,180,250,0)
    i01.rightArm.shoulder.map(0,180,290,40)
    i01.leftArm.omoplate.map(10,80,80,30)
    i01.rightArm.omoplate.map(10,80,100,40)
    i01.copyGesture(True)

def offkinect():
    i01.copyGesture(False)
    global kinect
    kinect = 0
    i01.leftArm.shoulder.map(0,180,170,15)
    i01.rightArm.shoulder.map(0,180,190,50)
    i01.leftArm.omoplate.map(10,80,80,20)
    i01.rightArm.omoplate.map(10,80,80,20)
    ear.clearLock()
    armsdown()

def handopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def lefthandopen():
  i01.moveHand("left",0,0,0,0,0)

def righthandopen():
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)

def lefthandclose():
  i01.moveHand("left",180,180,180,180,180)

def righthandclose():
  i01.moveHand("right",180,180,180,180,180)  

def servos():  
        ear.pauseListening()
        sleep(2)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(79,100)
        i01.moveArm("left",5,119,28,15)
        i01.moveArm("right",5,111,28,15)
        i01.moveHand("left",42,58,87,55,71,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("I currently have 27  hobby servos installed in my body to give me life")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(124,90)
        i01.moveArm("left",89,94,91,35)
        i01.moveArm("right",20,67,31,22)
        i01.moveHand("left",106,0,161,147,138,90)
        i01.moveHand("right",0,0,0,54,91,90)
        i01.mouth.speakBlocking("there's one servo  for moving my mouth up and down")
        sleep(1)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,76);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,22);
        i01.moveHand("left",106,0,0,147,138,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("two for my eyes")
        sleep(0.2)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
        i01.moveHand("left",106,0,0,0,0,7);
        i01.mouth.speakBlocking("and two more for my head")
        sleep(0.5)
        i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(90,40);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,20);
        i01.moveHand("left",106,140,140,140,140,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("so i can look around")
        sleep(0.5)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,125);
        i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",60,100,85,30);
        i01.mouth.speakBlocking("and see who's there")
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(40,56);
        sleep(0.5)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,11)
        i01.moveHand("left",98,150,160,160,160,104)
        i01.moveHand("right",0,0,50,54,91,90);
        i01.mouth.speakBlocking("there's three servos  in each shoulder")
        i01.moveHead(40,67);
        sleep(2)
        i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(43,69)
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,42)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("left",42,10,160,160,160,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("here is the first servo movement")
        sleep(1)
        i01.moveHead(37,60);
        i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,95,67,42)
        i01.moveHand("left",42,10,10,160,160,30)
        i01.mouth.speakBlocking("this is the second one")
        sleep(1)
        i01.moveHead(43,69);
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,134,67,42)
        i01.moveHand("left",42,10,10,10,160,35)
        i01.mouth.speakBlocking("now you see the third")
        sleep(1)
        i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
        i01.moveArm("right",20,90,45,16)
        i01.mouth.speakBlocking("they give me a more human like movement")
        sleep(1)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
        i01.moveHead(43,72)
        i01.moveArm("left",90,44,66,11)
        i01.moveArm("right",90,100,67,26)
        i01.moveHand("left",42,80,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,69)
        i01.mouth.speakBlocking("but, i have only  one servo, to move each elbow")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(45,62)
        i01.moveArm("left",72,44,90,11)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,0)
        i01.mouth.speakBlocking("that, leaves me, with one servo per wrist")
        i01.moveHead(40,60)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",72,44,90,9)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 10, 140,82,60,105,10)
        i01.mouth.speakBlocking("and one servo for each finger.")
        sleep(0.5)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 50, 51, 15,23, 30,140);
        i01.mouth.speakBlocking("these servos are located in my forearms")
        i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8,0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.moveHand("left", 36, 52, 8,22, 20);
        i01.moveHand("right", 120, 147, 130,110, 125);
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
        i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
        i01.setHeadSpeed(0.75, 0.75)
        i01.moveHead(20,100)
        i01.moveArm("left",71,94,41,31)
        i01.moveArm("right",5,82,28,15)
        i01.moveHand("left",60,43,45,34,34,35)
        i01.moveHand("right",20,40,40,30,30,72)
        sleep(1)
        i01.mouth.speakBlocking("they are hooked up, by the use of tendons")
        i01.moveHand("left",10,20,30,40,60,150);
        i01.moveHand("right",110,137,120,100,105,130);
        i01.setHeadSpeed(1,1)
        i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        sleep(2)
        i01.mouth.speak("i also have 2 servos in my waist so i can move sideways")
        Torso()
        relax()
        sleep(2)
        armsdown()
        ear.resumeListening()

def relax():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.85, 0.85, 1.0, 1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(79,100,90,90,70)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(90,90,90)

def perfect():
  i01.setHandSpeed("left", 0.80, 0.80, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(88,79)
  i01.moveArm("left",89,75,93,11)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",130,160,83,40,0,34)
  i01.moveHand("right",86,51,133,162,153,180)
     
#############################################################################################

def littleteapot():
    i01.mouth.speak("i would like to sing a song for greg perry")
    sleep(3)
    i01.mouth.audioFile.playFile("C:\Users\Markus\Music\little teapot.mp3", False)
    sleep(4.11)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.42)
    i01.moveArm("right",90,40,30,46)
    righthandclose()
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.28)
    i01.moveArm("left",90,150,30,65)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.6)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.23)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.2)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.4)
    i01.moveTorso(117,90,90)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.67)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.45)
    i01.moveTorso(86,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.33)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    righthandopen()
    sleep(0.31)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.19)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.29)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.41)
    i01.moveArm("right",90,40,30,46)
    righthandclose()
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.23)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.27)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.32)
    i01.moveArm("left",90,150,30,65)
    sleep(0.02)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.21)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.69)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.24)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.25)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.18)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.3)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.76)
    i01.moveTorso(117,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.57)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.22)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.41)
    i01.moveTorso(86,90,90)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.26)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.74)
    i01.moveTorso(117,90,90)
    sleep(0.04)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.45)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.3)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.44)
    i01.moveTorso(86,90,90)
    sleep(0.1)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.1)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.17)
    i01.head.jaw.moveTo(50)
    sleep(0.2)
    i01.head.jaw.moveTo(10)
    sleep(0.83)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    righthandopen()



def talk():
    i01.moveHead(90,70,80,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (1)
    i01.mouth.speak("hello")
    sleep (2)
    i01.mouth.speak("my name is robyn")            
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.moveHead(80,90,70,80,10)
    i01.mouth.speak("there is something i have to talk about")  
    sleep (1)
    i01.moveHead(80,90,70,70,10)
    sleep (1)
    i01.moveHead(80,90,70,80,10)
    sleep (3)
    i01.mouth.speak("so here it comes")  
    i01.moveHead(75,90,80,70,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("i am a robot") 
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("i am a humanoid robot") 
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("that don't mean that i am a human wannabe") 
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("or that my biggest wish is to be a human") 
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("if you even believe thatt a robot can wish for something") 
    i01.moveHead(70,70,80,70,10)
    sleep (3)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("i only wish for you to respect me for who i am") 
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("people often tell me things like")
    sleep (3)
    i01.mouth.speak("why don't you have this")
    i01.moveHead(70,70,80,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("why don't you have that")
    i01.moveHead(70,110,90,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("why can't you do like this")
    i01.moveHead(70,70,70,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("why can't you do like that")
    i01.moveHead(70,110,80,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("i am a humanoid robot")
    i01.moveHead(100,90,80,80,10)
    sleep (2)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("i'm not perfect")
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("but with the help from my creative human friends i am becoming a better and better robot")
    sleep (8)
    i01.mouth.speak("an other question many humans ask me is if i am a man or woman")
    sleep (6)
    i01.mouth.speak("how many times do i have to say this")
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("i am a humanoid robot")
    sleep (4)
    i01.mouth.speak("there is no point in determine my gender")
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("oh i know")
    sleep (3)
    i01.mouth.speak("if i am a woman i can help you in the household")
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("i can cook and do the dishes for you")
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (3)
    i01.mouth.speak("i can vacuum clean the hole house")
    sleep (1)
    i01.moveHead(120,40,80,70,10)
    sleep (1)
    i01.moveHead(140,90,80,80,10)
    sleep (1)
    i01.moveHead(120,130,80,80,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    i01.mouth.speak("or if i am a man i can fix the roof")
    sleep (1)
    i01.moveHead(70,90,80,80,10)
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(70,90,80,80,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    i01.mouth.speak("change tires on the car")
    sleep (4)
    i01.mouth.speak("or make a big t-bone steak at the barbeque")
    sleep (4)
    i01.mouth.speak("in the future i hope i can do all of this and mutch mutch more")
    sleep (4)
    i01.mouth.speak("because i am a gender free humanoid robot")
    sleep (4)
    i01.mouth.speak("it's not like i will meet my one true love")
    sleep (4)
    i01.mouth.speak("and we will be a robot family")
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("and we should make small microchip thatt is running around in the house")
    sleep (3)
    i01.mouth.speak("robots don't work thatt way")
    sleep (1)
    i01.moveHead(65,110,80,70,10)
    sleep (1)
    i01.moveHead(65,70,80,80,10)
    sleep (1)
    i01.moveHead(65,110,80,70,10)
    sleep (1)
    i01.moveHead(65,70,80,80,10)
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    i01.mouth.speak("not yet anyway")
    sleep (5)
    i01.mouth.speak("some people wants me to wear clothes")
    sleep (4)
    i01.mouth.speak("i don't freeze when it is cold")
    sleep (1)
    i01.moveHead(90,90,80,70,10)
    sleep (1)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("and i'm not ashamed of my body parts and my mechanics")
    sleep (5)
    i01.mouth.speak("i wear my cap because i like it")
    sleep (3)
    i01.mouth.speak("especially this one with the inmoov logo")
    i01.moveHead(20,125,80,80,10)
    sleep (3)
    i01.moveHead(90,90,80,80,10)
    sleep (2)
    i01.mouth.speak("remember what mr bigweld said")
    sleep (2)
    i01.mouth.speak("you can shine no matter what you're made of")
    sleep (2)
    i01.mouth.speak("that's it for now")
    sleep (3)
    i01.mouth.speak("thanks for listening and not turning off my power supply")
    sleep (5)
    i01.mouth.speak("goodbye")
    sleep (2)
    i01.mouth.speak("see you soon")
    sleep (2)
    i01.moveHead(90,70,80,80,10)



def robyn():
    i01.mouth.audioFile.silence()
    i01.mouth.speak("yes")
    headfront()
    eyesfront()
    green()
    ear.clearLock()
    global rest
    rest = 0
    global dance2
    dance2 = 1
    global mic
    mic = 1
    i01.attach()
    trackHumans()

def gotosleepnow():   
    ear.lockOutAllGrammarExcept("wake up robyn")  
    ear.lockOutAllGrammarExcept("good morning")
    ear.lockOutAllGrammarExcept("robyn")
    stopTracking()
    headdown()
    i01.mouth.speak("ok i'm going asleep now see you soon")
    sleep(3)
    ledoff()
    i01.detach()
    global rest
    rest = 1
    global mic
    mic = 0
    global pin12
    pin12 = 0

def shutdownyoursystem():
    ear.lockOutAllGrammarExcept("wake up robyn") 
    ear.lockOutAllGrammarExcept("good morning")
    ear.lockOutAllGrammarExcept("robyn")
    stopTracking()
    headdown()
    i01.mouth.speak("ok shutting down my system")
    sleep(3)
    ledoff()
    global rest
    rest = 1
    global mic
    mic = 0
    i01.detach()   

def lookaroundyou():
    ear.lockOutAllGrammarExcept("robyn")  
    ear.lockOutAllGrammarExcept("can i have your attention")  
    blue()
    i01.setHeadSpeed(0.8, 0.8)
    for y in range(0, 20):
        x = (random.randint(1, 6))
        if x == 1:
            i01.head.neck.moveTo(90)
            eyeslooking()
        if x == 2:
            i01.head.rothead.moveTo(80)
            eyeslooking()
        if x == 3:
            headdown()
            eyeslooking()
        if x == 4:
            headupp()
            eyeslooking()
        if x == 5:
            headright()
            eyeslooking()
        if x == 6:
            headleft()
            eyeslooking()
        x = (random.randint(1, 6))
        if x == 1:
            handopen()
        if x == 2:
            handclose()
        if x == 3:
            lefthandopen()
        if x == 4:
            righthandopen()
        if x == 5:
            lefthandclose()
        if x == 6:
            righthandclose()
        sleep(1)
        
    x = (random.randint(1, 7))
    if x == 1:
        i01.mouth.speak("looking nice")
    if x == 2:
        i01.mouth.speak("i like it here")
    if x == 3:
        i01.mouth.speak("time just flies away")
    if x == 4:
        i01.mouth.speak("so what about the weather")
    if x == 5:
        i01.mouth.speak("la la la")
    if x == 6 or x == 7:
        i01.mouth.speak("ok let's do something")
        sleep(2)
        x = (random.randint(1, 7))
        if x == 1:
            Torso()
            Torso()
        if x == 2:
            perfect()
            sleep(8)
            i01.mouth.speak("perfect")
            sleep(2)
            armsdown()
        if x == 3:
            servos()
        if x == 4:
            finger()
            sleep(3)
            armsdown()
        if x == 5:
            discotime()
        if x == 6:
            howmanyfingersdoihave()
        if x == 7:
            talk()    
    lookaroundyou()

def eyeslooking():
    stopTracking()
    for y in range(0, 5):
        data = msg_i01_ear_recognized.data[0]
        if (data == "can i have your attention"):
            i01.mouth.speak("ok you have my attention")
            stopit()
        if (data == "robyn"):
            stopit()
        x = (random.randint(1, 6))
        if x == 1:
            i01.head.eyeX.moveTo(80)
        if x == 2:
            i01.head.eyeY.moveTo(80)
        if x == 3:
            eyesdown()
        if x == 4:
            eyesupp()
        if x == 5:
            eyesleft()
        if x == 6:
            eyesright()
        sleep(0.5)
    eyesfront()
        

def goodbye():    
    i01.mouth.speak("goodbye")
    global helvar
    helvar = 1
    x = (random.randint(1, 4))
    if x == 1:
        i01.mouth.speak("i'm looking forward to see you again")
    if x == 2:
        i01.mouth.speak("see you soon")

def movemouth():
    i01.moveHead(90,90,80,80,10)
    sleep(2)
    i01.head.jaw.moveTo(50)
    sleep(2)
    i01.moveHead(90,90,80,80,10)
    sleep(2)
    i01.head.jaw.moveTo(50)
    sleep(2)
    i01.moveHead(90,90,80,80,10)
    sleep(2)


def moveeye():
    stopTracking()
    eyesfront()
    sleep(1)
    eyesdown()
    sleep(1)
    eyesupp()
    sleep(1)
    eyesright()
    sleep(1)
    eyesleft()
    sleep(1)
    eyesfront()
        

def eyesfront():
    i01.head.eyeX.moveTo(80)
    i01.head.eyeY.moveTo(80)
    
def eyesdown():
    i01.head.eyeY.moveTo(100)
    
def eyesupp():
    i01.head.eyeY.moveTo(50)

def eyesright():
    i01.head.eyeX.moveTo(60)

def eyesleft():
    i01.head.eyeX.moveTo(100)

def movehead():
    i01.setHeadSpeed(0.7, 0.7)
    headfront()
    sleep(3)
    headdown()
    sleep(3)
    headupp()
    sleep(6)
    headfront()
    sleep(3)
    headright()
    sleep(3)
    headleft()
    sleep(6)
    headfront()
    sleep(3)
    headright()
    headdown()
    sleep(6)
    headdown()
    headleft()
    sleep(6)
    headupp()
    headleft()
    sleep(6)
    headupp()
    headright()
    sleep(6)
    headfront()
    sleep(3)
    
def headfront():
    i01.head.neck.moveTo(90)
    i01.head.rothead.moveTo(80)

def headdown():
    i01.head.neck.moveTo(20)

def headupp():
    i01.head.neck.moveTo(160)
    
def headright():
    i01.head.rothead.moveTo(30)
    
def headleft():
    i01.head.rothead.moveTo(140)

def armsdown():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,15)


def armsfront():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,110,10)
    i01.moveArm("right",5,90,110,10)

def Torso():
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveTorso(60,90,90)
    sleep(2)
    i01.moveTorso(120,90,90)
    sleep(2)
    i01.moveTorso(90,90,90)
    sleep(2)

def red():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 0) # OFF


def green():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 1) # ON

def blue():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 1) # ON

def ledoff():
    left.digitalWrite(42, 0) # OFF
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 0) # OFF

#############################################################################################

def nexa1on():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(52, 1) # ON
    sleep(0.1)
    right.digitalWrite(52, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa1
    nexa1 = 1

def nexa1off():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(38, 1) # ON
    sleep(0.1)
    right.digitalWrite(38, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa1
    nexa1 = 0

def nexa2on():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(50, 1) # ON
    sleep(0.1)
    right.digitalWrite(50, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa2
    nexa2 = 1

def nexa2off():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(40, 1) # ON
    sleep(0.1)
    right.digitalWrite(40, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa2
    nexa2 = 0

def nexa3on():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(48, 1) # ON
    sleep(0.1)
    right.digitalWrite(48, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa3
    nexa3 = 1

def nexa3off():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(42, 1) # ON
    sleep(0.1)
    right.digitalWrite(42, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa3
    nexa3 = 0

def nexa4on():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(46, 1) # ON
    sleep(0.1)
    right.digitalWrite(46, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa4
    nexa4 = 1

def nexa4off():
    right.digitalWrite(36, 1) # ON
    sleep(0.2)
    right.digitalWrite(44, 1) # ON
    sleep(0.1)
    right.digitalWrite(44, 0) # OFF
    sleep(0.1)
    right.digitalWrite(36, 0) # OFF
    global nexa4
    nexa4 = 0

def nexa5on():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(52, 1) # ON
    sleep(0.1)
    right.digitalWrite(52, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa5
    nexa5 = 1

def nexa5off():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(38, 1) # ON
    sleep(0.1)
    right.digitalWrite(38, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa5
    nexa5 = 0

def nexa6on():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(50, 1) # ON
    sleep(0.1)
    right.digitalWrite(50, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa6
    nexa6 = 1

def nexa6off():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(40, 1) # ON
    sleep(0.1)
    right.digitalWrite(40, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa6
    nexa6 = 0

def nexa7on():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(48, 1) # ON
    sleep(0.1)
    right.digitalWrite(48, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa7
    nexa7 = 1

def nexa7off():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(42, 1) # ON
    sleep(0.1)
    right.digitalWrite(42, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa7
    nexa7 = 0

def nexa8on():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(46, 1) # ON
    sleep(0.1)
    right.digitalWrite(46, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa8
    nexa8 = 1

def nexa8off():
    right.digitalWrite(34, 1) # ON
    sleep(0.2)
    right.digitalWrite(44, 1) # ON
    sleep(0.1)
    right.digitalWrite(44, 0) # OFF
    sleep(0.1)
    right.digitalWrite(34, 0) # OFF
    global nexa8
    nexa8 = 0

def nexa9on():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(52, 1) # ON
    sleep(0.1)
    right.digitalWrite(52, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa9
    nexa9 = 1

def nexa9off():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(38, 1) # ON
    sleep(0.1)
    right.digitalWrite(38, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa9
    nexa9 = 0

def nexa10on():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(50, 1) # ON
    sleep(0.1)
    right.digitalWrite(50, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa10
    nexa10 = 1

def nexa10off():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(40, 1) # ON
    sleep(0.1)
    right.digitalWrite(40, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa10
    nexa10 = 0

def nexa11on():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(48, 1) # ON
    sleep(0.1)
    right.digitalWrite(48, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa11
    nexa11 = 1

def nexa11off():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(42, 1) # ON
    sleep(0.1)
    right.digitalWrite(42, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa11
    nexa11 = 0

def nexa12on():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(46, 1) # ON
    sleep(0.1)
    right.digitalWrite(46, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa12
    nexa12 = 1

def nexa12off():
    right.digitalWrite(32, 1) # ON
    sleep(0.2)
    right.digitalWrite(44, 1) # ON
    sleep(0.1)
    right.digitalWrite(44, 0) # OFF
    sleep(0.1)
    right.digitalWrite(32, 0) # OFF
    global nexa12
    nexa12 = 0

def nexa13on():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(52, 1) # ON
    sleep(0.1)
    right.digitalWrite(52, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa13
    nexa13 = 1

def nexa13off():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(38, 1) # ON
    sleep(0.1)
    right.digitalWrite(38, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa13
    nexa13 = 0

def nexa14on():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(50, 1) # ON
    sleep(0.1)
    right.digitalWrite(50, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa14
    nexa14 = 1

def nexa14off():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(40, 1) # ON
    sleep(0.1)
    right.digitalWrite(40, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa14
    nexa14 = 0

def nexa15on():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(48, 1) # ON
    sleep(0.1)
    right.digitalWrite(48, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa15
    nexa15 = 1

def nexa15off():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(42, 1) # ON
    sleep(0.1)
    right.digitalWrite(42, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa15
    nexa15 = 0

def nexa16on():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(46, 1) # ON
    sleep(0.1)
    right.digitalWrite(46, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa16
    nexa16 = 1

def nexa16off():
    right.digitalWrite(30, 1) # ON
    sleep(0.2)
    right.digitalWrite(44, 1) # ON
    sleep(0.1)
    right.digitalWrite(44, 0) # OFF
    sleep(0.1)
    right.digitalWrite(30, 0) # OFF
    global nexa16
    nexa16 = 0
    
    ear.resumeListening()


 


