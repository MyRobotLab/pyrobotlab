def rest():
  i01.setHeadSpeed(1.0,1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  #atach
  i01.head.neck.attach()
  i01.head.rothead.attach()
  i01.rightHand.attach()
  i01.rightArm.shoulder.attach()
  i01.rightArm.omoplate.attach()
  i01.rightArm.bicep.attach()
  leftneckServo.attach(right, 13)
  rightneckServo.attach(right, 12)
  sleep(0.5)
  #r.arm
  i01.moveArm("right",0,90,30,10)
  #head
  i01.head.neck.moveTo(75)
  i01.head.rothead.moveTo(88)
  #r.hand
  i01.moveHand("right",2,2,2,2,2,88)
  #roll neck
  delta = 20 
  neckMoveTo(restPos,delta)
  sleep(7)
  
  leftneckServo.detach()
  rightneckServo.detach()
  i01.detach()
  
  