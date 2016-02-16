# simple script to show how to send a message to and recieve a message from
# using a robot with the XMPP service 

# create an xmpp service
xmpp = Runtime.createAndStart("xmpp","Xmpp")

# adds the python service as a listener for messages
# xmpp.addListener("python","publishMessage")
python.subscribe("xmpp","publishMessage")

# there is a big list of different xmpp/jabber servers out there
# but we will connect to the big one - since that is where our robots account is
xmpp.connect("myrobotlab.org", 5222, "GroG.robot01", "xxxxxxxx")

# gets list of all the robots friends
print xmpp.getRoster()

# set your online status
xmpp.setStatus(True, "online all the time")

# add auditors you want this robot to chat with
# auditors can issue commands and will be notified of 
# commands being sent by others and what those commands return
xmpp.addAuditor("GroG")
# xmpp.addAuditor("Jane Smith")

# send a message
xmpp.sendMessage("hello this is robot01 - the current heatbed temperature is 40 degrees celcius", "GroG@myrobotlab.org")

def onMessage(msg):
	print msg.getFrom(), " says " , msg.getBody()
