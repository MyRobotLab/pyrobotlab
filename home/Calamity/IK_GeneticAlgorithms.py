ik=Runtime.createAndStart("ik","InverseKinematics3D");

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM15")

mtorso = Runtime.createAndStart("mtorso","Servo")
mtorso.attach(arduino,2,90);
mtorso.map(0,180,35,150);
mtorso.setMaxVelocity(13)
mtorso.moveTo(90)
ttorso = Runtime.createAndStart("ttorso","Servo")
ttorso.attach(arduino,3,90);
ttorso.map(0,180,85,125);
ttorso.setMaxVelocity(13)
ttorso.moveTo(90)
omoplate = Runtime.createAndStart("omoplate","Servo")
omoplate.attach(arduino,4,10);
omoplate.map(0,180,10,75)
omoplate.setMaxVelocity(15)
omoplate.moveTo(10)
shoulder = Runtime.createAndStart("shoulder","Servo")
shoulder.attach(arduino,5,30);
shoulder.map(0,180,25,180)
shoulder.setMaxVelocity(14)
shoulder.moveTo(30)
rotate = Runtime.createAndStart("rotate","Servo")
rotate.attach(arduino,6,90);
rotate.map(0,180,46,180)
rotate.setMaxVelocity(18)
rotate.moveTo(90)
bicep = Runtime.createAndStart("bicep","Servo")
bicep.attach(arduino,7,10);
bicep.map(0,180,10,80)
bicep.setMaxVelocity(26)
bicep.moveTo(10)


ik.setNewDHRobotArm()
ik.setDHLink(mtorso,110,-90,0,90)
ik.setDHLink(ttorso,0,-90+65.6+0,346,0)
ik.setDHLink(omoplate,0,24.4+180,40,-90)
ik.setDHLink(shoulder,80,-30+90+180,0,-90)
ik.setDHLink(rotate,280,90,-40,-90)
ik.setDHLink(bicep,0,-90,190,-0)

print ik.currentPosition();

ik.moveTo(200,200,200)

print ik.currentPosition();

print mtorso.targetOutput
print ttorso.targetOutput
print omoplate.targetOutput
print shoulder.targetOutput
print rotate.targetOutput
print bicep.targetOutput
