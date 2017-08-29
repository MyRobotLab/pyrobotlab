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
  
  if (sensorValue1 >= 100){
      Serial.write(1);
      delay(500);
  }
  if (sensorValue2 >= 100){
      Serial.write(2);
      delay(500);
  }
  if (sensorValue3 >= 100){
      Serial.write(3);
      delay(500);
  }
  if (sensorValue4 >= 100){
      Serial.write(4);
      delay(500);
  }
  if (sensorValue5 >= 100){
      Serial.write(5);
      delay(500);
  }
  if (sensorValue6 >= 100){
      Serial.write(6);
      delay(500);
  }
  if (sensorValue7 >= 100){
      Serial.write(7);
      delay(500);
  }
  if (sensorValue8 >= 100){
      Serial.write(8);
      delay(500);
  }
  if (sensorValue9 >= 100){
      Serial.write(9);
      delay(500);
  }
  if (sensorValue10 >= 100){
      Serial.write(10);
      delay(500);
  }
  if (sensorValue11 >= 100){
      Serial.write(11);
      delay(500);
  }
  if (sensorValue12 >= 100){
      Serial.write(12);
      delay(500);
  }
  delay(20);
}
