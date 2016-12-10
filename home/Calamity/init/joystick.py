joystickInit = False;

def joystickInit():
  global uberjoy
  global controllerButtonMap
  global controllerButtonMapTrigger
  global controllerButtonReverse
  global controllerButtonTrigger
  global controllerButtonTriggerState
  global joystickInit
  if(joystickInit == False):
    uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
    uberjoy.setController(joystickId)

    controllerButtonMap={"x":i01.leftArm.rotate,"y":i01.leftArm.bicep,"z":i01.rightArm.rotate,"rz":i01.rightArm.bicep,"4":i01.head.neck,"5":i01.head.neck,"6":i01.head.rothead,"7":i01.head.rothead}
    controllerButtonMapTrigger={"x":i01.leftArm.omoplate,"y":i01.leftArm.shoulder,"z":i01.rightArm.omoplate,"rz":i01.rightArm.shoulder}
    controllerButtonReverse={"x":True,"y":True,"z":False,"rz":True,"4":True,"5":False,"6":True,"7":False}
    controllerButtonTrigger={"x":"10","y":"10","z":"11","rz":"11"}
    controllerButtonTriggerState={"10":False,"11":False}
    
    for button,servo in controllerButtonMap.iteritems():
      servo.setSpeedControlOnUC(False)

    uberjoy.addListener("publishInput", "python", "joystickOnPublishInput")
    joystickInit = True
  uberjoy.startPolling()
    
	
def joystickOnPublishInput(data):
  global controllerButtonTriggerState
  if(controllerButtonReverse.get(data.id)):
    data.value*=-1
  if(controllerButtonTriggerState.has_key(data.id)):
    print "trigger button pressed"
    for k,v in controllerButtonTrigger.iteritems():
      if v==data.id:
        if controllerButtonTriggerState.get(data.id):
          controllerButtonMapTrigger.get(k).stop()
        else:
          controllerButtonMap.get(k).stop()
    controllerButtonTriggerState[data.id]=bool(data.value)
    return
  if(controllerButtonMap.has_key(data.id)):
    servotmp=[None]
    if(controllerButtonMapTrigger.has_key(data.id)):
      print "found trigger "+data.id+" = "+ controllerButtonMapTrigger.get(data.id).getName()
      if(controllerButtonTriggerState.get(controllerButtonTrigger.get(data.id))):
        servotmp[0]=controllerButtonMapTrigger.get(data.id)
        print "using alt servo: "+servotmp[0].getName()
      else:
        servotmp[0]=controllerButtonMap.get(data.id)
        print "using normal servo: "+ servotmp[0].getName()
    else:
      servotmp[0]=controllerButtonMap.get(data.id)
      print "using normal servo: "+ servotmp[0].getName()
    servo=servotmp[0]
    print servo.getName()
    absValue = math.fabs(data.value)
    if (absValue < 0.300):
      servo.stop()
      return
    absValue = absValue-0.01
    servo.setSpeed(absValue)
    delay = int((1-absValue) * 200)+25
    servo.stop()
    if (data.value > 0.0):
      #servo.sweep(servo.getPos(), int(servo.getMax()), delay, 1, True)
      servo.sweep(servo.getPos(), 180, delay, 1, True)
    else:
      servo.sweep(0, servo.getPos(), delay, -1, True)
      
def stopJoystick():
  uberjoy.stopPolling()
  