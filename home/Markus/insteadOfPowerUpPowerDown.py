Pin12 = 0
resttimer = 0
 
right.digitalReadPollingStart(Pin12)
 
# make friendly sample rate
right.setSampleRate(3000)
 
right.addListener("publishPin", "python", "publishPin")
 
 
def publishPin(pin):
#  print pin.pin, pin.value, pin.type, pin.source,
 
 
  if (pin.pin == 12 and pin.value == 1):
      if pin12 == 0:
          i01.mouth.speak("hello")
          global pin12
          pin12 = 1
          i01.head.attach()
          sleep(1)
          ear.clearLock()
          headfront()
          sleep(2)
          trackHumans()
 
  if (pin.pin == 12 and pin.value == 0):
      if pin12 == 1:
          global resttimer
          resttimer += 1
          if resttimer == 400:
              global resttimer
              resttimer = 0
              gotosleepnow() 