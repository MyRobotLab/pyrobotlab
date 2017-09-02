# -*- coding: utf-8 -*- 

def anniversaire(SpeakReturn):
	maintenant = datetime.now()
	#petite vavriable pour faire un retour en cas de non anniversaire
	NoBirthDay=1
	#On ouvre notre liste perso
	cr = csv.reader(open(oridir+"BDD/birthday.csv","rb"))
	for row in cr:
		#On converti au format date la premiere valeure pour faire des calculs car elle est en texte
		DateSelect=datetime.strptime(row[0], '%d/%m/%Y')
		#On filtre uniquement le mois et le jour
		KeyFounded=str(DateSelect.strftime('%d/%m'))
		#on calcul la différence de jour ( au prochain anniversaire )
		FakeDate=(datetime.strptime(KeyFounded+"/"+str(maintenant.year), '%d/%m/%Y')-maintenant).days+1
		#print datetime.strptime(KeyFounded+"/"+str(maintenant.year), '%d/%m/%Y')-maintenant
		if FakeDate<=7 and FakeDate>=0:
			age = (maintenant.year - DateSelect.year)
			NoBirthDay=0
		#On envoi le retour a l'aiml ( pour internationalisation : nom SYSTEM jours_restants BIRTHDAY OK age )
			chatBot.getResponse(str(row[1]) + " SYSTEM " + str(FakeDate) + " BIRTHDAY OK " + str(age))
			sleep(4)
	if SpeakReturn!="0" and NoBirthDay==1:
		chatBot.getResponse("SYSTEM BIRTHDAY NOK")