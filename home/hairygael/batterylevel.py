def batterylevel():
  power_now = subprocess.check_output(["WMIC","PATH","Win32_Battery","Get","EstimatedChargeRemaining"])
  battery = power_now.split("\n")[1].strip()
  # print battery
  i01.mouth.speak(str(battery) + " percent")
