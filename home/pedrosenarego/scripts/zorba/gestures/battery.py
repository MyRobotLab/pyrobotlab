
def battery():
  power_now = open("/sys/class/power_supply/BAT0/energy_now", "r").readline()
  power_full = open("/sys/class/power_supply/BAT0/energy_full", "r").readline()
  a = float(power_now)/float(power_full) * 100
  i01.mouth.speak("%.0f" % a + "percent")

  
  

 



