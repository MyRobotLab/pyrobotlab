
#include <Servo.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

/* This driver uses the Adafruit unified sensor library (Adafruit_Sensor),
which provides a common 'type' for sensor data and some helper functions.

To use this driver you will also need to download the Adafruit_Sensor
library and include it in your libraries folder.

You should also assign a unique ID to this sensor for use with
the Adafruit Sensor API so that you can identify this particular
sensor in any data logs, etc.  To assign a unique ID, simply
provide an appropriate value in the constructor below (12345
is used by default in this example).

Connections
===========
Connect SCL to analog 5
Connect SDA to analog 4
Connect VDD to 3-5V DC
Connect GROUND to common ground

History
=======
2015/MAR/03  - First release (KTOWN)
2015/AUG/27  - Added calibration and system status helpers
*/

#define PIN_COMMAND (8)
int pitchServoPin = 9;
int rollServoPin = 10;
int FeedbackPin = 13; /* interne gelbe LED */

Servo rollServo;  // create servo object to control turning movement
Servo pitchServo;  // create servo object to control bending movement

int CommandMode;
int ModeBefore;

int rollValue = 1500;    // variable to store the servo position
int rollMin = 600;
int rollMax = 2400;
int rollRead;           // normalized roll value
int rollKorr = 5;

int pitchValue = 1500;    // variable to store the target servo position
int pitchMin = 600;
int pitchMax = 2400;
int pitchRead;          // calibrated pitch value
int pitchKorr = -1;

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (20)

Adafruit_BNO055 bno = Adafruit_BNO055(55);


/**************************************************************************/
/*
Arduino setup function (automatically called at startup)
*/
/**************************************************************************/
void setup(void)
{

	Serial.begin(9600);
	Serial.println("Orientation Sensor Test"); Serial.println("");

	/* Initialise the sensor */
	if (!bno.begin())
	{
		/* There was a problem detecting the BNO055 ... check your connections */
		Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
		while (1);
	}

	delay(1000);

	bno.setExtCrystalUse(true);

  pinMode(PIN_COMMAND, INPUT_PULLUP); // the self-control is activated with pin in high state (1)
  ModeBefore = LOW;
}

/**************************************************************************/
/*
Arduino loop function, called once 'setup' is complete (your own code
should go here)
*/
/**************************************************************************/
void loop(void)
{
	
	sensors_event_t event;
  int rollCorrFactor;
  int pitchCorrFactor;  
  
  /* Check for activated Command pin */
  CommandMode = digitalRead(PIN_COMMAND);

  if (CommandMode == HIGH) {

    if (ModeBefore == LOW) {
        rollServo.attach(rollServoPin);  // attaches the servo on pin 10 to the servo object
        pitchServo.attach(pitchServoPin);  // attaches the servo on pin  9 to the servo object
        ModeBefore = HIGH;
        digitalWrite(FeedbackPin, HIGH);
    }

  	/* Get a new sensor event */
  	bno.getEvent(&event);

  
    /* use pitch value to change servo command
    -----------------------------------------*/
    pitchRead = event.orientation.y + pitchKorr;
    
    if (abs(pitchRead) > 10) {
      pitchValue = pitchValue + (pitchRead * 5);
    } else {
      pitchValue = pitchValue + (pitchRead * 3);
    }
    
    /* limit to min value */    
    if (pitchValue > pitchMax) pitchValue = pitchMax;
    if (pitchValue < pitchMin) pitchValue = pitchMin;
 
    
    pitchServo.writeMicroseconds(pitchValue);
  
    Serial.print("\tPitch: ");
    Serial.print(event.orientation.y);
    Serial.print("\t pitchServo target: ");
    Serial.print(pitchValue);
  
  
    /* as the sensor is below the hand the goal is to get 180 degree roll 
    normalize the value
    */
    if (event.orientation.z < 0) rollRead = 360 + event.orientation.z + rollKorr;
    if (event.orientation.z >= 0) rollRead = event.orientation.z + rollKorr;
    Serial.print("\trollRead: "); Serial.print(rollRead);
  
      
    rollValue = rollValue - ((rollRead - 180) * 5);
    
    /* do not cross the limits */
    if (rollValue > rollMax) rollValue = rollMax;
    if (rollValue < rollMin) rollValue = rollMin;
   
  
    Serial.print("\t rollServo target: ");
    Serial.print(rollValue);
    rollServo.writeMicroseconds(rollValue);
  
 
    /* New line for the next sample */
    Serial.println("");
    
  } else {
      if (ModeBefore == HIGH) {
        rollServo.detach();  // detaches the servo on pin 10 to the servo object
        pitchServo.detach();  // detaches the servo on pin  9 to the servo object
        ModeBefore = LOW;
        digitalWrite(FeedbackPin, LOW);
    }
  }

  /* Wait the specified delay before requesting nex data */
  delay(BNO055_SAMPLERATE_DELAY_MS);

}
