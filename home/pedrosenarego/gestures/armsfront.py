def armsfront():
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.rightArm.shoulder.attach()
  i01.rightArm.shoulder.moveTo(180)
  sleep(8)
  i01.rightArm.shoulder.detach()
  