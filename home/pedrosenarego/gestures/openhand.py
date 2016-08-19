def openhand():
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.rightHand.attach()
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak("Hands open, come closer, come closer") 
  sleep(0.5)
  i01.rightHand.detach()