# Domotique @Lecanois

def allume(phrase):
	talk(phrase)
	Parse("http://192.168.1.27/lumieres.php")
	

def eteins(phrase):
	talk(phrase)
	Parse("http://192.168.1.27/lumiereoffs.php")
	
#RELAY CONTROL TO SHUTDOWN SERVO
sleep(0.1)
left.pinMode(53, Arduino.OUTPUT)
left.pinMode(51, Arduino.OUTPUT)
right.pinMode(53, Arduino.OUTPUT)
right.pinMode(51, Arduino.OUTPUT)
left.digitalWrite(53,255)
left.digitalWrite(51,255)
right.digitalWrite(53,255)
right.digitalWrite(51,255)