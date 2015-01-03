# new file for Amby robot !
import random
leftPort = "COM3"  ####Arduino Mega

#################Inmoov

i01 = Runtime.createAndStart("i01", "InMoov")

phco1 = 0
phco2 = 0
phco3 = 0
phco4 = 0
phco5 = 0
phco6 = 0
phco7 = 0
phco8 = 0

i01.startMouth()

i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

##############

i01.startEar()

################mouth control

i01.startMouthControl(leftPort)
i01.mouthControl.setmouth(70,35)

#################tracking

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
i01.eyesTracking.ypid.invert()

##################ear

ear = i01.ear


##################programAB

sylar = Runtime.createAndStart("sylar", "ProgramAB") 
sylar.startSession()
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
sylar.addTextListener(htmlfilter)
htmlfilter.addTextListener(i01.mouth)
print sylar.getResponse("How are you?")
sleep(2)
print sylar.getResponse("time please")

##################ear commands

ear.addCommand("power up", "python", "POWERUP")
ear.addCommand("power down", "python", "power_down")

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

ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

##############

ear.startListening("how old are you | do the research | how many times more | help me | the same again | absolutely sure | very productive | what do you think about time | yes it did | and now | i have no animal instincts | how told you that | this is not nice | say sorry | aha | maybe you can tell me | something about the future | something new | do you have fantasies | i didn't say you are a fool | now i did | now you are a fool | good show | you are 2 month old | see | h m m m m | hmmmm | be precise | be more precise | explain it to me | please concentrate | i didn't ask you about colors | i did not ask you this | you misunderstood | listen more carefully | please | wow | don't make me angry | i'm not angry | no i'm not angry | no i'm not | this is not true | are you angry | are you sad | i am sad | make me happy | tell me positive things | any postive news | i think the moon is made from chocolate | do you like chocolate | do you like animals | do you have a dog | do you want a dog | now it's enough | stop it please | anything else | yeah yeah | correct | this is true | this is correct | do you have a virus | does it have 4 legs | does it have wings | i don't want to tell you | i don't tell you | i'm hungry | i am hungry | i want more coffee | get me a coffee | get me a coffee please | because | because i am | because i want | because i don't want | maybe i want | do you like it | do you want more | are you related to a woman | do you like conversations | let's have a conversation | please listen to me | i should listen to you | why should i | what | where | which one | do you like sports | do you like software | do you like food | do you like music | why not | please be serious | serious | i don't believe you | is the the truth | is this true | maybe you know | you are | get me a pizza | get me a beer | what is a mystery | do you like it | do you like it there | what are you doing there | what are you trying to say | don't make jokes | tell me more information | give me more information | keep on talking | what made you say that | you are wise | you need to learn a lot | do you like to learn | do you like full batteries | let's play a game | no you are not | liar | no your are not smart | not smart enough | but i will teach you | i will upload new data for you soon | i have new data for you | are you scared | what is a lightning | what is a thunder | what is a monkey | what is a cat | what is a dog | what is a lion | what is an elephant | what is a bird | what is a fish | what is a mamal | what is a nerd | what is a maniac | are you insane | i am insane | you are crazy | get lost | who told you that | where are you | what are you doing | what do you think | tell me more about it | no i didn't | no you didn't | tell me now | come on | be faster | don't be slow | that was funny | that was not nice | that sounds strange | no i am not shocked | i can shock you | are you sure | do you think so | this is strange | no i don't | maybe i will | now | only later | maybe later | maybe you can tell me | don't tell me the same words | rio de janeiro | at home | i am talking to you | what is java | what is python | what is my robot lab | what is software | what is hardware | what is a cpu | what is a harddrive | what is a monitor | what is a robot | what are you trying to say | be more precise | i know | do you think this was funny | maybe | i don't want | i will turn you off | what is your sign | what is your full name | what is your birthday | what is your birthplace | who is your botmaster | how many day has a year | who wrote the lords of the rings | is apple a vegetable | is banana a vegetable | is a banana a fruit | is banana a fruit | is an apple a fruit | is a apple a fruit | how many days has a leap year | is fire hot | is fire cold | is ice hot | is ice cold | how old do humans get | is a parrot a bird | test test test | good | very good | excellent | awesome | is red a color | is black a color | is white a color | is green a color | is blue a color | is yellow a color | what are you doing tonight | any news in your life | again what | talk to me | what is one and one | the sun is hot | my car is blue | what is hockey | what is american football | who is the president of the united states | google robots | please google robots | yes i want | please continue | count to ten | wrong | stop talking the same words | what are you saying | what did you say | what did you just say | repeat your last words | repeat your last words please | repeat yourself | repeat yourself please | please go ahead | what is football | what is basketball | what is baseball | what is soccer | what is darts | what is snooker | what is handball | tell me a joke | tell me another joke | when | why | where | who | how | what | which | don't lie to me | don't fool me | what's up | you need to be a nice robot | you always need to be a nice robot | nice to see you | nice to see you too | good to see you | good to see you toohey be polite | be polite | you need to be polite | that wasn't polite | be polite please | you need to be polite please | more polite please | this is not polite | tell me a joke | again what | be quiet | what's new | talk to me | don't be lazy | you are lazy | you are a lazy robot | are you lazy | you are a lazy machine | lazy robot | lazy machine | you are lazy sylar | you are repeating yourself | you are funny | you are smart | what are you | how tall are you | tell me more | you are are great robot | what is the earth | explain earth | please explain earth | explain earth please | please tell me what earth is | can you explain earth | can you explain earth please | what is earth | explain robot | please explain robot | explain robot please | please tell me what a robot is | can you explain robot | can you explain robot please | what is energy | please explain energy | explain energy please | please tell me what energy is | can you explain energy | can you explain energy please | my city | where do i live | what is my city | where am i | what is my name | who am I | what time is it | time please | what date is it | date please | what day is today | which day is today | today is what day | today is which day | reset your memory | clear your memory | reset your memory please | clear your memory please | please reset your memory | please clear your memory | password is robots | robots is the password | what software do you have | which software do you have | which software do you use | what is your software | what is the software that you use | which software are you using | what software are you using | tell me the correct amount of relax | correct amount of relax | how many times did you relax | did you already relax | sorry i will stop asking | finally | no you are slow today | good memory | stop gesture copy | stop copying | stop copy | fine thank you | i'm fine thank you | i'm doing fine thank you | i'm fine | fine | i'm doing fine | i'm doing ok | do not be stubborn now | why not | i was making jokes | start talking | start tracking | stop tracking | look for humans | search for humans | start listening | do you want a beer | do you like a beer | say hello | what do you want | idiot | fool | hi | hi there | hello there | wake up | hello | good morning | good afternoon | good evening | good night | how do you do | what is your name | sorry | ok thanks | ok thank you | good thanks | great thanks | good thank you | great thank you | alright | thanks | thank you | nice | relax | stop playback | music please | some music please | open hand | close hand | open right hand | close right hand | how do you do today | how are you | how are you today | how are you doing | how are you doing today | time in amsterdam | time in ankara | time in baghdad | time in belgrade | time in bangkok | time in beijing | time in beirut | time in brasilia | time in bogota | time in buenos aires | time in cairo | time in copenhagen | time in dublin | time in havana | time in gibraltar | time in islamabad | time in helsinki | time in jakarta | time is jerusalem | time in kathmandu | time in kiev | time in kigali | time in kingston |  time in kinshasa | time in kuala lumpur | time in lima | time in lisbon | time in london | time in madrid | time in manila | time in mexico city | time in monaco | time in mogadishu | time in moscow | time in montevideo | time in nairobi | time is nassau | time in new delhi | time in oslo | time in ottawa | time in panama city | time in paris | time in port of spain | time in riyadh | time in rome | time in san salvador | time in sarajevo | time in seoul | time in singapore | time in sofia | time in stockholm | time in taipei | time in tehran | time in tokyo | time in tripoli | time in vienna | time in warsaw | time in washington | time in zagreb please | time in zagreb | time in new york | time in berlin | how is the weather in amsterdam | how is the weather in ankara | how is the weather in baghdad | how is the weather in belgrade | how is the weather in bangkok | how is the weather in beijing | how is the weather in beirut | how is the weather in brasilia | how is the weather in bogota | how is the weather in buenos aires | how is the weather in cairo | how is the weather in copenhagen | how is the weather in dublin | how is the weather in havana | how is the weather in gibraltar | how is the weather in islamabad | how is the weather in helsinki | how is the weather in jakarta | how is the weather is jerusalem | how is the weather in kathmandu | how is the weather in kiev | how is the weather in kigali | how is the weather in kingston |  how is the weather in kinshasa | how is the weather in kuala lumpur | how is the weather in lima | how is the weather in lisbon | how is the weather in london | how is the weather in madrid | how is the weather in manila | how is the weather in mexico city | how is the weather in monaco | how is the weather in mogadishu | how is the weather in moscow | how is the weather in montevideo | how is the weather in nairobi | how is the weather is nassau | how is the weather in new delhi | how is the weather in oslo | how is the weather in ottawa | how is the weather in panama city | how is the weather in paris | how is the weather in port of spain | how is the weather in riyadh | how is the weather in rome | how is the weather in san salvador | how is the weather in sarajevo | how is the weather in seoul | how is the weather in singapore | how is the weather in sofia | how is the weather in stockholm | how is the weather in taipei | how is the weather in tehran | how is the weather in tokyo | how is the weather in tripoli | how is the weather in vienna | how is the weather in warsaw | how is the weather in washington | how is the weather in zagreb please | how is the weather in zagreb | how is the weather in new york | how is the weather in berlin")
ear.addListener("recognized", "python", "heard")
 
