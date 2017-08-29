
int leftrearPin = 3;    // leftrear motor connected to digital pin 3
int leftfrontPin = 5;    // leftfront motor connected to digital pin 5
int rightrearPin = 9;    // rightrear motor connected to digital pin 9
int rightfrontPin = 10;    // rightfront motor  connected to digital pin 10
int sensorPin0 = A0;    // select the input pin for the  potentiometer
int sensorPin1 = A1;    // select the input pin for the potentiometer
int sensorPin2 = A2;    // select the input pin for the potentiometer
int sensor0Value = 0;  // variable to store the value coming from the sensor
int sensor1Value = 0;  // variable to store the value coming from the sensor
int sensor2Value = 0;  // variable to store the value coming from the sensor
int leftfront = 0;
int rightfront = 0;
int leftrear = 0;
int rightrear = 0;

void setup() {
    pinMode(2, OUTPUT);    //determine the direction for the leftrear motor
    pinMode(4, OUTPUT);    //determine the direction for the leftfront motor
    pinMode(8, OUTPUT);    //determine the direction for the rightrear motor
    pinMode(12, OUTPUT);    //determine the direction for the rightfront motor

    Serial.begin(9600);
}

void loop() {
    sensor0Value = analogRead(sensorPin0);
    sensor0Value = map(sensor0Value, 0, 1023, 250, -250);
    sensor1Value = analogRead(sensorPin1);
    sensor1Value = map(sensor1Value, 0, 1023, -250, 250);
    sensor2Value = analogRead(sensorPin2);
    sensor2Value = map(sensor2Value, 0, 1023, 250, -250);
    
    leftfront = sensor0Value - sensor1Value + sensor2Value ;
    if (leftfront >= 250) {
      leftfront = 250;
    }
    if (leftfront <= -250) {
      leftfront = -250;
    }
    rightfront = sensor0Value + sensor1Value - sensor2Value ;
    if (rightfront >= 250) {
      rightfront = 250;
    }
    if (rightfront <= -250) {
      rightfront = -250;
    }
    leftrear = sensor0Value + sensor1Value + sensor2Value ;
    if (leftrear >= 250) {
      leftrear = 250;
    }
    if (leftrear <= -250) {
      leftrear = -250;
    }
    rightrear = sensor0Value - sensor1Value - sensor2Value ;  
    if (rightrear >= 250) {
      rightrear = 250;
    }
    if (rightrear <= -250) {
      rightrear = -250;
    }
    if (leftrear <= -20) {
      digitalWrite(2, HIGH);
      analogWrite(leftrearPin, - leftrear);
    } else if (leftrear >= 10) {
        digitalWrite(2, LOW);
        analogWrite(leftrearPin, leftrear); 
      }  else if (leftrear <= 10) {
             analogWrite(leftrearPin, 0); 
}
    if (rightrear <= -20) {
      digitalWrite(8, HIGH);
      analogWrite(rightrearPin, - rightrear);
    } else if (rightrear >= 10) {
        digitalWrite(8, LOW);
        analogWrite(rightrearPin, rightrear); 
      }  else if (rightrear <= 10) {
             analogWrite(rightrearPin, 0); 
}
    if (leftfront <= -20) {
      digitalWrite(4, HIGH);
      analogWrite(leftfrontPin, - leftfront);
    } else if (leftfront >= 10) {
        digitalWrite(4, LOW);
        analogWrite(leftfrontPin, leftfront); 
      }  else if (leftfront <= 10) {
             analogWrite(leftfrontPin, 0); 
}
    if (rightfront <= -20) {
      digitalWrite(12, HIGH);
      analogWrite(rightfrontPin, - rightfront);
    } else if (rightfront >= 10) {
        digitalWrite(12, LOW);
        analogWrite(rightfrontPin, rightfront); 
      }  else if (rightfront <= 10) {
             analogWrite(rightfrontPin, 0); 
}
    delay(200);
    Serial.println(rightrear);
}
