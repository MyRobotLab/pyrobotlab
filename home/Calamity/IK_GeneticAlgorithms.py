#start ik service
ik=Runtime.createAndStart("ik","IntegratedMovement");

#arduino service
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM15")

#define and attach servo
#map is set so servo accept angle as input, output where
#they need to go so that their part they where attach to
#move by the input degree
mtorso = Runtime.createAndStart("mtorso","Servo")
mtorso.attach(arduino,28,90);
mtorso.map(15,165,38,148);
#mtorso.setMinMax(35,150)
mtorso.setVelocity(13)
mtorso.moveTo(90)
ttorso = Runtime.createAndStart("ttorso","Servo")
ttorso.attach(arduino,27,90);
ttorso.map(60,120,120,90);
ttorso.setInverted(False)
#ttorso.setMinMax(85,125)
ttorso.setVelocity(13)
ttorso.moveTo(90)
omoplate = Runtime.createAndStart("omoplate","Servo")
omoplate.attach(arduino,11,10);
omoplate.map(10,70,10,70)
omoplate.setVelocity(15)
#omoplate.setMinMax(10,70)
omoplate.moveTo(10)
shoulder = Runtime.createAndStart("shoulder","Servo")
shoulder.attach(arduino,10,30);
shoulder.map(0,180,0,180)
#shoulder.setMinMax(0,180)
shoulder.setVelocity(14)
shoulder.moveTo(20)
rotate = Runtime.createAndStart("rotate","Servo")
rotate.attach(arduino,9,90);
rotate.map(46,160,46,160)
#rotate.setMinMax(46,180)
rotate.setVelocity(18)
rotate.moveTo(90)
bicep = Runtime.createAndStart("bicep","Servo")
bicep.attach(arduino,8,10);
bicep.map(5,60,5,80)
bicep.setVelocity(26)
#bicep.setMinMax(5,90)
bicep.moveTo(10)
wrist = Runtime.createAndStart("wrist","Servo")
wrist.attach(arduino,7,10);
wrist.map(45,135,45,135)
wrist.setVelocity(26)
#bicep.setMinMax(5,90)
wrist.moveTo(90)
finger = Runtime.createAndStart("finger","Servo")
finger.attach(arduino,8,90);
finger.map(90,90,90,90)
finger.setVelocity(26)
#bicep.setMinMax(5,90)
finger.moveTo(90)

#define the DH parameters for the ik service
ik.setNewDHRobotArm()
ik.setDHLink(mtorso,113,90,0,-90)
ik.setDHLink(ttorso,0,90+65.6,346,0)
ik.setDHLink(omoplate,0,-5.6+24.4+180,55,-90)
ik.setDHLink(shoulder,77,-20+90,0,90)
ik.setDHLink(rotate,284,90,40,90)
ik.setDHLink(bicep,0,-7+24.4+90,300,90)
ik.setDHLink(wrist,00,-90,200,0)


#define object, each dh link are set as an object, but the
#start point and end point will be update by the ik service, but still need
#a name and a radius
#static object need a start point, an end point, a name and a radius 
ik.clearObject()
ik.addObject(0.0, 0.0, 0.0, 0.0, 0.0, -150.0, "base", 150.0)
ik.addObject("mtorso", 150.0)
ik.addObject("ttorso", 10.0)
ik.addObject("omoplate", 10.0)
ik.addObject("shoulder", 50.0)
ik.addObject("rotate", 50.0)
ik.addObject("bicep", 60.0)
ik.addObject("wrist", 70.0)
ik.addObject(-1000.0, 300, 0, 1000, 300, 00, "obstacle",40)


print ik.currentPosition();

#setting ik parameters for the computing
ik.setComputeMethodGeneticAlgorythm()
ik.setGeneticComputeSimulation(False)

#move to a position
ik.moveTo(350,400,1000)

print ik.currentPosition();

