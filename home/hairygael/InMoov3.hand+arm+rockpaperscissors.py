#file : InMoov3.hand+arm+rockpaperscissors.py

# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a right hand or finger box
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

# play rock paper scissors
inmoov = 0
human = 0

# Change to the port that you use
rightPort = "COM7"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("Ryan")
##############
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand
#i01.rightHand.thumb.setMinMax(55,135)
#i01.rightHand.index.setMinMax(0,160)
#i01.rightHand.majeure.setMinMax(0,140)
#i01.rightHand.ringFinger.setMinMax(48,145)
#i01.rightHand.pinky.setMinMax(45,146)
#i01.rightHand.thumb.map(0,180,55,135)
#i01.rightHand.index.map(0,180,0,160)
#i01.rightHand.majeure.map(0,180,0,140)
#i01.rightHand.ringFinger.map(0,180,48,145)
#i01.rightHand.pinky.map(0,180,45,146)
#################
i01.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

# verbal commands
ear = i01.ear

ear.addCommand("attach your right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect your right hand", "i01.rightHand", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("rock paper scissors", "python", "rockpaperscissors")
ear.addCommand("ready", "python", "ready")
ear.addCommand("rock", "python", "rock")
ear.addCommand("paper", "python", "paper")
ear.addCommand("scissors", "python", "scissors")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening(ear.startListening("yes | no | i have rock | i have paper | i have scissors")


def handopen():
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak("ok I open my hand")

def handclose():
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak("a nice and wide open hand that is")

def rockpaperscissors():
    fullspeed()
    i01.mouth.speak("lets play first to 3 points win")
    sleep(4)
    rockpaperscissors2()

def rockpaperscissors2():
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
                i01.mouth.speak("zero zero")
            if x == 2:
                i01.mouth.speak("no no")
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
            global inmoov
            inmoov += 1
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
            global inmoov
            inmoov += 1
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
            global inmoov
            inmoov += 1
            sleep(1)
        if (data == "i have scissors"):
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("no no")
            if x == 2:
                i01.mouth.speak("zero zero")
            if x == 3:
                i01.mouth.speak("no points")
            sleep(1)
    if inmoov == 3:
        stoprockpaperscissors()
        sleep(1)
    elif human == 3:                       # changed from if to  elif              
        stoprockpaperscissors()
        sleep(1)
    elif inmoov <= 2:                      # changed from if to  elif 
        rockpaperscissors2()
    elif human <= 2:                       # changed from if to  elif 
        rockpaperscissors2()   
  
def stoprockpaperscissors():
    rest()
    sleep(5)
    if inmoov < human:
        i01.mouth.speak("congratulations you won with" + str(human - inmoov) + "points")
        sleep(3)
        i01.mouth.speak(str(human) + "points to you and" + str(inmoov) + "points to me")
    elif inmoov > human:                                                                                                         # changed from if to  elif
        i01.mouth.speak("yes yes i won with" + str(inmoov - human) + "points")
        sleep(3)
        i01.mouth.speak("i've got " + str(inmoov) + "points and you got" + str(human) + "points")
    elif inmoov == human:                                                                                                          # changed from if to  elif
        i01.mouth.speak("none of us won we both got" + str(inmoov) + "points")
    global inmoov
    inmoov = 0
    global human
    human = 0
    i01.mouth.speak("that was fun")
    sleep(2)
    i01.mouth.speak("do you want to play again")
    sleep(10)
    data = msg_i01_ear_recognized.data[0]
    if (data == "yes let's play again"):
        rockpaperscissors2()
    elif (data == "yes"):                                                                              # changed from if to  elif
        rockpaperscissors2()
    elif (data == "no thanks"):                                                                  # changed from if to  elif
        i01.mouth.speak("maybe some other time")
        sleep(4)
        power_down()
    elif (data == "no thank you"):                                                           # changed from if to  elif
        i01.mouth.speak("maybe some other time")
        sleep(4)
        power_down()
    ##i01.mouth.speak("ok i'll find something else to do then")
    ##lookaroundyou()
    

def ready():
    i01.mouth.speak("ready")
    i01.mouth.speak("go")
    i01.moveHead(90,90)
    i01.moveArm("left",65,90,75,10)
    i01.moveArm("right",20,80,25,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    

def rock():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",45,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,80)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have rock what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")

def paper():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",0,0,0,0,0,165)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have paper what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")

def scissors():
    fullspeed()
    i01.moveHead(90,90)
    i01.moveArm("left",70,90,80,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",80,90,85,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    
    sleep(.5)
    i01.moveArm("left",90,90,90,10)
    i01.moveArm("right",20,85,10,20)
    i01.moveHand("left",130,180,180,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.5)
    i01.moveHead(90,90)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",20,80,20,20)
    i01.moveHand("left",50,0,0,180,180,90)
    i01.moveHand("right",50,90,90,90,100,90)
    sleep(.3)
    x = (random.randint(1, 2))
    if x == 1:
        i01.mouth.speakBlocking("i have scissors what do you have")
    if x == 2:
        i01.mouth.speakBlocking("what do you have")      
