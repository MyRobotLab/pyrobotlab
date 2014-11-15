from time import sleep

topic = "mrl"
qos = 2
broker = "tcp://iot.eclipse.org:1883" //if you have your own just change the hostname/IP
clientID = "MRL MQTT python"

mqtt1 = Runtime.createAndStart("mqtt", "MQTT")
mqtt1.startService()
print mqtt1.getDescription()
mqtt1.startClient(topic, qos, broker, clientID)

sleep(1)

mqtt1.publish("Greetings from MRL python");
