# Domotique @Lecanois

def allume(phrase):
	talk(phrase)
	Parse("http://192.168.1.27/lumieres.php")
	

def eteins(phrase):
	talk(phrase)
	Parse("http://192.168.1.27/lumiereoffs.php")