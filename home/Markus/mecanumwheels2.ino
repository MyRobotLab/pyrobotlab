
const int leftrearPin = 3;    // leftrear motor connected to digital pin 3
const int leftfrontPin = 5;    // leftfront motor connected to digital pin 5
const int rightrearPin = 9;    // rightrear motor connected to digital pin 9
const int rightfrontPin = 10;    // rightfront motor  connected to digital pin 10

int sensorPin0 = A1;    // select the input pin for the  potentiometer
int sensorPin1 = A0;    // select the input pin for the potentiometer
int sensor0Value = 0;  // variable to store the value coming from the sensor
int sensor1Value = 0;  // variable to store the value coming from the sensor


int Stop = 127;

int leftfront = Stop;
int rightfront = Stop;
int leftrear = Stop;
int rightrear = Stop;

const int mandrivePin = 2;     // the number of the pushbutton pin
int mandriveState = 0;         // variable for reading the pushbutton status
int mandrive = 0;  

void setup() {

    Serial.begin(115200);
    
    analogWrite(leftfrontPin,  leftfront);
    analogWrite(rightfrontPin, rightfront);
    analogWrite(leftrearPin,  leftrear);
    analogWrite(rightrearPin, rightrear);   

    pinMode(mandrivePin, INPUT);
}

void loop() {
    mandriveState = digitalRead(mandrivePin);

    
    delay(20);
    if (mandriveState == LOW) { 
      if (mandrive == 0) {
        mandrive = 1; 
      }
      else if (mandrive == 1) {
        mandrive = 2; 
      }
      else if (mandrive == 2) {
        mandrive = 0; 
      }
      delay(500);
      }
    
       

    if (mandrive == 0) {
      
      // if there's any serial available, read it:
      while (Serial.available() > 0) {

        // look for the next valid integer in the incoming serial stream:
        int red = Serial.parseInt();
        // do it again:
        int green = Serial.parseInt();
        // do it again:
        int blue = Serial.parseInt();

        // look for the newline. That's the end of your
        // sentence:
        if (Serial.read() == '\n') {
          // constrain the values to 0 - 255 and invert
          // if you're using a common-cathode LED, just use "constrain(color, 0, 255);"
          red = 255 - constrain(red, 0, 255);
          green = 255 - constrain(green, 0, 255);
          blue = 255 - constrain(blue, 0, 255);

          red = map(red, 0, 255, -70, 325);
          green = map(green, 0, 255, -70, 325);
          blue = map(blue, 0, 255, -70, 325);
        
          leftfront = (green + blue + (255 - red) ) / 3 ;
          rightfront = (green + (255 - blue) + red ) / 3 ;
          leftrear = (green + blue + red) / 3 ;
          rightrear = (green + (255 - blue) + (255 - red) ) / 3 ;  


      
          // fade the red, green, and blue legs of the LED:
          analogWrite(leftrearPin, - leftrear);
          analogWrite(rightrearPin, - rightrear);
          analogWrite(leftfrontPin, - leftfront);
          analogWrite(rightfrontPin, - rightfront);
        }
      }
    }

                  
    else if (mandrive == 1) {
      sensor0Value = analogRead(sensorPin0);
      sensor0Value = map(sensor0Value, 0, 1023, 300, -60);
      sensor1Value = analogRead(sensorPin1);
      sensor1Value = map(sensor1Value, 0, 1023, 250, 0);
    
      leftfront = (sensor0Value + sensor1Value) / 2 ;
      if (leftfront >= 200) {
        leftfront = 200;
      }
      if (leftfront <= 30) {
        leftfront = 30;
      }
      rightfront = ((sensor0Value + 127) / 2) + (127 - sensor1Value) / 2 ;
      if (rightfront >= 200) {
        rightfront = 200;
      }
      if (rightfront <= 30) {
        rightfront = 30;
      }
      leftrear = (sensor0Value + sensor1Value) / 2 ;
      if (leftrear >= 200) {
        leftrear = 200;
      }
      if (leftrear <= 30) {
        leftrear = 30;
      }
      rightrear = ((sensor0Value + 127) / 2) + (127 - sensor1Value) / 2 ;  
      if (rightrear >= 200) {
        rightrear = 200;
      }
      if (rightrear <= 30) {
        rightrear = 30;
      }
    
      analogWrite(leftrearPin, - leftrear);
      analogWrite(rightrearPin, - rightrear);
      analogWrite(leftfrontPin, - leftfront);
      analogWrite(rightfrontPin, - rightfront);

      }

    else if (mandrive == 2) {
      sensor0Value = analogRead(sensorPin0);
      sensor0Value = map(sensor0Value, 0, 1023, 250, 0);
      sensor1Value = analogRead(sensorPin1);
      sensor1Value = map(sensor1Value, 0, 1023, 250, 0);
    
      leftfront = (sensor0Value + sensor1Value) / 2 ;
      if (leftfront >= 200) {
        leftfront = 200;
      }
      if (leftfront <= 50) {
        leftfront = 50;
      }
      rightfront = ((sensor0Value + 127) / 2) + (127 - sensor1Value) / 2 ;
      if (rightfront >= 200) {
        rightfront = 200;
      }
      if (rightfront <= 50) {
        rightfront = 50;
      }
      leftrear = ((sensor0Value + 127) / 2) + (127 - sensor1Value) / 2 ;
      if (leftrear >= 200) {
        leftrear = 200;
      }
      if (leftrear <= 50) {
        leftrear = 50;
      }
      rightrear = (sensor0Value + sensor1Value) / 2 ;
      if (rightrear >= 200) {
        rightrear = 200;
      }
      if (rightrear <= 50) {
        rightrear = 50;
      }
    
      analogWrite(leftrearPin, - leftrear);
      analogWrite(rightrearPin, - rightrear);
      analogWrite(leftfrontPin, - leftfront);
      analogWrite(rightfrontPin, - rightfront);

      }
      
 //   Serial.println(leftfront);
 //   Serial.println(rightfront);
 //   Serial.println(leftrear);
//    Serial.println(rightrear);
//    delay(100);
  }
    
