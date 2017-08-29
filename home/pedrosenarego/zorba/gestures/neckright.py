def neckright():
  leftneckServo.attach(right, 13)
  rightneckServo.attach(right, 12)
  delta = -40
  neckMoveTo(restPos,delta)
  sleep(1)
  leftneckServo.detach()
  rightneckServo.detach()
  
  