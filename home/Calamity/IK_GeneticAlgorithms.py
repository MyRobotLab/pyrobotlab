ik=Runtime.createAndStart("ik","InverseKinematics3D");

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM3")

mtorso = Runtime.createAndStart("mtorso","Servo")
mtorso.attach(arduino,28,90);
mtorso.map(15,165,38,148);
#mtorso.setMinMax(35,150)
mtorso.setVelocity(13)
mtorso.moveTo(90)
ttorso = Runtime.createAndStart("ttorso","Servo")
ttorso.attach(arduino,27,90);
ttorso.map(60,120,90,120);
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
rotate.map(0,160,0,160)
#rotate.setMinMax(46,180)
rotate.setVelocity(18)
rotate.moveTo(90)
bicep = Runtime.createAndStart("bicep","Servo")
bicep.attach(arduino,8,10);
bicep.map(5,60,5,80)
bicep.setVelocity(26)
#bicep.setMinMax(5,90)
bicep.moveTo(10)


ik.setNewDHRobotArm()
ik.setDHLink(mtorso,113,-90,0,90)
ik.setDHLink(ttorso,0,-90+65.6,346,0)
ik.setDHLink(omoplate,0,-5.6+24.4+180,55,-90)
ik.setDHLink(shoulder,77,-20+90,0,90)
ik.setDHLink(rotate,284,90,40,90)
ik.setDHLink(bicep,0,-7-90+24.4+180,480,-0)

ik.clearObject()
ik.addObject(0.0, 0.0, 0.0, 0.0, 0.0, -150.0, "base", 150.0)
ik.addObject("mtorso", 150.0)
ik.addObject("ttorso", 10.0)
ik.addObject("omoplate", 10.0)
ik.addObject("shoulder", 50.0)
ik.addObject("rotate", 50.0)
ik.addObject("bicep", 60.0)
#ik.addObject(-1000.0, 300, 0, 1000, 300, 00, "obstacle",40)


print ik.currentPosition();

ik.setComputeMethodGeneticAlgorythm()
ik.moveTo(350,400,300, -10, -30, 100)

print ik.currentPosition();

print "mtorso:" + str(mtorso.targetPos) + "-" + str(mtorso.targetOutput)
print "ttorso:" + str(ttorso.targetPos) + "-" + str(ttorso.targetOutput)
print "omoplate:" + str(omoplate.targetPos) + "-" + str(omoplate.targetOutput)
print "shoulder:" + str(shoulder.targetPos) + "-" + str(shoulder.targetOutput)
print "rotate:" + str(rotate.targetPos) + "-" + str(rotate.targetOutput)
print "bicep:" + str(bicep.targetPos) + "-" + str(bicep.targetOutput)

jp = ik.createJointPositionMap()

for i in range (1,len(jp)):
	print ik.getCurrentArm().getLink(i-1).getName() + " x:" +str(jp[i][0]) + " y:" + str(jp[i][1]) + " z:" + str(jp[i][2]) + " theta:" + str(ik.getCurrentArm().getLink(i-1).getThetaDegrees()) + " alpha:" 
