def headup():
  i01.setHeadSpeed(1.0,1.0)
  i01.head.neck.attach()
  i01.head.neck.moveTo(180)
  sleep(0.5)
  i01.head.neck.detach()
  