#head
print("i01.moveHead("+str(i01.head.neck.getPos())+","+str(i01.head.rothead.getPos())+","+str(i01.head.eyeX.getPos())+","+str(i01.head.eyeY.getPos())+","+str(i01.head.jaw.getPos())+","+str(i01.head.rollNeck.getPos())+")") 

#arm
print "i01.moveArm(\"left\","+str(i01.leftArm.bicep.getPos())+","+str(i01.leftArm.rotate.getPos())+","+str(i01.leftArm.shoulder.getPos())+","+str(i01.leftArm.omoplate.getPos())+")"

#hand
print "i01.moveHand(\"left\","+str(i01.leftHand.thumb.getPos())+","+str(i01.leftHand.index.getPos())+","+str(i01.leftHand.majeure.getPos())+","+str(i01.leftHand.ringFinger.getPos())+","+str(i01.leftHand.wrist.getPos())+")"

#torso
print "i01.moveTorso("+str(i01.torso.topStom.getPos())+","+str(i01.torso.midStom.getPos())+","+str(i01.torso.lowStom.getPos())+")"
