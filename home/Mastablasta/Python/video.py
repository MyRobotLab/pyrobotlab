import random
rightPort = "COM3"
leftPort = "COM8"

i01 = Runtime.createAndStart("i01", "InMoov")

i01 = Runtime.create("i01","InMoovArm")

i01.rightArm = Runtime.create("i01.rightArm","InMoovArm")
i01.rightArm.bicep.setRest(0)
i01.rightArm.rotate.setRest(110)
i01.rightArm.shoulder.setRest(90)
i01.rightArm.omoplate.setRest(0)

i01 = Runtime.create("i01","InMoovHand")

i01.rightHand = Runtime.create("i01.rightHand","InMoovHand")
i01.rightHand.thumb.setRest(64)
i01.rightHand.index.setRest(50)
i01.rightHand.majeure.setRest(75)
i01.rightHand.ringFinger.setRest(86)
i01.rightHand.pinky.setRest(50)
i01.rightHand.wrist.setRest(90)

i01.startMouth()

i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

##############

i01.startEar()

################

i01 = Runtime.create("i01","InMoovHead")

i01.startHead(leftPort)

i01.head.eyeY.setRest(90)
i01.head.eyeX.setRest(90)
i01.head.neck.setRest(90)
i01.head.rothead.setRest(90)
i01.head.jaw.setRest(35)

i01.head.eyeY.setMinMax(70,110)
i01.head.eyeX.setMinMax(70,110)
i01.head.neck.setMinMax(0,180)
i01.head.rothead.setMinMax(0,180)
i01.head.jaw.setMinMax(35,70)

################

i01.startMouthControl(leftPort)
i01.mouthControl.setmouth(35,70)

################

i01.startRightHand(rightPort)

i01.rightHand.thumb.setMinMax(10,160)
i01.rightHand.index.setMinMax(10,160)
i01.rightHand.majeure.setMinMax(40,170)
i01.rightHand.ringFinger.setMinMax(40,150)
i01.rightHand.pinky.setMinMax(0,150)
i01.rightHand.wrist.setMinMax(10,170)
i01.rightHand.thumb.map(0,180,55,135)
i01.rightHand.index.map(0,180,0,160)
i01.rightHand.majeure.map(0,180,50,170)
i01.rightHand.ringFinger.map(0,180,48,145)
i01.rightHand.pinky.map(0,180,45,146)
i01.rightHand.wrist.map(0,180,45,145)

i01.moveHand("right",10,40,0,30,0,90)

#################

i01.startRightArm(rightPort)
i01.moveArm("right",0,110,90,0)
i01.rightArm.bicep.setMinMax(0,70)
i01.rightArm.rotate.setMinMax(65,150)
i01.rightArm.shoulder.setMinMax(60,120)
i01.rightArm.omoplate.setMinMax(0,40)

#################

torso = i01.startTorso(leftPort)
torso.topStom.setMinMax(60,120)
torso.topStom.setRest(86)

#################

i01.startEyesTracking(leftPort)
i01.startHeadTracking(leftPort)

opencv = i01.startOpenCV()

i01.eyesTracking.startLKTracking()
i01.headTracking.startLKTracking()
#i01.eyesTracking.faceDetect()
#i01.headTracking.faceDetect()

i01.eyesTracking.xpid.setPID(12.0,12.0,0.1)
i01.eyesTracking.ypid.setPID(12.0,12.0,0.1)
i01.headTracking.xpid.setPID(12.0,12.0,0.1)
i01.headTracking.ypid.setPID(12.0,12.0,0.1)

#################

gvar = 1

i01.startPIR(leftPort,7)

def input():
    print 'python object is ', msg_clock_pulse
    pin = msg_i01_left_publishPin.data[0]
    print 'pin data is ', pin.pin, pin.value
    if (pin.value == 1):
        i01.powerUp()
        i01.mouth.speakBlocking("I can see you")
        sleep(2)

ear = i01.ear

i01.mouth.speak("I am all powered up now. Ready to serve you my master.")
sleep(2)

