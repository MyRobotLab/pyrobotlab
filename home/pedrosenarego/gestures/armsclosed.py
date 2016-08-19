def armsclosed():
  i01.setArmSpeed("right", 0.9, 0.9, 0.9, 0.9)
  i01.rightArm.omoplate.attach()
  i01.rightArm.omoplate.moveTo(0)
  sleep(2)
  i01.rightArm.omoplate.detach()
  