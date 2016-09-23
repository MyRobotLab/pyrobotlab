def loto(phrase,the,chance,fin):
	table1 = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
	tablefin = []
	doublon = []

	for i in table1:
		if i not in tablefin:
			tablefin.append(i) #supprime les doublons
		else:
			doublon.append(i) #extraire les doublons
			d = len(doublon)
			while d > 0:
			#nouveau tirage
				doublon = []
				table1 = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
				# recherche doublon
				for i in table1:
					if i not in tablefin:
						tablefin.append(i) #supprime les doublons
					else:
						doublon.append(i) #extraire les doublons
					# si il existe doublon d+1 et vite la table
					if (len(doublon)==1)or(len(doublon)==2)or(len(doublon)==3)or(len(doublon)==4)or(len(doublon)==5):
						talkBlocking("j ai trouver un doublon , je refais un tirage")
						d = d+1
						doublon =[]
					else:
						d = 0
		break
	# tri la table avant de la dire
	table1.sort()
	talkBlocking(phrase)
	talkBlocking(the+str(table1[0]))
	talkBlocking(the+str(table1[1]))
	talkBlocking(the+str(table1[2]))
	talkBlocking(the+str(table1[3]))
	talkBlocking(the+str(table1[4]))
	talkBlocking(chance+str(random.randint(1,9)))
	talkBlocking(fin)