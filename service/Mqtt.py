topic = "myrobotlab/test"
qos = 2
broker = "tcp://broker.mqttdashboard.com:1883" 

clientID = "MRLMQTTpython1"
mqtt = Runtime.createAndStart("mqtt", "Mqtt")
print mqtt.getDescription()

mqtt.setBroker(broker)
mqtt.setQos(qos)
mqtt.setPubTopic(topic)
mqtt.setClientId(clientID)
mqtt.connect(broker)
# authentification mqtt.connect(broker,"guest","guest")

mqtt.subscribe("myrobotlab/test", 0)
mqtt.publish("hello myrobotlab world")

mqtt.addListener("publishMqttMsgString", "python", "publishMqttMsgString")
	 
#  MQTT call-back

def publishMqttMsgString(msg):
	print "message : ",msg[0]
print "topic : ",msg[1]
