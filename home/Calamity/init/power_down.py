def power_down():
  headTilt.detach()
  neopixel.animationStop()
  if(language == "english"):
    i01.mouth.speak("powering down")
  else:
    i01.mouth.speak("J'entre en mode sommeil")
