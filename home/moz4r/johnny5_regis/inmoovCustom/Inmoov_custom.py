# -- coding: utf-8 --
# #############################################################################
#                           YOUR INMOOV CUSTOM
# Here you can add your own commands to play and test with inmoov
# If you udpate the whole script, don't worry, those commands are safe
# ##############################################################################



talkBlocking("Bonjour ! comment sa va")


ear.addCommand(u"ouvre les yeux", "python", "paupiereOuvre")
ear.addCommand(u"ferme les yeux", "python", "paupiereFerme")

def paupiereOuvre():
	rotationCylindre.moveTo(180)
	berceau.moveTo(180)
	
def paupiereFerme():
	rotationCylindre.moveTo(0)
	berceau.moveTo(0)

