def armsback():
  i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
  i01.rightArm.shoulder.attach()
  i01.rightArm.shoulder.moveTo(30)
  sleep(8)
  i01.rightArm.shoulder.detach()
  