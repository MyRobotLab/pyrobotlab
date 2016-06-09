# This is an example of staring two servo services
# and showing each servo in a separate tab in the browsee

# Start the servo services
s1 = Runtime.createAndStart("Servo1","Servo")
s2 = Runtime.createAndStart("Servo2","Servo")

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

# Start the browsers and show the first service ( Servo1 )
webgui.startBrowser("http://localhost:8888/#/service/Servo1")

# Wait a little before executing the second startBrowser to allow
# the first browser to start so that the second service will be shown
# in a new tab. Without the sleep(1) you will probably get two browsers.
sleep(1)
webgui.startBrowser("http://localhost:8888/#/service/Servo2")
