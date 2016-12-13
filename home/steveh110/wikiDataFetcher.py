def getDate(query, ID): 
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)
	
def getIp():  
	ip = str(socket.gethostbyname(socket.gethostname()))
	ip = ip.replace('.',' point ')
	chatBot.getResponse("say Mon adresse IP est  " + ip)

def talk(data):
	if data!="":
		mouth.speak(data)
	query = unicode(query,'utf-8')
	if query[1]== "\'" : 
		query2 = query[2:len(query)]
		query = query2
	print query 
	word = wdf.cutStart(query) 
	start = wdf.grabStart(query) 
	wikiAnswer = wdf.getDescription(word) 
	answer = ( query + " est " + wikiAnswer)
	if wikiAnswer == "Not Found !":
		answer = "Je ne sais pas"
	chatBot.getResponse("say " + answer) 

def getProperty(query, what): 
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	if query[1]== "\'" :
		query2 = query[2:len(query)]
		query = query2
	if what[1]== "\'" :
		what2 = what[2:len(what)]
		what = what2
		print "what = " + what + " - what2 = " + what2
	ID = "error"
	
	f = codecs.open(u"G:/robot/WIKI_prop.txt",'r',"utf-8") 
	
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	print "query = " + query + " - what = " + what + " - ID = " + ID
	wikiAnswer= wdf.getData(query,ID) 
	answer = ( what +" de " + query + " est " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer = "Je ne sais pas"
	chatBot.getResponse("say " + answer)
	return answer
	
def askWiki(query):
	query = unicode(query,'utf-8')
	print query
	word = wdf.cutStart(query)
	start = wdf.grabStart(query)
	wikiAnswer = wdf.getDescription(word)
	answer = ( query + " est " + wikiAnswer)
	if wikiAnswer == "Description not Found":
		answer = "Je ne sais pas mon ami"
	chatBot.getResponse("say " + answer)

