# This is an example of staring two servo services
# and showing each servo in a separate browser

# Start the servo services
s1 = Runtime.createAndStart("Servo1","Servo")
s2 = Runtime.createAndStart("Servo2","Servo")

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

# Start two browsers and show one service in each
webgui.startBrowser("http://localhost:8888/#service/Servo1")
webgui.startBrowser("http://localhost:8888/#service/Servo2")
