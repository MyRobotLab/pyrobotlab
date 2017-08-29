def bicepup():
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.rightArm.bicep.attach()
  i01.rightArm.bicep.moveTo(180)
  sleep(1)
  i01.rightArm.bicep.detach()
  