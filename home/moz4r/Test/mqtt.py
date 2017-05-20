# worky with MRL 1.0.2179

topic = "inmoov/test"
qos = 2
broker = "tcp://broker.mqttdashboard.com:1883" 

clientID = "MRLMQTTpython1"
mqtt1 = Runtime.createAndStart("Mqtt", "Mqtt")
print mqtt1.getDescription()

mqtt1.setBroker(broker)
mqtt1.setQos(qos)
mqtt1.setPubTopic(topic)
mqtt1.setClientId(clientID)
mqtt1.connect(broker)

mqtt1.subscribe("inmoov/test", 0)
mqtt1.publish("hello inmoov world")

# Quelle evenement ecouter ?
# au choix :

mqtt1.addListener("publishMqttMsg", "python", "publishMqttMsg")
mqtt1.addListener("publishMqttMsgByte", "python", "publishMqttMsgByte")
mqtt1.addListener("publishMqttMsgString", "python", "publishMqttMsgString")
	 
#  MQTT call-back
def publishMqttMsg(msg):
	print msg

def publishMqttMsgByte(msg):
	print msg

def publishMqttMsgString(msg):
	print msg
