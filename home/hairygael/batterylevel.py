def batterylevel():
  power_now = subprocess.call ("WMIC PATH Win32_Battery Get EstimatedChargeRemaining", "r".readline())
  ANSWER = float(power_now) * 100 , "%"
  i01.mouth.speak(str(ANSWER))
