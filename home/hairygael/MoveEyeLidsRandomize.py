# ##############################################################################
#            *** ROBOT MOVE THE EYELIDS RANDOMLY ***
# ##############################################################################

if isEyeLidsActivated:
  MoveEyeLidsTimer = Runtime.start("MoveEyeLidsTimer","Clock")

  def MoveEyeLids(timedata):
    #redefine next loop
    MoveEyeLidsTimer.setInterval(random.randint(100,10000))
    if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
      
      if isEyeLidsActivated:
        if EyeLidsLeftActivated and EyeLidsRightActivated:
          i01.eyelids.setVelocity(-1,-1)
          i01.eyelids.moveToBlocking(180,180)
          sleep(0.2)
          i01.eyelids.moveTo(0,0)
          sleep(0.1)
          i01.eyelids.disable()
        elif EyeLidsLeftActivated and not EyeLidsRightActivated:
          i01.eyelids.eyelidleft.setVelocity(-1)
          i01.eyelids.eyelidleft.moveToBlocking(180)
          sleep(0.2)
          i01.eyelids.eyelidleft.moveTo(0)
          sleep(0.1)
          i01.eyelids.eyelidleft.disable()
      else:
        MoveEyeLidsTimer.stopClock()
    
  #initial function
  def MoveEyeLidsStart():
    if isEyeLidsActivated:
      print "moveEyeLidsStart"
      if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
        MoveEyeLidsTimer.startClock()
      else:MoveEyeLidsTimer.stopClock()
      
  def MoveEyeLidsStop():
    
    if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
      if isEyeLidsActivated:
        if EyeLidsLeftActivated and EyeLidsRightActivated:
          MoveEyeLidsTimer.stopClock()
          i01.eyelids.setVelocity(-1,-1)
          i01.eyelids.rest()
        elif EyeLidsLeftActivated and not EyeLidsRightActivated:
          MoveEyeLidsTimer.stopClock()
          i01.eyelids.eyelidleft.setVelocity(-1)
          i01.eyelids.eyelidleft.rest()

  if RobotCanMoveEyeLids==1:
    MoveEyeLidsStart()
      
  MoveEyeLidsTimer.addListener("pulse", python.name, "MoveEyeLids")
  MoveEyeLidsTimer.addListener("clockStarted", python.name, "MoveEyeLidsStart")
  MoveEyeLidsTimer.addListener("clockStopped", python.name, "MoveEyeLidsStop")
