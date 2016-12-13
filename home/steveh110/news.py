

def parser(lien,nb) :

    	if lien == 1: 
    		lien = "http://www.lesbonsnumeros.com/euromillions/rss.xml"
	elif lien == 2:
		lien = "http://www.20min.ch/rss/rss.tmpl?type=rubrik&get=784&lang=ro"
	elif lien == 3:
		lien = "http://www.20min.ch/rss/rss.tmpl?type=rubrik&get=313&lang=ro"
	elif lien == 4:
		lien = "http://www.20min.ch/rss/rss.tmpl?type=rubrik&get=526&lang=ro"
	else :
		lien = "http://www.20min.ch/rss/rss.tmpl?type=rubrik&get=784&lang=ro"	
  

	d = feedparser.parse(lien)
	i = 0
	if nb == "de" :
		nb = 2
		
	if nb <= len(d['entries']) and nb != 0 :
		nb = nb
	else :
		nb = len(d['entries'])
	

	while i < nb :
		texte = d['entries'][i]['title'] + ". " + d['entries'][i]['description'] 
		texte = re.sub('<[A-Za-z\/][^>]*>', '', texte)
		for x in texte.split("\n"):
			print x;
			mouth.speakBlocking(x)
		i += 1 