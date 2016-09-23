#Shared Knowledge save to the cloud
def SaveMemory(question,reponse,silent,justPredicates):
	sleep(0.5)
	chatBot.savePredicates()
	if justPredicates==0:
		ServerResponse="0"
		RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " ")))
		print "http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " "))
		if silent<>1:
			chatBot.getResponse("SAVEMEMORY")

#Shared Knowledge save to local programab config file		
def SaveMemoryPersonal(question,ReturnSubject,record):
	if str(record)=="0":
		valueQuestion=chatBot.getPredicate("default",question).decode( "utf8" )
		if valueQuestion=="unknown":
			chatBot.getResponse("SaveMemoryPersonal "+unicode(ReturnSubject,'utf-8')+" "+unicode(question,'utf-8'))
		else:
			chatBot.getResponse(unicode(ReturnSubject,'utf-8') + " " + unicode(question,'utf-8') + " LECTURENOM " + " " + unicode(valueQuestion,'utf-8'))
	else:
		chatBot.setPredicate("default",question,record)
		chatBot.savePredicates()
		
def ClearMemory():
	chatBot.setPredicate("default","topic","default")
	chatBot.setPredicate("default","QUESTION_WhoOrWhat","")
	chatBot.setPredicate("default","QUESTION_sujet","")
	chatBot.setPredicate("default","QUESTION_action","")

	
		
def QueryMemory(question,retourNok,retourOk):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=select&question="+urllib2.quote(question))
	
	if RetourServer!="" and RetourServer!="0":
		chatBot.getResponse(retourOk + " " + RetourServer)
	else:
		chatBot.getResponse(retourNok)