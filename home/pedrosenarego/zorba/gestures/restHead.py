def restHead():
  i01.setHeadSpeed(1.0,1.0)
  i01.head.neck.attach()
  i01.head.neck.moveTo(75)
  i01.head.rothead.attach()
  i01.head.rothead.moveTo(88)
  leftneckServo.attach(right, 13)
  rightneckServo.attach(right, 12)
  delta = 20 
  neckMoveTo(restPos,delta)
  sleep(0.5)
  i01.head.neck.detach()
  i01.head.rothead.detach()
  leftneckServo.detach()
  rightneckServo.detach()
  
  