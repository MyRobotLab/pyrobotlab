#! usr/bin/python 
# -*- coding: ISO-8859-1 -*- 

# Variable global
CompteurTraking = 0
TRACKING= False #True
client = S7Client()
MODEVIDEO = 0  # 0= arret 1= traking visage 2= reconnaissance
INTERLOCUTEUR = "Defaut"

#Arduino
Arduino1 = 1 # 0 = sans arduino 1 = avec arduino
Arduino2 = 0 # 0 = sans arduino 1 = avec arduino
Arduino1Com = "COM4"


#syntèse vocal
SynteseVocal = 1	# 0 = NaturalReaderSpeech 1=MARY

if SynteseVocal == 1 :
	# MARYTTS LANGUAGE 
	lang="FR"
	Voice="upmc-pierre-hsmm" # french enst-dennys-hsmm / enst-camille-hsmm / upmc-jessica-hsmm / upmc-pierre-hsmm
elif SynteseVocal == 0 :
	lang ="FR"
	Voice="Julie"	

#Traduction
# https://datamarket.azure.com/account
Azure_client_id = "048ad8bd-a985-4a98-a514-e3a2d18cd7d2"
Azure_client_secret = "XIOpUP9qFG0qyVXqJzLZ4Ec4Do0fc6XO0bDG26c1uuw"


#liste des sorties des servos moteur
PinRegardGD = 8
PinRotationTete = 9
PinBouche = 10
