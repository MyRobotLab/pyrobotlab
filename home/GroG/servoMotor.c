#include <OrangutanLEDs.h>
#include <OrangutanAnalog.h>
#include <OrangutanMotors.h>
 
 
/*
 * OrangutanMotorExample for the 3pi robot, Orangutan LV-168, Orangutan SV-xx8,
 *   and Baby Orangutan B
 *
 * This example uses the OrangutanMotors library to drive
 * motors in response to the position of user trimmer potentiometer
 * and blinks the red user LED at a rate determined by the trimmer
 * potentiometer position.  It uses the OrangutanAnalog library to measure
 * the trimpot position, and it uses the OrangutanLEDs library to provide
 * limited feedback with the red user LED.
 *
 * http://www.pololu.com/docs/0J17/5.e
 * http://www.pololu.com
 * http://forum.pololu.com
 */
 
OrangutanAnalog analog;
OrangutanLEDs leds;
OrangutanMotors motors;
 
void setup()               // run once, when the sketch starts
{
 
}
 
void loop()                // run over and over again
{
  //                  M1   M2
  //motors.setSpeeds(128, 128);
  
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
  pinMode(16, OUTPUT);

  // PIN MAPPINGS M1 POWER PD5 == Pin 12
  analogWrite(1, 128);
  digitalWrite(1, 0);
  delay(1000);
  analogWrite(2, 128);
  digitalWrite(2, 0);
  delay(1000);
  analogWrite(3, 128);
  digitalWrite(3, 0);
  delay(1000);
  analogWrite(4, 128);
  digitalWrite(4, 0);
  delay(1000);
  analogWrite(5, 128);
  digitalWrite(5, 0);
  delay(1000);
  analogWrite(6, 128);
  digitalWrite(6, 0);
  delay(1000);
  analogWrite(7, 128);
  digitalWrite(7, 0);
  delay(1000);
  analogWrite(8, 128);
  digitalWrite(8, 0);
  delay(1000);
  analogWrite(9, 128);
  digitalWrite(9, 0);
  delay(1000);
  analogWrite(10, 128);
  digitalWrite(10, 0);
  delay(1000);
  analogWrite(11, 128);
  digitalWrite(11, 0);
  delay(1000);
  analogWrite(12, 128);
  digitalWrite(12, 0);
  delay(1000);
  analogWrite(13, 128);
  digitalWrite(13, 0);
  delay(1000);
  analogWrite(14, 128);
  digitalWrite(14, 0);
  delay(1000);
  analogWrite(15, 128);
  digitalWrite(15, 0);
  delay(1000);
  analogWrite(16, 128);
  digitalWrite(16, 0);
  delay(1000);
   
  leds.red(HIGH);       // turn red LED on
  delay(128);
 
  leds.red(LOW);       // turn red LED off
  delay(128);
}
