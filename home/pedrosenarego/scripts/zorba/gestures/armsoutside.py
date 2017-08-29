def armsoutside():
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.rightArm.rotate.attach()
  i01.rightArm.rotate.moveTo(180)
  sleep(7)
  i01.rightArm.rotate.detach()
  