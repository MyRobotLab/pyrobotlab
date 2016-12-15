#! usr/bin/python 
# -*- coding: ISO-8859-1 -*- 
def connectionDomotique(db,StartByte,NbByte) :
	global client
	client = S7Client()
	IpAdress ="192.168.1.149"
	Rack = 0
	Slot = 2
	Result = client.ConnectTo(IpAdress, Rack, Slot)
	Result=client.ReadArea(S7.S7AreaDB,db,StartByte,NbByte,client.PDU)
	T_tampon_Haut = S7.GetFloatAt(client.PDU, 12)
	print str(T_tampon_Haut)

def infochauffage() :
	global client
	connectionDomotique(3,250,32)
	sleep (1)
	T_entree_generateur = S7.GetFloatAt(client.PDU, 0)
	T_depart_radiateur = S7.GetFloatAt(client.PDU, 4)
	T_exterieur = S7.GetFloatAt(client.PDU, 8)
	T_tampon_Haut = S7.GetFloatAt(client.PDU, 12)
	T_tampon_bas = S7.GetFloatAt(client.PDU, 16)
	T_depart_plancher_chauffant = S7.GetFloatAt(client.PDU, 20)
	T_consigne_radiateur = S7.GetFloatAt(client.PDU, 24)
	T_consigne_plancher_chauffant = S7.GetFloatAt(client.PDU, 28)
	Texte =(u"La température éxterieur actuelle est de " + ConvertionFloatString(T_exterieur) )
	Texte =( Texte + u" degré.")
	mouth.speakBlocking(Texte)
	Texte = (u"La réserve d'eau du chauffage est acuellement à " + ConvertionFloatString(T_tampon_Haut) )
	Texte =( Texte + u" degré.")
	mouth.speakBlocking(Texte)
	Texte = (u"La température au départ des radiateur est de " + ConvertionFloatString(T_depart_radiateur) )
	Texte =( Texte + u" degré.")
	Texte = (Texte + u" et la consigne est de " + ConvertionFloatString(T_consigne_radiateur) )
	Texte =( Texte + u" degré.")
	mouth.speakBlocking(Texte)
	Texte = (u"La température au départ du planché chauffant est de " + ConvertionFloatString(T_depart_plancher_chauffant) )
	Texte =( Texte + u" degré.")
	Texte = (Texte + u" et la consigne est de " + ConvertionFloatString(T_consigne_plancher_chauffant) )
	Texte =( Texte + u" degré.")
	mouth.speakBlocking(Texte)


def ConvertionFloatString(nombre) :
	Valeur = round(nombre,1)
	Valeur = str(Valeur)
	Valeur = Valeur.replace('-','moin ').replace('.','. virgule ')
	return Valeur

