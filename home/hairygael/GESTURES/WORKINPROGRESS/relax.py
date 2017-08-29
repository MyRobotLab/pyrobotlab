def relax():
  global MoveBodyRandom
  MoveBodyRandom==1
  global MoveHeadRandom
  if (i01.eyesTracking.getOpenCV().capturing):
       MoveHeadRandom==0
       i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
       i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
       i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
       i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
       i01.setHeadSpeed(0.85, 0.85)
       i01.setTorsoSpeed(0.75, 0.55, 1.0)
       i01.moveHead(79,100)
       i01.moveArm("left",5,84,28,14)
       i01.moveArm("right",5,82,28,16)
       i01.moveHand("left",92,33,37,71,66,25)
       i01.moveHand("right",81,66,82,60,105,113)
       i01.moveTorso(95,90,90)

  else:
       MoveHeadRandom==1
       i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
       i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
       i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
       i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
       i01.setHeadSpeed(0.85, 0.85)
       i01.setTorsoSpeed(0.75, 0.55, 1.0)
       #i01.moveHead(79,100)
       i01.moveArm("left",5,84,28,14)
       i01.moveArm("right",5,82,28,16)
       i01.moveHand("left",92,33,37,71,66,25)
       i01.moveHand("right",81,66,82,60,105,113)
       i01.moveTorso(95,90,90)
