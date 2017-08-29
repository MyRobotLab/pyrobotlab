def rest():
  i01.rightHand.attach()
  i01.moveHand("right",2,2,2,2,2,88)
  i01.rightArm.rotate.attach()
  i01.rightArm.rotate.moveTo(94)
  i01.rightArm.omoplate.attach()
  i01.rightArm.omoplate.moveTo(0)
  i01.rightArm.shoulder.attach()
  i01.rightArm.shoulder.moveTo(30)
  i01.setHeadSpeed(1.0,1.0)
  i01.head.neck.attach()
  i01.head.neck.moveTo(75)
  i01.head.rothead.attach()
  i01.head.rothead.moveTo(88)
  leftneckServo.attach(right, 13)
  rightneckServo.attach(right, 12)
  delta = 20 
  neckMoveTo(restPos,delta)
  sleep(6)
  leftneckServo.detach()
  rightneckServo.detach()
  i01.detach()
  
  