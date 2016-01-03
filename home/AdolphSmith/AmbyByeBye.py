arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM9")
 
mouth = Runtime.create("mouth","Speech")
 
s8 = Runtime.createAndStart("s8","Servo")
s9 = Runtime.createAndStart("s9","Servo")
s10 = Runtime.createAndStart("s10","Servo")
s11 = Runtime.createAndStart("s11","Servo")
s13 = Runtime.createAndStart("s13","Servo")
s14 = Runtime.createAndStart("s14","Servo")
# s15 = Runtime.createAndStart("s15","Servo")
s16 = Runtime.createAndStart("s16","Servo")
s17 = Runtime.createAndStart("s17","Servo")
# s34 = Runtime.createAndStart("s43","Servo")
# s35 = Runtime.createAndStart("s35","Servo")
# s30 = Runtime.createAndStart("s30","Servo")
# s31 = Runtime.createAndStart("s31","Servo")
# s36 = Runtime.createAndStart("s36","Servo")
# s37 = Runtime.createAndStart("s37","Servo")
# s38 = Runtime.createAndStart("s38","Servo")
# s39 = Runtime.createAndStart("s39","Servo")
# s42 = Runtime.createAndStart("s42","Servo")
# s43 = Runtime.createAndStart("s43","Servo")
# s26 = Runtime.createAndStart("s26","Servo")
 
s8.setRest(12)  # Left Elbow
s9.setRest(75) # left arm Turn
s10.setRest(103)  # left Shaulder up
s11.setRest(123) # Left Omniplate
s13.setRest(81) # Neck Turn
s14.setRest(93) # Right Arm Up
# s15.setRest(63) # Right Omniplate
s16.setRest(79) # Right Arm Turn 
s17.setRest(138) # Right Elbow
# s34.setRest(66) # Left Hip
# s35.setRest(126) # Right Hip
# s30.setRest(97) # Left Leg Turn 
# s31.setRest(120) # Right Leg Turn
# s36.setRest(54) # Left Leg Up
# s37.setRest(46) # Right Leg up
# s38.setRest(75) # Knee Left 
# s39.setRest(75) # Knee Right 
# s42.setRest(132) # Ankle Left
# s43.setRest(89) # Ankle Right 
# s26.setRest(71) # Mouth
 
s8.attach("arduino",8)
s9.attach("arduino",9)
s10.attach("arduino",10)
s11.attach("arduino",11)
s13.attach("arduino",13)
s17.attach("ardiuno",17)
s16.attach("ardiuno",16)
s14.attach("ardiuno",14)
 
 
def rest():
s8.rest()   # right shoulder
s9.rest()  # right arm up
s10.rest()   # right elbow
s13.rest()  # head\
s11.rest()
s17.rest() 
s16.rest()
s14.rest()
 
 
def wave():
s8.moveTo(9)
s9.moveTo(80)
s8.moveTo(7)
s8.moveTo(105)
s9.moveTo(157)
s10.moveTo(6)
s8.moveTo(149)
sleep(0.4)
s8.moveTo(60)
sleep(0.4)
s8.moveTo(149)
sleep(0.4)
s8.moveTo(60)
sleep(0.4)
s8.moveTo(135)
s10.moveTo(102)
s9.moveTo(68)
s8.moveTo(1)
 
def bye():
s17.moveTo(139)
s16.moveTo(81)
s17.moveTo(53)
s16.moveTo(157)
s14.moveTo(0)
s17.moveTo(5)
s17.moveTo(74)
sleep(0.4)
s17.moveTo(1)
sleep(0.4)
s17.moveTo(74)
sleep(0.4)
s17.moveTo(1)
sleep(0.4)
s17.moveTo(32)
s14.moveTo(98)
s16.moveTo(83)
s17.moveTo(136)
 
 
 
def attach():
s8.attach()   # right shoulder
s9.attach()  # right arm up
s10.attach()   # Left elbow
s11.attach()   # Left Omniplate
s13.attach()  # head
s14.attach()
s16.attach()
s17.attach()
 
def detach():
s8.detach()   # Left shoulder
s9.detach()  # Left arm up
s10.detach()   # Left elbow
s11.detach()   # Left Omniplate
s13.detach()  # Neck Turn
s14.detach()
s16.detach()
s17.detach() 
 
for x in range(0, 3):
attach()
# do a gesture
 
 
rest()
mouth.speakBlocking("I want to show you what i can do")
mouth.speakBlocking("I am the new Amby bot made by Adolph")
mouth.speakBlocking("Hello every one")
wave()
sleep(1)
rest()
sleep(1)
 
# wait for a second
sleep(1)
# do another gesture
mouth.speakBlocking("I think you are going to like me")
s13.moveTo(36) # Neck Turn
mouth.speakBlocking("I am alive")
sleep(0.5)
s13.moveTo(109) # Neck Turn
sleep(0.5)
mouth.speakBlocking("I am alive thrue mirobotlab")
s13.moveTo(62) # Neck Turn
sleep(0.5)
mouth.speakBlocking("I like you all")
s13.moveTo(36) # Neck Turn
sleep(0.2)
s13.moveTo(109) # Neck Turn
sleep(0.2)
s13.rest()
 
mouth.speakBlocking("You all are nice")
 
mouth.speakBlocking("Bye Bye Guys")
wave()
sleep(1)
rest()
sleep(1)
 
