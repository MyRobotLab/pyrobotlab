

if LeftPortIsConnected :
  leftArduino = runtime.getService("i01.left")
  
  if isTorsoActivated :
    i01.mouth.speak("Fixing torso servos")
    sleep(2)

    servoTopStom = Runtime.getService('i01.torso.topStom')
    servoTopStom.setPin(27)
    leftArduino.attach(servoTopStom)

    servoMidStom = Runtime.getService('i01.torso.midStom')
    servoMidStom.setPin(28)
    leftArduino.attach(servoMidStom)

    servoLowStom = Runtime.getService('i01.torso.lowStom')
    servoLowStom.setPin(29)
    leftArduino.attach(servoLowStom)
  else :
    i01.mouth.speak("torso not activated")
    sleep(2) 
    
  if isHeadActivated :    
    i01.mouth.speak("fixing head servos")
    sleep(2)

    servoNeck = Runtime.getService('i01.head.rothead')
    servoNeck.detach(leftArduino)
    servoNeck.setPin(13)
    leftArduino.attach(servoNeck)

    servoNeck = Runtime.getService('i01.head.neck')
    servoNeck.detach(leftArduino)
    servoNeck.setPin(12)
    leftArduino.attach(servoNeck)
  else :
    i01.mouth.speak("head is not activated")
    sleep(2) 
    
  if isLeftArmActivated :    
    i01.mouth.speak("fixing left arm servos")
    sleep(2)

    servoLeftBicep = Runtime.getService('i01.leftArm.bicep')
    servoLeftBicep.detach(leftArduino)
    servoLeftBicep.setPin(8)
    leftArduino.attach(servoLeftBicep)

    servoLeftrotate = Runtime.getService('i01.leftArm.rotate')
    servoLeftrotate.detach(leftArduino)
    servoLeftrotate.setPin(9)
    leftArduino.attach(servoLeftrotate)

    servoLeftshoulder = Runtime.getService('i01.leftArm.shoulder')
    servoLeftshoulder.detach(leftArduino)
    servoLeftshoulder.setPin(10)
    leftArduino.attach(servoLeftshoulder)

    servoLeftomoplate = Runtime.getService('i01.leftArm.omoplate')
    servoLeftomoplate.detach(leftArduino)
    servoLeftomoplate.setPin(11)
    leftArduino.attach(servoLeftomoplate)
  else :
    i01.mouth.speak("left arm is not activated")
    sleep(2)    
else :
  i01.mouth.speak("left arduino not activated")
  sleep(2)  



if RightPortIsConnected :
  rightArduino = runtime.getService("i01.right")
  
  if isRightArmActivated :
    i01.mouth.speak("fixing right arm servos")
    sleep(2)

    servorightBicep = Runtime.getService('i01.rightArm.bicep')
    servorightBicep.detach(rightArduino)
    servorightBicep.setPin(8)
    rightArduino.attach(servorightBicep)

    servorightrotate = Runtime.getService('i01.rightArm.rotate')
    servorightrotate.detach(rightArduino)
    servorightrotate.setPin(9)
    rightArduino.attach(servorightrotate)

    servorightshoulder = Runtime.getService('i01.rightArm.shoulder')
    servorightshoulder.detach(rightArduino)
    servorightshoulder.setPin(10)
    rightArduino.attach(servorightshoulder)

    servorightomoplate = Runtime.getService('i01.rightArm.omoplate')
    servorightomoplate.detach(rightArduino)
    servorightomoplate.setPin(11)
    rightArduino.attach(servorightomoplate)
  else :
    i01.mouth.speak("right arm is not activated")
    sleep(2)    
else :
  i01.mouth.speak("right arduino not activated")  
  sleep(2)
  

i01.mouth.speak("i am done fixing servos")
sleep(2)
