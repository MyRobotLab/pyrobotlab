def restHands():
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.rightHand.attach()
  i01.moveHand("right",2,2,2,2,2,88)
  sleep(0.3)
  i01.rightHand.detach()
  
  