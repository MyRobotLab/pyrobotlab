def closehand():
  i01.rightHand.attach()
  i01.moveHand("right",138,180,180,180,180)
  i01.mouth.speak("Hands closed, on your neck....")
  sleep(0.5)
  i01.detach()