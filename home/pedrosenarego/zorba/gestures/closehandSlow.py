def closehandSlow():
  i01.rightHand.attach()
  i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak("closing slowly")
  sleep(0.5)
  i01.rightHand.detach()