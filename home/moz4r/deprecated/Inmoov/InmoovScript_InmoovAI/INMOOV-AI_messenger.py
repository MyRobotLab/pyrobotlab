def GetUnreadMessageNumbers(SpeakReturn):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=GetUnreadMessageNumbers&bot_id="+str(chatBot.getPredicate("default","bot_id")))
	print "http://www.myai.cloud/shared_memory.php?action=GetUnreadMessageNumbers&bot_id="+str(chatBot.getPredicate("default","bot_id"))
	if RetourServer!="0":
		Light(0,1,1)
		#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\message.jpg',1)
		#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\message.jpg',1)
		chatBot.getResponse("SYSTEM "+RetourServer+ " MESSAGE")
	else:
		Light(1,1,1)
		#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
		#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
		if SpeakReturn=="1":
			chatBot.getResponse("SYSTEM "+RetourServer+ " MESSAGE")
	
def GetMessage():
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=GetMessage&bot_id="+str(chatBot.getPredicate("default","bot_id")))
	print "http://www.myai.cloud/shared_memory.php?action=GetMessage&bot_id="+str(chatBot.getPredicate("default","bot_id"))
	chatBot.getResponse("SYSTEMREADMESSAGE "+RetourServer)
	
def NewMessage(botname,bot_id,question):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=NewMessage&bot_id="+bot_id+"&botname="+urllib2.quote(botname.replace("'", " "))+"&question="+urllib2.quote(question.replace("'", " ")))
	print "http://www.myai.cloud/shared_memory.php?action=NewMessage&bot_id="+bot_id+"&botname="+urllib2.quote(botname.replace("'", " "))+"&question="+urllib2.quote(question.replace("'", " "))
	chatBot.getResponse(RetourServer)
	
def CheckRobot(botname):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=CheckRobot&botname="+urllib2.quote(botname.replace("'", " ")))
	print "http://www.myai.cloud/shared_memory.php?action=CheckRobot&botname="+urllib2.quote(botname.replace("'", " "))
	chatBot.getResponse(RetourServer)	
	
	