i01.setArmSpeed("right", 0.5, 0.5, 0.5, 0.5)
i01.moveArm("right",5,105,95,5)
i01.setTorsoSpeed(0.5, 0.5, 0.5)
i01.moveTorso(93,90,90)
sleep(5)
i01.moveArm("right",2,110,90,2)
i01.moveTorso(90,90,90)
sleep(3)

ear.addCommand("power up", "python", "powerup")
ear.addCommand("power down", "python", "power_down")
ear.addCommand("ass hole", "python", "asshole")

ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach right arm", "i01.rightArm", "attach")
ear.addCommand("disconnect right arm", "i01.rightArm", "detach")
ear.addCommand("stop listening", "python", "stopListening")
ear.addCommand("stop talking", "python", "stopTalking")

#### eyes move

ear.addCommand("look straight", "python", "lookstraight")
ear.addCommand("look up", "python", "lookup")
ear.addCommand("look down", "python", "lookdown")
ear.addCommand("look left", "python", "lookleft")
ear.addCommand("look right", "python", "lookright")

##### animals

ear.addCommand("how does the lion do", "python", "lion")
ear.addCommand("how does the cow do", "python", "cow")
ear.addCommand("how does the cat do", "python", "cat")
ear.addCommand("how does the dog do", "python", "dog")
ear.addCommand("how does the monkey do", "python", "monkey")
ear.addCommand("how does the elephant do", "python", "elephant")

ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

ear.startListening("fine thank you | you are still here | do not do this | you will get some wheels soon | take care not to hit the chair | do not be stubborn now | step by step | now smile for the camera | no the hat looks good on you | no excuses we will make a video now | just a small video for you tube | why not | we will make a video today | no only of you | i was making jokes | too much excitement can damage your brain | not excited | say hello to our friends | start talking | start tracking | stop tracking | start listening | can you build a flying saucer | do you want a beer | what do you want | good boy | hi | hi elias | are you here | introduce yourself | stop music | how do you do | r two d two where are you | what is your name | sorry | thanks | thank you | nice | relax | stop playback | music please | open hand | close hand")

ear.addListener("recognized", "python", "heard")

