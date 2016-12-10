def power_up():
  neopixel.setAnimation("Ironman",0,0,255,1)
  headTilt.attach()
  if(language == "english"):
    i01.mouth.speak("powering up")
  else:
    i01.mouth.speak("Je me réveille")
