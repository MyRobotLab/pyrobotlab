def headright():
  i01.setHeadSpeed(1.0,1.0)
  i01.head.rothead.attach()
  i01.head.rothead.moveTo(0)
  sleep(1)
  i01.head.rothead.detach()
  