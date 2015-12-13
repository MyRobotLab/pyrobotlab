
// These constants won't change.  They're used to give names
// to the pins used: 
const int analogInPin1 = A0;  // Analog input pin that the potentiometer is attached to
const int analogInPin2 = A1;  // Analog input pin that the potentiometer is attached to
const int analogInPin3 = A2;  // Analog input pin that the potentiometer is attached to
const int analogInPin4 = A3;  // Analog input pin that the potentiometer is attached to
const int analogInPin5 = A4;  // Analog input pin that the potentiometer is attached to
const int analogInPin6 = A5;  // Analog input pin that the potentiometer is attached to
const int analogInPin7 = A6;  // Analog input pin that the potentiometer is attached to
const int analogInPin8 = A7;  // Analog input pin that the potentiometer is attached to
const int analogInPin9 = A8;  // Analog input pin that the potentiometer is attached to
const int analogInPin10 = A9;  // Analog input pin that the potentiometer is attached to
const int analogInPin11 = A10;  // Analog input pin that the potentiometer is attached to
const int analogInPin12 = A11;  // Analog input pin that the potentiometer is attached to

int startValue1 = 0;        // value read from the pot
int startValue2 = 0;        // value read from the pot
int startValue3 = 0;        // value read from the pot
int startValue4 = 0;        // value read from the pot
int startValue5 = 0;        // value read from the pot
int startValue6 = 0;        // value read from the pot
int startValue7 = 0;        // value read from the pot
int startValue8 = 0;        // value read from the pot
int startValue9 = 0;        // value read from the pot
int startValue10 = 0;        // value read from the pot
int startValue11 = 0;        // value read from the pot
int startValue12 = 0;        // value read from the pot

int sensorValue1 = 0;        // value read from the pot
int sensorValue2 = 0;        // value read from the pot
int sensorValue3 = 0;        // value read from the pot
int sensorValue4 = 0;        // value read from the pot
int sensorValue5 = 0;        // value read from the pot
int sensorValue6 = 0;        // value read from the pot
int sensorValue7 = 0;        // value read from the pot
int sensorValue8 = 0;        // value read from the pot
int sensorValue9 = 0;        // value read from the pot
int sensorValue10 = 0;        // value read from the pot
int sensorValue11 = 0;        // value read from the pot
int sensorValue12 = 0;        // value read from the pot

void setup() {
  // initialize serial communications at 57600 bps:
  Serial.begin(57600);

  delay(1000);

  startValue1 = analogRead(analogInPin1);
  startValue2 = analogRead(analogInPin2);
  startValue3 = analogRead(analogInPin3);
  startValue4 = analogRead(analogInPin4);
  startValue5 = analogRead(analogInPin5);
  startValue6 = analogRead(analogInPin6);
  startValue7 = analogRead(analogInPin7);
  startValue8 = analogRead(analogInPin8);
  startValue9 = analogRead(analogInPin9);
  startValue10 = analogRead(analogInPin10);
  startValue11 = analogRead(analogInPin11);
  startValue12 = analogRead(analogInPin12);

  delay(1000);
}

void loop() {
  // read the analog in value:
  sensorValue1 = analogRead(analogInPin1);
  sensorValue2 = analogRead(analogInPin2);
  sensorValue3 = analogRead(analogInPin3);
  sensorValue4 = analogRead(analogInPin4);
  sensorValue5 = analogRead(analogInPin5);
  sensorValue6 = analogRead(analogInPin6);
  sensorValue7 = analogRead(analogInPin7);
  sensorValue8 = analogRead(analogInPin8);
  sensorValue9 = analogRead(analogInPin9);
  sensorValue10 = analogRead(analogInPin10);
  sensorValue11 = analogRead(analogInPin11);
  sensorValue12 = analogRead(analogInPin12);
  
  if (sensorValue1 <= startValue1 - 100){
      Serial.write(1);
      delay(200);
  }
  if (sensorValue2 <= startValue2 - 100){
      Serial.write(2);
      delay(200);
  }
  if (sensorValue3 <= startValue3 - 100){
      Serial.write(3);
      delay(200);
  }
  if (sensorValue4 <= startValue4 - 100){
      Serial.write(4);
      delay(200);
  }
  if (sensorValue5 <= startValue5 - 100){
      Serial.write(5);
      delay(200);
  }
  if (sensorValue6 <= startValue6 - 100){
      Serial.write(6);
      delay(200);
  }
  if (sensorValue7 <= startValue7 - 100){
      Serial.write(7);
      delay(200);
  }
  if (sensorValue8 <= startValue8 - 100){
      Serial.write(8);
      delay(200);
  }
  if (sensorValue9 <= startValue9 - 100){
      Serial.write(9);
      delay(200);
  }
  if (sensorValue10 <= startValue10 - 100){
      Serial.write(10);
      delay(200);
  }
  if (sensorValue11 <= startValue11 - 100){
      Serial.write(11);
      delay(200);
  }
  if (sensorValue12 <= startValue12 - 100){
      Serial.write(12);
      delay(200);
  }
//  Serial.println(sensorValue1);
  delay(20);
}
