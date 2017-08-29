xmppRobotName= "yourRobotName" #insert robot username on server XMPP @myrobotlab.org
xmppReceiver="yourReceiver@myrobotlab.org" #insert your username of receiver and sender on server XMPP @myrobotlab.org
xmppPwd = "passwordRobot" #inser password of robot account

xmpp = Runtime.createAndStart("xmpp","Xmpp") #start service XMPP
xmpp.connect("myrobotlab.org", 5222, xmppRobotName, xmppPwd) #connect to server @myrobotlab.org
xmpp.setStatus(True, "online all the time") #Online when is execute this script
xmpp.addAuditor(xmppReceiver) #add receiver and sender account

htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter") #start service HtmlFilter

alice2 = Runtime.createAndStart("alice2", "ProgramAB") #start ProgramAB serivce
alice2.startSession("default", "alice2") #start with name and robot intelligence 
alice2.addTextListener(htmlfilter) #add listerner of text 

python.subscribe("xmpp","publishXMPPMsg") #public on Python service function when robot receive message
python.subscribe('htmlfilter', 'publishText') #public on Python service function when ProgramAB answers  

def onXMPPMsg(xmppmsg): 
   print xmppmsg.msg.getBody() #print text of message receive
   alice2.getResponse(xmppmsg.msg.getBody()) #send message to ProgramAB
   
def onText(text):
   xmpp.sendMessage(text, xmppReceiver) #send message to receiver account 
