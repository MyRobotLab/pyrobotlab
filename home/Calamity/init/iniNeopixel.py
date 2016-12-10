neopixel = Runtime.createAndStart("neopixel","NeoPixel")
def startNeopixel():
  neopixel.attach(i01.arduinos.get(rightPort),23,16)
  neopixel.setAnimation("Ironman",0,0,255,1)
pinocchioLying = False
  
def onStartSpeaking(data):
  if (pinocchioLying):
    neopixel.setAnimation("Ironman",0,255,0,1)
  else:
    neopixel.setAnimation("Ironman",255,0,0,1)
  
def onEndSpeaking(data):
  if (pinocchioLying):
    neopixel.setAnimation("Ironman",0,127,127,1)
    global pinocchioLying
    pinocchioLying = False
  else:
    neopixel.setAnimation("Ironman",0,0,255,1)
  
i01.mouth.addListener("publishStartSpeaking","python","onStartSpeaking")
i01.mouth.addListener("publishEndSpeaking","python","onEndSpeaking")
