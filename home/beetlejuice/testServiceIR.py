runtime.createAndStart("infraRouge", "IRremote")
infraRouge.arduino.setBoard("atmega328")
infraRouge.attach("COM4", 2, 3)
infraRouge.RSsend("C2")