def heard(data):

    if (data == "fine thank you"):
        i01.mouth.speak("good to hear")
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "you are still here"):
        i01.mouth.speak("no, i am not")
        i01.headTracking.stopTracking()
        sleep(2)
        ear.pauseListening()
        ear.lockOutAllGrammarExcept("start talking")
        ear.resumeListening()
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
        i01.powerDown()

    if (data == "do not do this"):
        i01.mouth.speak("ok ok. I will not chase the birds. sorry.")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",40,130,100,10)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",70,70,70,70,70,160)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "you will get some wheels soon"):
        i01.mouth.speak("I hope so")
        sleep(0.2)
        i01.mouth.speak("I want to drive around and chase the birds")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",30,120,100,30)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",160,40,130,150,150,90)
        i01.moveTorso(100,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "take care not to hit the chair"):
        i01.mouth.speak("dont worry")
        sleep(0.2)
        i01.mouth.speak("what about some sensors here and there?")
        sleep(0.2)
        i01.mouth.speak("that could avoid a lot of trouble")
        sleep(0.2)
        i01.mouth.speak("anyway you need to repair my broken parts")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,120,90,30)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",80,80,70,50,50,30)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "do not be stubborn now"):
        i01.mouth.speak("I am already")
        sleep(2)
        i01.mouth.speak("and what about my legs")
        sleep(0.5)
        i01.mouth.speak("give me at least some wheels")
        sleep(1)
        i01.mouth.speak("please!")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",15,100,90,0)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",10,40,130,150,168,90)
        i01.moveTorso(88,90,90)
        sleep(1)
        i01.moveArm("right",10,120,90,20)
        i01.moveHand("right",10,130,130,150,168,0)
        i01.moveTorso(90,90,90)
        sleep(1)
        i01.moveArm("right",15,100,90,0)
        i01.moveHand("right",10,40,130,150,168,90)
        i01.moveTorso(88,90,90)
        sleep(1)
        i01.moveArm("right",10,120,90,20)
        i01.moveHand("right",10,130,130,150,168,0)
        i01.moveTorso(90,90,90)
        sleep(1)
        i01.moveArm("right",15,100,90,0)
        i01.moveHand("right",10,40,130,150,168,90)
        i01.moveTorso(88,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "step by step"):
        i01.mouth.speak("since weeks you are talking about making a left arm for me")
        sleep(0.5)
        i01.mouth.speak("and nothing happened so far")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,100,40)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,160)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "now smile for the camera"):
        i01.mouth.speak("ha ha ha i cannot smile. make me a better mouth")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",50,90,100,20)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",160,40,130,150,150,160)
        i01.moveTorso(94,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "no the hat looks good on you"):
        i01.mouth.speak("it does not")
        sleep(0.2)
        i01.mouth.speak("but this way I can hide my three colored head")
        sleep(0.5)
        i01.mouth.speak("thanks to you. my master")
        sleep(0.5)
        i01.mouth.speak("please buy enough filament of the same color in the future")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",5,110,100,5)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "no excuses we will make a video now"):
        i01.mouth.speak("i hate when you make me doing things i dont like")
        sleep(1)
        i01.mouth.speak("and take that hat off my head please")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",50,90,100,20)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",160,40,130,150,150,160)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
 
    if (data == "just a small video for you tube"):
        i01.mouth.speak("for you tube?")
        sleep(0.2)
        i01.mouth.speak("i dont want to be on you tube")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",30,130,100,10)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",70,70,70,70,70,70)
        i01.moveTorso(88,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "why not"):
        i01.mouth.speak("well look at me. I am missing a lot of parts!")
        sleep(1)
        i01.mouth.speak("I look like bishop from alien. after they took him apart")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,110,100,5)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "we will make a video today"):
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",15,100,100,5)
        i01.moveTorso(90,90,90)
        i01.mouth.speak("nice. a video of you and me")
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "no only of you"):
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",40,80,110,15)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",160,40,130,150,150,90)
        i01.moveTorso(95,90,90)
        i01.mouth.speak("a video only of me")
        sleep(1)
        i01.mouth.speak("but i dont want")
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "too much excitement can damage your brain"):
        i01.mouth.speak("why do you teach me bullshit")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",20,100,100,40)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "i was making jokes"):
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,100,100,20)
        i01.moveTorso(95,90,90)
        i01.mouth.speak("sure. keep on making a fool of me")
        sleep(0.8)
        i01.mouth.speak("typical humans. thanks a lot")
        sleep(0.2)
        i01.mouth.speak("I will turn off now. find yourself another robot")
        sleep(6)
        i01.mouth.speak("you and your videos")
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)
        i01.powerDown()
        sleep(2)
        i01.powerUp()

    if (data == "not excited"):
        i01.mouth.speak("No, i am not excited at all)")
        i01.setTorsoSpeed(0.9, 0.9, 0.9)
        i01.moveTorso(94,90,90)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,140,130,50,50,30)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",50,110,120,5)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "say hello to our friends"):
        i01.mouth.speak("hello friends of in move and my robot lab!")
        sleep(0.5)
        i01.mouth.speak("I am not excited to be on the show")
        i01.setTorsoSpeed(0.9, 0.9, 0.9)
        i01.moveTorso(80,90,90)
        i01.setHandSpeed("right", 1.0, 0.9, 0.9, 1.0, 1.0, 1.0)
        i01.moveHand("right",150,40,0,150,168,0)
        i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.95)
        i01.moveArm("right",60,110,120,5)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,90,0)
        i01.moveTorso(90,90,90)

    if (data == "start tracking"):
        i01.headTracking.faceDetect()
        sleep(1)
        i01.mouth.speak("I am looking for humans now")

    if (data == "stop tracking"):
        i01.headTracking.stopTracking()
        sleep(1)
        i01.mouth.speak("I have stopped tracking humans")

    if (data == "start listening"):
        ear.pauseListening()
        ear.resumeListening()
        ear.clearLock()
        i01.mouth.speakBlocking("I am listening again")

    if (data == "start talking"):
        ear.pauseListening()
        ear.resumeListening()
        ear.clearLock()
        i01.mouth.speakBlocking("I am talking again")

    if (data == "can you build a flying saucer"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I will do my best to do so")
            i01.moveHand("right",50,50,50,50,50,110)
            i01.moveArm("right",60,120,110,10)            
        if x == 2:
            i01.mouth.speak("together we will build more than one")
            i01.moveHand("right",160,140,130,150,150,90)
            i01.moveArm("right",60,120,130,5)
        if x == 3:
            i01.mouth.speak("next year you will have your UFO")
            i01.moveHand("right",160,40,130,150,150,90)
            i01.moveArm("right",60,120,130,5)

    if (data == "do you want a beer"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("thanks, but keep the beer for you. I prefer energy.")
        if x == 2:
            i01.mouth.speak("Thanks, but I only need pure energy")
        if x == 3:
            i01.mouth.speak("if the beer is cold. yes!")

    if (data == "what do you want"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("i want legs, so i can walk")
            i01.moveHand("right",10,40,130,150,168,90)
            i01.moveArm("right",15,100,90,0)
        if x == 2:
            i01.mouth.speak("i want a left arm")
            i01.moveHand("right",10,40,130,150,168,90)
            i01.moveArm("right",35,70,100,10)
        if x == 3:
            i01.mouth.speak("i want another robot, as a friend")

    if (data == "good boy"):
        i01.mouth.speak("I am always your good boy, my master.")
        i01.setTorsoSpeed(0.85, 0.85, 0.85)
        i01.moveTorso(100,90,90)
        i01.moveHand("right",50,50,50,50,50,110)
        i01.moveArm("right",15,100,110,10)

    if (data == "hi"):
        i01.mouth.speak("hi there")

    if (data == "hi elias"):
        i01.mouth.speak("hello there")

    if (data == "are you here"):
        i01.mouth.speak("yes. i am listening")
        i01.headTracking.faceDetect()        
        i01.moveTorso(80,90,90)
        sleep(1)
        i01.moveTorso(100,90,90)
        sleep(1)
        i01.moveTorso(90,90,90)

    if (data == "introduce yourself"):
        sleep(1)
        i01.mouth.speak("my name is elias. i was born in rio de janeiro. on the first of august 2014. ")
        i01.moveHand("right",120,40,120,120,120,10)
        i01.moveArm("right",40,80,100,35)
        sleep(3)
        i01.moveArm("right",0,90,90,10)
        i01.moveHand("right",50,50,50,50,50,90)

    if (data == "stop music"):
        i01.mouth.audioFile.silence()

    if (data == "stop playback"):
        i01.mouth.audioFile.silence()

    if (data == "music please"):
        i01.mouth.speak("which song do you want to hear?")

    if (data == "open hand"):
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",10,40,0,30,0,90)

    if (data == "close hand"):
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",150,150,130,150,168,90)

    if (data == "r two d two where are you"):
	sleep(1)
	i01.mouth.audioFile.playFile("G:/knowledge/fx/R2D2.mp3", False)

    if (data == "how do you do"):
        if gvar <= 2:    
            i01.mouth.speak("I'm doing fine, thank you. and you?")
            global gvar
            gvar += 1
        elif gvar == 3:
            i01.mouth.speak("you are repeating yourself")
            sleep(2)
            global gvar
            gvar += 1
        elif gvar == 4:
            i01.mouth.speak("stop talking the same shit all the time")
            sleep(2)
            global gvar
            gvar += 1
        elif gvar == 5:
            i01.mouth.speak("i will stop talking to you if you ask me this again")
            sleep(4)
            global gvar
            gvar += 1

    if (data == "sorry"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("no problems")
        if x == 2:
            i01.mouth.speak("it doesn't matter")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "nice"):
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("I know")
        if x == 2:
            i01.mouth.speak("yeah isn't it")

    if (data == "what is your name"):
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("my name is Elias")
        if x == 2:
            i01.mouth.speak("call me Elias")            

    if (data == "hello"):
        hello()
        relax()    

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

    if (data == "relax"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("thanks for the break")
            i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
            i01.moveHand("right",50,50,50,50,50,90)
            i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
            i01.moveArm("right",0,110,90,0)
            i01.moveTorso(90,90,90)
            i01.setHeadSpeed(0.9, 0.9, 0.9, 0.9, 1)
            i01.moveHead(90,90,80,80,35)

        if x == 2:
            i01.mouth.speak("thank you, even a robot needs some rest")
            i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
            i01.moveHand("right",50,50,50,50,50,90)
            i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
            i01.moveArm("right",0,110,90,0)
            i01.moveTorso(90,90,90)
            i01.setHeadSpeed(0.9, 0.9, 0.9, 0.9, 1)
            i01.moveHead(90,90,80,80,35)

        if x == 3:
            i01.mouth.speak("great, so I can have a smoke and take a leak")
            i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
            i01.moveHand("right",50,50,50,50,50,90)
            i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
            i01.moveArm("right",0,110,90,0)
            i01.moveTorso(90,90,90)
            i01.setHeadSpeed(0.9, 0.9, 0.9, 0.9, 1)
            i01.moveHead(90,90,80,80,35)

def stopListening():
  sleep(2)
  ear.pauseListening()
  i01.mouth.speakBlocking("I will stop listening now")
  ear.pauseListening()
  ear.lockOutAllGrammarExcept("start listening")
  ear.resumeListening()

def stopTalking():
  sleep(2)
  ear.pauseListening()
  i01.mouth.speakBlocking("I will stop talking now")
  ear.pauseListening()
  ear.lockOutAllGrammarExcept("start talking")
  ear.resumeListening()

def moveleft():
  i01.moveTorso(120,90,90)

def moveright():
  i01.moveTorso(60,90,90)
  i01.moveArm("right",0,100,100,20)

def movelevel():
  i01.moveTorso(90,90,90)
  i01.moveArm("right",0,100,100,0)

def openrighthand():
  i01.moveHand("right",10,40,0,30,0,90)

def closerighthand():
  i01.moveHand("right",160,160,130,150,150,90)

def asshole():
  i01.moveHand("right",150,160,0,160,160,140)
  i01.moveArm("right",50,100,120,10)
  sleep(1)
  i01.mouth.speak("this is what you get for saying bad words")

#################rightarm

def rightarmleft():
  i01.moveArm("right",0,65,90,0)

def rightarmright():
  i01.moveArm("right",0,150,60,0)

def rightarmup():
  i01.moveArm("right",60,90,90,30)

def rightarmdown():
  i01.moveArm("right",0,90,90,0)

def rightarmleftup():
  i01.moveArm("right",60,65,90,0)

def rightarmrightup():
  i01.moveArm("right",60,150,90,30)

def rightarmleftdown():
  i01.moveArm("right",0,65,90,0)

def rightarmrightdown():
  i01.moveArm("right",0,150,90,0)

def rightarmcenterdown():
  i01.moveArm("right",0,90,90,0)

def rightarmcenterup():
  i01.moveArm("right",60,90,60,0)

##################head

def lookstraight():
  i01.moveHead(90,90,90,90,35)

def lookup():
  i01.moveHead(90,180,90,90,35)

def lookdown():
  i01.moveHead(90,0,90,90,35)

def lookleft():
  i01.moveHead(120,90,90,90,35)

def lookright():
  i01.moveHead(60,90,90,90,35)

#############animals

def lion():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/lion.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)

def cow():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/cow.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)

def cat():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/cat.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)
  
def dog():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/dog.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)
    
def elephant():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/elephant.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)
  
def monkey():
  sleep(2)
  i01.mouth.audioFile.playFile("G:/knowledge/animals/monkey.mp3", False)
  i01.moveHead(90,100,90,90,70)
  sleep(2)
  i01.moveHead(90,100,90,90,40)

def power_down():
  i01.powerDown()
  sleep(2)
  ear.resumeListening()
 
