
const int pwrPin = 6;      // the pin that the motor's power is attached to

void setup()
{
  // initialize the serial communication:
  Serial.begin(9600);
  // initialize the pwrPin as an output:
  pinMode(pwrPin, OUTPUT);
}

void loop() {
  byte power;

  // check if data has been sent from the computer:
  if (Serial.available()) {
    // read the most recent byte (which will be from 0 to 255):
    power = Serial.read();
    // set the power of the LED:
    analogWrite(pwrPin, power);
  }
}
