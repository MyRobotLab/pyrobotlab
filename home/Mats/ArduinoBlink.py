# Start the Arduino service on port COM11
Arduino = Runtime.createAndStart("Arduino","Arduino")
Arduino.connect("COM11")
# Blink the led at PIN 13 two times
Arduino.pinMode(13,"OUTPUT")
Arduino.digitalWrite(13,1)
sleep(1)
Arduino.digitalWrite(13,0)
sleep(1)
Arduino.digitalWrite(13,1)
sleep(1)
Arduino.digitalWrite(13,0)