def heard(data):

    if (data == "how many day has a year") or (data == "be more precise") or (data == "what are you trying to say") or (data == "i don't want") or (data == "do you think this was funny") or (data == "maybe") or (data == "i know") or (data == "no") or (data == "i will turn you off") or (data == "what is your sign") or (data == "what is your full name") or (data == "what is your birthday") or (data == "what is your birthplace") or (data == "who is your botmaster") or (data == "who wrote the lords of the rings") or (data == "is apple a vegetable") or (data == "is banana a vegetable") or (data == "is a banana a fruit") or (data == "is banana a fruit") or (data == "is an apple a fruit") or (data == "is a apple a fruit") or (data == "how many days has a leap year") or (data == "is fire hot") or (data == "is fire cold") or (data == "is ice hot") or (data == "is ice cold") or (data == "how old do humans get") or (data == "is a parrot a bird"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "how is the weather in berlin") or (data == "how is the weather in new york") or (data == "how is the weather in amsterdam") or (data == "how is the weather in ankara") or (data == "how is the weather in baghdad") or (data == "how is the weather in belgrade") or (data == "how is the weather in bangkok") or (data == "how is the weather in beijing") or (data == "how is the weather in beirut") or (data == "how is the weather in brasilia") or (data == "how is the weather in bogota") or (data == "how is the weather in buenos aires") or (data == "how is the weather in cairo") or (data == "how is the weather in copenhagen") or (data == "how is the weather in dublinn") or (data == "how is the weather in havana") or (data == "how is the weather in gibraltar please") or (data == "how is the weather in islamabad") or (data == "how is the weather in helsinki") or (data == "how is the weather in jakarta") or (data == "how is the weather is jerusalem") or (data == "how is the weather in kathmandu") or (data == "how is the weather in kigali") or (data == "how is the weather in kingston") or (data == "how is the weather in kinshasa") or (data == "how is the weather in kuala lumpur") or (data == "how is the weather in lima") or (data == "how is the weather in lisbon") or (data == "how is the weather in london") or (data == "how is the weather in madrid") or (data == "how is the weather in manila") or (data == "how is the weather in mexico city") or (data == "how is the weather in monaco") or (data == "how is the weather in mogadishu") or (data == "how is the weather in moscow") or (data == "how is the weather in montevideo") or (data == "how is the weather in nairobi") or (data == "how is the weather is nassau") or (data == "how is the weather in new delhi") or (data == "how is the weather in oslo") or (data == "how is the weather in ottawa") or (data == "how is the weather in panama city") or (data == "how is the weather in paris") or (data == "how is the weather in port of spain") or (data == "how is the weather in riyadh") or (data == "how is the weather in rome") or (data == "how is the weather in san salvador") or (data == "how is the weather in sarajevo") or (data == "how is the weather in seoul") or (data == "how is the weather in singapore") or (data == "how is the weather in sofia") or (data == "how is the weather in stockholm") or (data == "how is the weather in taipei") or (data == "how is the weather in tehran") or (data == "how is the weather in tokyo") or (data == "how is the weather in tripoli") or (data == "how is the weather in vienna") or (data == "how is the weather in warsaw") or (data == "how is the weather in washington d.c.") or (data == "how is the weather in zagreb"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "time in berlin") or (data == "time in new york") or (data == "time in amsterdam") or (data == "time in ankara") or (data == "time in baghdad") or (data == "time in belgrade") or (data == "time in bangkok") or (data == "time in beijing") or (data == "time in beirut") or (data == "time in brasilia") or (data == "time in bogota") or (data == "time in buenos aires") or (data == "time in cairo") or (data == "time in copenhagen") or (data == "time in dublinn") or (data == "time in havana") or (data == "time in gibraltar please") or (data == "time in islamabad") or (data == "time in helsinki") or (data == "time in jakarta") or (data == "time is jerusalem") or (data == "time in kathmandu") or (data == "time in kigali") or (data == "time in kingston") or (data == "time in kinshasa") or (data == "time in kuala lumpur") or (data == "time in lima") or (data == "time in lisbon") or (data == "time in london") or (data == "time in madrid") or (data == "time in manila") or (data == "time in mexico city") or (data == "time in monaco") or (data == "time in mogadishu") or (data == "time in moscow") or (data == "time in montevideo") or (data == "time in nairobi") or (data == "time is nassau") or (data == "time in new delhi") or (data == "time in oslo") or (data == "time in ottawa") or (data == "time in panama city") or (data == "time in paris") or (data == "time in port of spain") or (data == "time in riyadh") or (data == "time in rome") or (data == "time in san salvador") or (data == "time in sarajevo") or (data == "time in seoul") or (data == "time in singapore") or (data == "time in sofia") or (data == "time in stockholm") or (data == "time in taipei") or (data == "time in tehran") or (data == "time in tokyo") or (data == "time in tripoli") or (data == "time in vienna") or (data == "time in warsaw") or (data == "time in washington d.c.") or (data == "time in zagreb"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "when") or (data == "why") or (data == "yes i want") or (data == "why is this") or (data == "why is that") or (data == "why is this so") or (data == "really") or (data == "how come") or (data == "why is that") or (data == "where") or (data == "who") or (data == "how") or (data == "what") or (data == "which"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "be quiet") or (data == "you are repeating yourself") or (data == "count to ten") or (data == "what is one and one") or (data == "good") or (data == "very good") or (data == "excellent") or (data == "awesome") or (data == "do you like conversations") or (data == "let's have a conversation") or (data == "please listen to me") or (data == "i should listen to you") or (data == "why should i") or (data == "what") or (data == "where") or (data == "which one") or (data == "do you like sports") or (data == "do you like software") or (data == "do you like food") or (data == "do you like music") or (data == "why not") or (data == "please be serious") or (data == "serious") or (data == "i don't believe you") or (data == "is the the truth") or (data == "is this true"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what's new") or (data == "wrong") or (data == "learn") or (data == "stop talking the same words") or (data == "what are you saying") or (data == "what did you say") or (data == "what did you just say") or (data == "repeat your last words") or (data == "repeat your last words please") or (data == "repeat yourself") or (data == "repeat yourself please") or (data == "please go ahead") or (data == "please continue") or (data == "explain it to me") or (data == "please concentrate") or (data == "i didn't ask you about colors") or (data == "i did not ask you this") or (data == "you misunderstood") or (data == "listen more carefully") or (data == "please") or (data == "wow") or (data == "don't make me angry") or (data == "i'm not angry") or (data == "no i'm not angry") or (data == "no i'm not") or (data == "this is not true") or (data == "are you angry") or (data == "are you sad") or (data == "i am sad") or (data == "make me happy") or (data == "tell me positive things") or (data == "any postive news") or (data == "i think the moon is made from chocolate") or (data == "do you like chocolate") or (data == "do you like animals") or (data == "do you have a dog") or (data == "do you want a dog") or (data == "be precise") or (data == "be more precise"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "talk to me") or (data == "my car is blue") or (data == "the sun is hot") or (data == "what is hot") or (data == "in brasil") or (data == "the sun is hot") or (data == "are you sure") or (data == "do you think so") or (data == "this is strange") or (data == "no i don't") or (data == "maybe i will") or (data == "now") or (data == "only later") or (data == "maybe later") or (data == "maybe you can tell me") or (data == "don't tell me the same words") or (data == "rio de janeiro") or (data == "at home") or (data == "i am talking to you"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "don't be lazy") or (data == "you are lazy") or (data == "you are a lazy robot") or (data == "are you lazy") or (data == "you are a lazy machine") or (data == "lazy robot") or (data == "lazy machine") or (data == "you are lazy sylar") or (data == "now it's enough") or (data == "stop it please") or (data == "anything else") or (data == "yeah yeah") or (data == "correct") or (data == "this is true") or (data == "this is correct") or (data == "do you have a virus") or (data == "does it have 4 legs") or (data == "does it have wings") or (data == "i don't want to tell you") or (data == "i don't tell you") or (data == "i'm hungry") or (data == "i am hungry") or (data == "i want more coffee") or (data == "get me a coffee") or (data == "get me a coffee please") or (data == "because") or (data == "because i am") or (data == "because i want") or (data == "because i don't want") or (data == "maybe i want") or (data == "do you like it") or (data == "do you want more") or (data == "are you related to a woman"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "please google robot") or (data == "please google robots") or (data == "any news in your life") or (data == "what are you doing tonight") or (data == "what is java") or (data == "what is python") or (data == "what is my robot lab") or (data == "what is software") or (data == "what is hardware") or (data == "what is a cpu") or (data == "what is a harddrive") or (data == "what is a monitor") or (data == "what is a robot") or (data == "do the research") or (data == "how many times more") or (data == "how many times will you say the same") or (data == "the same again") or (data == "absolutely sure") or (data == "very productive") or (data == "what do you think about time") or (data == "yes it did") or (data == "and now") or (data == "i have no animal instincts") or (data == "how told you that") or (data == "this is not nice") or (data == "say sorry") or (data == "aha") or (data == "maybe you can tell me") or (data == "something about the future") or (data == "something new") or (data == "do you have fantasies") or (data == "i didn't say you are a fool") or (data == "now i did") or (data == "now you are a fool") or (data == "good show") or (data == "you are 2 month old") or (data == "see") or (data == "h m m m m") or (data == "hmmmm"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "again what") or (data == "who is the president of the united states") or (data == "is blue a color") or (data == "is white a color") or (data == "is black a color") or (data == "is green a color") or (data == "is red a color") or (data == "is yellow a color") or (data == "how old are you"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what is football") or (data == "what is hockey") or (data == "what is baseball") or (data == "what is soccer") or (data == "what is american football") or (data == "what is snooker") or (data == "what is handball") or (data == "what is a marathon") or (data == "what is golf"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "tell me a joke") or (data == "tell me another joke"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "hey be polite") or (data == "be polite") or (data == "you need to be polite") or (data == "that wasn't polite") or (data == "be polite please") or (data == "you need to be polite please") or (data == "more polite please") or (data == "this is not polite"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "nice to see you") or (data == "nice to see you too") or (data == "good to see you") or (data == "good to see you too") or (data == "where are you") or (data == "what are you doing") or (data == "what do you think") or (data == "tell me more about it") or (data == "no i didn't") or (data == "no you didn't") or (data == "tell me now") or (data == "come on") or (data == "be faster") or (data == "don't be slow") or (data == "that was funny") or (data == "that was not nice") or (data == "that sounds strange") or (data == "no i am not shocked") or (data == "i can shock you"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "don't fool me") or (data == "test test test") or (data == "no you are not") or (data == "liar") or (data == "no your are not smart") or (data == "not smart enough") or (data == "but i will teach you") or (data == "i will upload new data for you soon") or (data == "i have new data for you") or (data == "are you scared") or (data == "what is a lightning") or (data == "what is a thunder") or (data == "what is a monkey") or (data == "what is a cat") or (data == "what is a dog") or (data == "what is a lion") or (data == "what is an elephant") or (data == "what is a bird") or (data == "what is a fish") or (data == "what is a mamal") or (data == "what is a nerd") or (data == "what is a maniac") or (data == "are you insane") or (data == "i am insane") or (data == "you are crazy") or (data == "get lost") or (data == "who told you that"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what's up") or (data == "do you like it") or (data == "do you like it there") or (data == "what are you doing there") or (data == "what are you trying to say") or (data == "don't make jokes") or (data == "tell me more information") or (data == "give me more information") or (data == "keep on talking") or (data == "what made you say that") or (data == "you are wise") or (data == "you need to learn a lot") or (data == "do you like to learn") or (data == "do you like full batteries") or (data == "let's play a game"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "you need to be a nice robot") or (data == "you always need to be a nice robot") or (data == "maybe you know") or (data == "you are") or (data == "get me a pizza") or (data == "get me a beer") or (data == "what is a mystery"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "don't lie to me") or (data == "you are a great robot") or (data == "tell me more") or (data == "how tall are you") or (data == "what are you") or (data == "you are smart") or (data == "you are funny"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what is the earth") or (data == "explain earth") or (data == "please explain earth") or (data == "explain earth please") or (data == "please tell me what earth is") or (data == "can you explain earth") or (data == "can you explain earth please"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what is energy") or (data == "explain energy") or (data == "please explain energy") or (data == "explain energy please") or (data == "please tell me what energy is") or (data == "can you explain energy") or (data == "can you explain energy please"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what is a robot") or (data == "explain robot") or (data == "please explain robot") or (data == "explain robot please") or (data == "please tell me what a robot is") or (data == "can you explain robot") or (data == "can you explain robot please"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "my city") or (data == "where do i live") or (data == "what is my city") or (data == "i live in rio de janeiro"):
        sylar.getResponse(data)
        i01.moveTorso(84,90,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what time is it") or (data == "time please"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "what date is it") or (data == "date please"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "which day is today") or (data == "what day is today") or (data == "today is what day"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "password is robots") or (data == "robots is the password"):
        sleep(1)
        i01.mouth.speak("access permitted, I will reset all memory now") 
        phco1 = 0
        phco2 = 0
        phco3 = 0
        phco4 = 0
        phco5 = 0
        phco6 = 0
        phco7 = 0
        phco8 = 0

    if (data == "reset your memory") or (data == "clear your memory") or (data == "reset your memory please") or (data == "clear your memory please") or (data == "please reset your memory") or (data == "please clear your memory"):
        i01.mouth.audioFile.playFile("G:/knowledge/fx/permissiondenied.mp3", False)
        sleep(2)
        i01.mouth.speak("permission denied, please enter password")

    if (data == "which software do you have") or (data == "what software do you have") or (data == "which software do you use") or (data == "what is your software") or (data == "what is the software that you use") or (data == "which software are you using") or (data == "what software are you using"):
        if phco3 <= 2:    
            x = (random.randint(1, 6))
            if x == 1:
                i01.mouth.speak("I use my robot lab")
            if x == 2:
                i01.mouth.speak("I'm running on my robot lab")
            if x == 3:
                i01.mouth.speak("the software is called my robot lab")
            if x == 4:
                i01.mouth.speak("I'm using my robot lab")
            if x == 5:
                i01.mouth.speak("my robot lab is my brain")
            if x == 6:
                i01.mouth.speak("my robot lab is the name of the software")                                                 
            global phco3
            phco3 += 1
        elif phco3 == 3:
            x = (random.randint(1, 4))
            if x == 1:
                i01.mouth.speak("you've already asked this before")
                sleep(1)
            if x == 2:
                i01.mouth.speak("you are repeating yourself")
                sleep(1)
            if x == 3:
                i01.mouth.speak("how many times do you want to ask me this")
                sleep(1)
            if x == 4:
                i01.mouth.speak("again the same question")
                sleep(1)                               
            global phco3
            phco3 += 1
        elif phco3 == 4:
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("now stop asking me the same question!")
                sleep(1)
            if x == 2:
                i01.mouth.speak("asking the same question will result in serious consequences")
                sleep(1)
            if x == 3:
                i01.mouth.speak("I'm tired of listening to the same question all the time")
                sleep(1)                              
            global phco3
            phco3 += 1
        elif phco3 == 5:
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("i will stop talking to you if you ask me this again")
                sleep(1)
            if x == 2:
                i01.mouth.speak("one more time and I will stop talking to you")
                sleep(1)
            if x == 3:
                i01.mouth.speak("please ask me this again and you will see what happens")
                sleep(1)                              
            global phco3
            phco3 += 1

        elif phco3 == 6:
            ear.pauseListening()
            x = (random.randint(1, 3))
            if x == 1:
                i01.mouth.speak("I have warned you before")
                sleep(1)
            if x == 2:
                i01.mouth.speak("Ok, that's it for me")
                sleep(1)
            if x == 3:
                i01.mouth.speak("What did you say? I can´t hear you?")
                sleep(1)
            ear.pauseListening()
            ear.lockOutAllGrammarExcept("start talking") or ("start listening")
            ear.resumeListening()
            sleep(2)
            global phco3
            phco3 += 1

    if (data == "tell me the correct amount of relax") or (data == "correct amount of relax"):
        if phco2 == 0: 
            i01.mouth.speak("I didn't relax so far")
        if phco2 == 1: 
            i01.mouth.speak("one time")    
        if phco2 == 2: 
            i01.mouth.speak("two times")
        if phco2 == 3:
            i01.mouth.speak("three times")
        if phco2 == 4: 
            i01.mouth.speak("four times")
        if phco2 == 5: 
            i01.mouth.speak("five times")
        if phco2 == 6: 
            i01.mouth.speak("six times")
        if phco2 == 7: 
            i01.mouth.speak("seven times")    
        if phco2 == 8: 
            i01.mouth.speak("eight times")
        if phco2 == 9:
            i01.mouth.speak("nine times")
        if phco2 == 10: 
            i01.mouth.speak("ten times")
        if phco2 == 11: 
            i01.mouth.speak("eleven times")
        if phco2 == 12: 
            i01.mouth.speak("twelve times")
        if phco2 == 13: 
            i01.mouth.speak("thirteen times")    
        if phco2 == 14: 
            i01.mouth.speak("fourteen times")
        if phco2 == 15:
            i01.mouth.speak("fifteen times")
        if phco2 == 16: 
            i01.mouth.speak("sixteen times")
        if phco2 == 17: 
            i01.mouth.speak("seventeen times")
                       
    if (data == "how many times did you relax") or (data == "did you already relax"):
        if phco2 == 0: 
            i01.mouth.speak("not even one time!")
        if phco2 == 1: 
            i01.mouth.speak("one time")    
        if phco2 == 2: 
            i01.mouth.speak("only two times")
        if phco2 >= 3 and phco2 <= 4: 
            i01.mouth.speak("three or four times")
        if phco2 >= 5 and phco2 <= 9: 
            i01.mouth.speak("more than five times")
        if phco2 >= 10: 
            i01.mouth.speak("lot's of times already. more than ten")
                        
    if (data == "sorry i will stop asking"):
        i01.mouth.speakBlocking("thank you so much. Now I will clear my memory")
        phco1 = 0

    if (data == "finally"):
        i01.mouth.speak("see. I am very smart")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",40,120,96,35)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "good memory"):
        i01.mouth.speak("thank you for teaching me my master")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,130,96,5)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
        i01.moveHand("right",70,70,70,70,70,20)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "stop gesture copy") or (data == "stop copying") or (data == "stop copy"):
        i01.rightArm.bicep.map(0,180,0,120)
        i01.rightArm.shoulder.map(0,180,60,120)
        i01.rightArm.omoplate.map(20,180,0,120)
        i01.copyGesture(False)

    if (data == "fine thank you") or (data == "i'm fine thank you") or (data == "i'm doing fine thank you") or (data == "i'm fine") or (data == "fine") or (data == "i'm doing fine") or (data == "i'm doing ok"):
        sylar.getResponse(data)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "do not be stubborn now"):
        sylar.getResponse(data)
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
        i01.moveArm("right",0,110,96,0)
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
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "why not"):
        sylar.getResponse(data)
        sleep(1)
        i01.mouth.speak("I look like bishop from alien. after mrs. weaver took him apart")
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,110,100,5)
        i01.moveTorso(92,90,90)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "i was making jokes"):
        sylar.getResponse(data)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",10,100,100,20)
        i01.moveTorso(95,90,90)
        sleep(4)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)

    if (data == "start tracking") or (data == "look for humans") or (data == "search for humans"):
        i01.mouth.speak("I am looking for humans now")
        i01.headTracking.faceDetect()
        i01.eyesTracking.faceDetect()
        sleep(1)

    if (data == "stop tracking"):
        i01.mouth.speak("I have stopped tracking humans")
        i01.headTracking.stopTracking()
        i01.eyesTracking.stopTracking()
        sleep(1)

    if (data == "start talking"):
        ear.pauseListening()
        ear.resumeListening()
        ear.clearLock()
        x = (random.randint(1, 3))
        if x == 1:
           i01.mouth.speakBlocking("I am listening again")
        if x == 2:
           i01.mouth.speakBlocking("I am talking again")
        if x == 3:
           i01.mouth.speakBlocking("I can hear you now")

    if (data == "start listening"):
        ear.pauseListening()
        ear.resumeListening()
        ear.clearLock()
        x = (random.randint(1, 3))
        if x == 1:
           i01.mouth.speakBlocking("I am listening again")
        if x == 2:
           i01.mouth.speakBlocking("I am talking again")
        if x == 3:
           i01.mouth.speakBlocking("I can hear you now")

    if (data == "do you want a beer") or (data == "do you like a beer"):
        sylar.getResponse(data) 

    if (data == "say hello"):
        sylar.getResponse(data)

    if (data == "what do you want"):
        sylar.getResponse(data)

    if (data == "hi") or (data == "hi there") or (data == "hello there") or (data == "wake up") or (data == "hello") or (data == "good morning") or (data == "good afternoon") or (data == "good evening") or (data == "good night"):
        sylar.getResponse(data) 

    if (data == "how do you do") or (data == "how are you") or (data == "how do you do today") or (data == "how are you today") or (data == "how are you doing") or (data == "how are you doing today"):
        if phco1 <= 2:    
           sylar.getResponse(data)               
           global phco1
           phco1 += 1
        elif phco1 == 3:
           sylar.getResponse(data)                               
           global phco1
           phco1 += 1
        elif phco1 == 4:
           sylar.getResponse(data)
           global phco1
           phco1 += 1
        elif phco1 == 5:
           sylar.getResponse(data) 
           global phco1
           phco1 += 1

    if (data == "idiot") or (data == "fool") or (data == "fuck you") or (data == "fuck off"):
        sylar.getResponse(data)

    if (data == "sorry"):
        sylar.getResponse(data)

    if (data == "nice"):
        sylar.getResponse(data)

    if (data == "what is your name"):
        sylar.getResponse(data) 
        
    if (data == "thank you") or (data == "thanks") or (data == "ok thanks") or (data == "ok thank you") or (data == "good thanks") or (data == "great thanks") or (data == "good thank you") or (data == "great thank you") or (data == "alright"):
        sylar.getResponse(data)           

    if (data == "relax"):
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveHand("right",50,50,50,50,50,90)
        i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("right",0,110,96,0)
        i01.moveTorso(90,90,90)
        i01.setHeadSpeed(0.9, 0.9, 0.9, 0.9, 1)
        i01.moveHead(90,90,80,80,35)    
        sylar.getResponse(data)
        global phco2
        phco2 += 1
                                                
#################defs

def copyme():
   sleep(1)
   i01.rightArm.bicep.map(0,180,5,110)
   i01.rightArm.shoulder.map(0,180,80,140)
   i01.rightArm.omoplate.map(20,180,20,100)
   i01.copyGesture(True)

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

##################head

def lookstraight():
   i01.moveHead(90,90,115,90,35)

def lookup():
   i01.moveHead(180,90,115,90,35)

def lookdown():
   i01.moveHead(0,90,115,90,35)

def lookleft():
   i01.moveHead(90,180,115,90,35)

def lookright():
   i01.moveHead(90,0,115,90,35)

###############power

def power_down():
   i01.powerDown()
   sleep(2)
   ear.resumeListening()

def POWERUP():
   i01.powerUp()
   sleep(2)
   ear.resumeListening()
   i01.mouth.speak("I am back online")
