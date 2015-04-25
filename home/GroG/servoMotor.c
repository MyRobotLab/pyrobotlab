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
  
  // PIN MAPPINGS M1 POWER PD5 == Pin 12
  analogWrite(12, 128);
   
  leds.red(HIGH);       // turn red LED on
  delay(128);
 
  leds.red(LOW);       // turn red LED off
  delay(128);
}
