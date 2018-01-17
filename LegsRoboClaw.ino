/*  modified for mega and roboclaw   
 *  roboclaw right leg 2X15A firmware 4.1.23 hardware V5D Oct 1
 *  roboclaw  left leg 2X15A firmware 4.1.23 hardware V5D  Oct 6
 *  roboclaw  hips (older 2X15A firmware 4.1.23 hardware V5D  Nov 7
 *  trying to use position command on roboclaw instead of distance Jan 5
 */

#include <Arduino.h>
#include <stdio.h>
#include <Servo.h>            // used for toes and rotation of ankles
#include <Wire.h>             // needed for compass
#include <SPI.h>
#include "RoboClaw.h"

Servo ToeServoR;            // create servo object for toe right
Servo ToeServoL;            // create servo object for toe left
Servo AnkleServoR;          // create servo object for ankle right
Servo AnkleServoL;          // create servo object for ankle left

String sBuffer = "";        // string to hold asci string
String inString = "";       // string to hold numbers
char c;                     // used in input key many places
char str[64];
String verDate = "Jan 16,2018 morning";

int LeftKneeCnt = 0;          // current positon of various joints
int LeftAnkleCnt = 0;
int LeftHipCnt = 0;
int LeftHipSw = 0;
int LeftKneeSw = 0;
int LeftAnkleSw = 0;
int LeftToe = 100;        // servo starting position of toe    
int LeftKneeSpd = 0;
int LeftAnkleSpd = 0;
int LeftHipSpd = 0;
int LeftAnkleRot = 95;    // starting position should be level with floor
int RightKneeCnt = 0;
int RightAnkleCnt = 0;
int RightHipCnt = 0;
int RightHipSw = 0;
int RightKneeSw = 0;
int RightAnkleSw = 0;
int RightToe = 100;        // servo starting position of toe
int RightKneeSpd = 0;
int RightAnkleSpd = 0;
int RighHipSpd = 0;
int RightAnkleRot = 90;   // starting position should be level with floor

int LeftRoll;
int LeftPitch;
int LeftYaw;
int RightRoll;
int RightPitch;
int RightYaw;

int i = 0;  
int LedCnt = 0;       // heart beat on mega board
int swleg = 0;
int address = 0x80;   // this could be 80, 81, 82 for roboclaw boards
int AnalogPins[8] = {0,1,2,3,4,5,6,7};   // analog pins 4 limit switches and 4 photo sensors
int agDist[8];          // storage area for above values        
int NumIn = 0;          // keypad number integer number input
int aval;               // analog value used many places
int SignString = 0;
bool AnySpeed;

const byte redLEDpin = 13;     // Pin heart beat
const int HipRight = 9;        // limit switch for hip
const int HipLeft = 8;

// used for special delay
unsigned long interval = 5000;     // the time we need to wait
unsigned long previousMillis = 0;  // millis() returns an unsigned long.
unsigned long currentMillis = 0;

// Serial1 pins 19(RX) 18(TX), Serial2 pins 17(RX) 16(TX), Serial3 pins 15(RX) 14(TX) 
  RoboClaw roboclawR(&Serial1,10000);   // was 10000

int OutputPinCount = 5;     // number of channels in use
const int MaOutputPins [] = 
{
  5,  // right toe servo
  4,  // left toe servo
  6,  // left ankle servo
  7,  // right ankle servo  
  13, // heart beat led
};

void setup() {
//Open Serial terminal and roboclaws at 38400bps
  Serial.begin( 57600 );          // terminal
//  roboclawR.begin( 9600 );        // both legs and hips lowered baud rate jan 10
//  roboclawR.begin( 19200 );     // both legs and hips lowered baud rate jan 8
  roboclawR.begin( 38400 );     // both legs and hips
  Serial.println( " " );
  Serial.print( "Leg Control " ); 
  Serial.println( verDate );
  Serial2.begin( 38400 );        // gyro left foot
  Serial3.begin( 38400 );        // gyro right foot
  
  for (int i = 0; i < OutputPinCount; i++)
  {
    pinMode( MaOutputPins [i], OUTPUT );     // set to output mode
    digitalWrite (MaOutputPins [i], LOW);  // set chip enable off
  }
  pinMode( 8, INPUT );       // limit switch hip right
  pinMode( 9, INPUT );       // limit switch hip left
  pinMode( 10, INPUT );
  pinMode( 11, INPUT );
  pinMode( 12, INPUT );
  digitalWrite( 13, LOW);   // led off
 
// servo setup pins for toes and rotation of ankles
  ToeServoR.attach(MaOutputPins [0]); 
  ToeServoL.attach(MaOutputPins [1]); 
  AnkleServoL.attach(MaOutputPins [2]); 
  AnkleServoR.attach(MaOutputPins [3]); 
  
/*  looking at QPPS again on Nov 10 spent most of day
 *  values from auto tuning in ion studio are being used
 *  SO NOT SETTING LISTED HERE!
 *   
 * Knee Actobotics 142rpm 12 volt motor, max current 4.9a
 * 142rpm * 84 gear ratio  * 12 counts/rev and divide by 60sec = 2385 for QPPS
 * Ankle Actobotics 116rpm 12 volt motor, max current 4.9a
 * 116rpm * 103 gear ratio  * 12 counts/rev and divide by 60sec = 2390 for QPPS 
 * Hip Actobotics 52rpm 12 volt motor, max current 4.9a
 * 52rpm * 231 gear ratio  * 12 counts/rev and divide by 60sec = 2400 for QPPS
 *hip left M1 Vp16046, Vi 3275, Vd 0, QPPS 2110
 *hipright M2 Vp14304, Vi 2974, Vd 0, QPPS 2096

#define Kp 1.0
#define Ki 0.5
#define Kd 0.0
#define qpps 2200       

//Set PID Coefficients
  roboclawR.SetM1VelocityPID( 0x80,Kd,Kp,Ki,qpps);  // right ankle
  roboclawR.SetM2VelocityPID( 0x80,Kd,Kp,Ki,qpps);  // right knee
  roboclawR.SetM1VelocityPID( 0x81,Kd,Kp,Ki,qpps);  // left ankle
  roboclawR.SetM2VelocityPID( 0x81,Kd,Kp,Ki,qpps);  // left knee
  roboclawR.SetM1VelocityPID( 0x82,Kd,Kp,Ki,qpps);  // left hip
  roboclawR.SetM2VelocityPID( 0x82,Kd,Kp,Ki,qpps);  // right hip
 */
 
  AllStop( 'R' );               // stop everything and reset encoders
  Compass_Left_Foot( 'N' );     // dump compass data left foot
  Compass_Right_Foot( 'N' );    // dump compass data right foot
  while (Serial.available() > 0)   // clean out any characters in serial buffer at start up
      c = Serial.read();          // dump keys in dont need  
//   roboclawR.clear();       
}

void loop() 
{
  LedCnt ++;          // just a blinking led on mega heart
  if( LedCnt > 25 )
  {
    digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle RED LED pin heart beat
    LedCnt = 0;
  }
  delay( 50 );
  if (Serial.available () > 0)             
    {
    SignString = 1;     // positive number
    while (Serial.available () > 0)        
      {
      delay (10);
      c = Serial.read ();                    
      if (c == '\r')                  // look for end of line to exit
      {
        NumIn = inString.toInt();    // Convert readString into a number
        NumIn = constrain(NumIn, -12001, 12001);      // limit number

// next print lines for testing
        Serial.print( ">" );         // Echo captured string
        Serial.println( sBuffer );   // Echo captured string
        ProcessCommand();
        sBuffer = "";               // reset buffer and inString
        inString = "";
        NumIn = 0;                  // reset integer number
        continue;
      }
      sBuffer += c;                 // make string
      if( isDigit(c) ) 
        inString += c;              // save just number
      if( c == '-' )
      {
        SignString = -1;            // save negative sign
        inString += c;
      }
    }    // end while
  }      // end if serial 
}

void ProcessCommand ()            
{
  if (sBuffer.length () > 0)
    {
    sBuffer.toUpperCase ();       
    if( sBuffer[0] == 'E' )  // errors and buffer status
      WaitBuffer();

    if( sBuffer[0] == 'B' )  // bend down  
      BendDown();

    if( sBuffer[0] == 'G' ) // compass left and right foot display
    {
      Compass_Left_Foot( 'D' );
      Compass_Right_Foot( 'D' );
    }
    
    if( sBuffer[0] == 'D' )          // show me all data
    {
      roboclawR.clear();       
      roboclawR.flush();       
      displayspeed( 'D' );          // 1 turns on display
//      Compass_Left_Foot( 'D' );     // D turns on display
//      Compass_Right_Foot( 'D' );
    }
     
    if( sBuffer[0] == 'F' )  // stand on one foot
      LeftFoot();

    if( sBuffer[0] == 'H' )  // find center for hips
      CenterHips( 'B' );     // B for both hips could do L or R

    if( sBuffer[0] == 'K' )  // both knees to home
    {
      KneeLeftLS();
      KneeRightLS();
    }
    if( sBuffer[0] == 'L' )  // level feet
    {
      LevelLeftFt();
      LevelRightFt();
    }
 
    if( sBuffer[0] == 'N' )  // using number pad to control leg in samll steps
      NumDrive(); 

    if( sBuffer[0] == 'C' )  // read current
      DisAmps(); 
        
    if( sBuffer[0] == 'S' )  // motors stop if 2nd char is R the encoders are reset
      AllStop( sBuffer[ 1 ] );
      
    if( sBuffer[0] == 'W' )  // step and walk
    {
      Step();
//      delay( 500 );        
//      Step();
    }

   if( sBuffer[0] == 'T' )   // zero encoder
      TestPID();             // figure out pid values

   if( sBuffer[0] == 'Z' )   // zero encoder
      ZeroEnc( NumIn );      // 1=right ankle 2=right knee 3=left ankle 4=left knee

   else                               
      Serial.println( "?" );  
  }
}

// uses knees and ankles to bend down, limit is plastic knee parts
void BendDown()
{
     Serial.println( "***   bend knees & ankles, keep feet flat" );
// reset encoders next line will cause an error when running several times
// there is a deadzone on the position command of 10 
// so the commands telling position of 0 maybe up to 10 off
     AllStop( 'R' );             // no where we start and set encoders to zero
     displayspeed(  'D'  );        // just to see where we start
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000,7000,1); 
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000,7000,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000,-6500,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000,-6500,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x82,800,500,500,-1500,1); 
     roboclawR.SpeedAccelDeccelPositionM2(0x82,800,500,500,1500,1); 
     delay( 4000 );     // just see stop in between commands  
     WaitSpeed();       // wait for speed to be 0
     displayspeed( 'D' );
     Serial.println( "****   straighten knees & ankles down, feet flat" );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000,50,0); // almost all the way back
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000,50,0); 
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000,0,0); 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000,0,0); 
     roboclawR.SpeedAccelDeccelPositionM1(0x82,800,500,500,0,0); // move left hip
     roboclawR.SpeedAccelDeccelPositionM2(0x82,800,500,500,0,0); // move right hip 
     delay( 4000 );     // just see stop in between commands  
     WaitSpeed();       // wait for speed to be 0
     KneeRightLS();     // find limit switch
     KneeLeftLS();
     WaitSpeed();       // wait for speed to be 0
     displayspeed( 'D' );
     Serial.println( "***   Kneel Done" );
}

// use pitch to level left foot
void LevelLeftFt()
{
     int LevelAnkleL = 1;
     int t = 0;
     Serial.println( "***   level left foot" );
     Compass_Left_Foot( 'N' );          // clean out que
     for( int q=0; q<15; q++ )
     {
       Compass_Left_Foot( 'D' );          // check pitch
       LevelAnkleL = (-LeftPitch) * 15;   // compass reading ankle
       Serial.println( LevelAnkleL );       // for testing
       if( (LeftPitch > -2) && (LeftPitch < 2) )
       {
          LevelAnkleL = 0;
          Serial.println( "%%%   left ankle level" );
          Compass_Left_Foot( 'D' );
          q = 25;           // just a way out of for loop
       }
       t = abs(LevelAnkleL);
       if( LeftPitch <1 )
         roboclawR.SpeedDistanceM1( 0x81,-1000,t,1 );   // ankle left move
       if( LeftPitch >1 )
         roboclawR.SpeedDistanceM1( 0x81,1000,t,1 );   // ankle left move
       delay( 400 );               // time for motor to start before checking
       displayspeed(  'N'  );      // dont need to see current speed just set vars
       while( (LeftAnkleSpd >5) || (LeftAnkleSpd <-5) )  // looking for speed to be 0
       {
        aval = analogRead( AnalogPins[ 3 ] );  // check upper switch left ankle
        if( aval < 20 )
          roboclawR.BackwardM1( 0x81, 0x00 );  // stop left ankle
        displayspeed(  'N'  );                     // dont need to see current speed just set var
       }  // end while
     delay( 100 );
     }         // end for loop
     Serial.println( "***  level done" );
}

void LevelRightFt()
{
     int LevelAnkleR = 1;
     int t = 0;
     Serial.println( "***   level Right foot" );
     Compass_Right_Foot( 'N' );          // clean out que
     for( int q=0; q<15; q++ )
     {
       Compass_Right_Foot( 'D' );          // check pitch
       LevelAnkleR = (-RightPitch) * 15;   // compass reading ankle
       Serial.println( LevelAnkleR );        // for testing
       if( (RightPitch > -2) && (RightPitch < 2) )
       {
          LevelAnkleR = 0;
          Serial.println( "%%%   Right ankle level" );
          Compass_Right_Foot( 'D' );
          q = 25;           // just a way out of for loop
       }
       t = abs(LevelAnkleR);
       if( RightPitch <1 )
         roboclawR.SpeedDistanceM1( 0x80,-1000,t,1 );   // ankle Right
       if( RightPitch >1 )
         roboclawR.SpeedDistanceM1( 0x80,1000,t,1 );   // ankle Right  
       delay( 400 );               // time for motor to start before checking
       displayspeed(  'N'  );      // dont need to see current speed just set vars
       while( (RightAnkleSpd >5) || (RightAnkleSpd <-5) )  // looking for speed to be 0
       {
        aval = analogRead( AnalogPins[ 5 ] );  // check upper switch Right ankle
        if( aval < 20 )
          roboclawR.BackwardM1( 0x80, 0x00 );  // stop Right ankle
        displayspeed(  'N'  );                 // dont need to see current speed just set var
       }  // end while
     delay( 100 );
     }         // end for loop
     Serial.println( "***  level done" );
}

// lets keep moving left knee to limit switch
void KneeLeftLS()
{
     Serial.println( "***   left  knee to ls" );
     aval = analogRead( AnalogPins[ 2 ] );  // check limit switch left knee
     if( aval < 500 )                     // check switch first
       goto StpLftLs;
     roboclawR.BackwardM2( 0x81,70 );       // make knee straight address and speed
     while( aval > 500 )
        aval = analogRead( AnalogPins[ 2 ] ); // check limit switch left knee
StpLftLs:
     roboclawR.BackwardM2( 0x81,00 );       // stop
     delay( 1000 );
     roboclawR.ResetEncoders( 0x81 );      // reset encoders left leg
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1000,2000,2000,1600,1); // move off switch
     delay( 3000 );           // needs to get off limit switch   
     WaitSpeed();             // wait for speed to be 0
     displayspeed( 'D' );
     roboclawR.ResetEncoders( 0x81 );      // reset encoders left leg
     Serial.println( " on switch & encoder reset" );
}

// lets keep moving right knee to limit switch
void KneeRightLS()
{
// lets keep moving right knee to limit switch
     roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
     Serial.println( "***   right knee to ls" );
     aval = analogRead( AnalogPins[ 4 ] ); // check limit switch right knee
     if( aval < 500 )                     // check switch first
       goto StpRghLs;
     roboclawR.BackwardM2( 0x80,70 );      // make knee straight address and speed
     while( aval > 500 )
        aval = analogRead( AnalogPins[ 4 ] ); // check limit switch right knee
StpRghLs:
     roboclawR.BackwardM2( 0x80,00 );     // stop
     delay( 100 );
     roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1000,2000,2000,1500,1); // move off switch
     delay( 3000 );           // needs to get off limit switch   
     WaitSpeed();             // wait for speed to be 0
     displayspeed( 'D' );
     roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
     Serial.println( " on switch & encoder reset" );
} 

void Step()
{
     int t;
     Serial.println( "***   take a step" );
     displayspeed( 'D' );                   // let me know where we start for hips
     Serial.print( "***   ankle rotation right=");    // shift weight to right foot
     for( t=1; t<58; t++ )                      
     {
        AnkleServoR.write( RightAnkleRot - t );       // rotating both ankles
        AnkleServoL.write( LeftAnkleRot + t );
        delay( 50 );
     }
     RightAnkleRot = RightAnkleRot - t;   // remember position
     LeftAnkleRot = LeftAnkleRot + t;
     Serial.print( RightAnkleRot);        // show me
     Serial.print( " left=");
     Serial.println( LeftAnkleRot);      // show me    
      
     Serial.println( "***   bend right knee & ankle a little leaning legs to right side" );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,1800,1); // right knee 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,-2000,1);  // right ankle
     delay( 1500 );
     WaitSpeed();
     Serial.println( "***   ankle left pushes down forcing legs over to right side" );
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,1000,1000,3000,0);
     delay( 1500 );     // wait to let unit stablize, rocks around
     WaitSpeed();
//     WaitKey();
     
// should balance on one leg here
     Serial.println( "***   lift left leg, bend knee & ankle, rotating left hip forward" );
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,4500,1); // knee
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,-4000,1); // ankle
     delay( 1500 );   // removed trying to get left leg to stay forward
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,-400,1);    // hip
     delay( 1500 );
     WaitSpeed();
//     WaitKey();
     
     Serial.println( "***   straighten left knee and ankle down" );
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,1500,0);   // knee left 
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1000,2000,2000,-1000,0);   // ankle left 
     delay( 1500 );
     WaitSpeed();
//     WaitKey();
     
/*    Serial.println( "***  straighten right knee a little" );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,100,0);   // knee right
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,1500,0);   // ankle was to much at 2000
     delay( 1500 );
     WaitSpeed();
     WaitKey();
*/               
     Serial.print( "***   ankle rotation right=");  
     for( t=1; t<116; t++ )   
     {
        AnkleServoR.write( RightAnkleRot + t );
        AnkleServoL.write( LeftAnkleRot - t );
        delay( 70 );
     }
     RightAnkleRot = RightAnkleRot + t;
     LeftAnkleRot = LeftAnkleRot - t;
     Serial.print( RightAnkleRot);      // show me
     Serial.print( " left=");
     Serial.println( LeftAnkleRot);      // show me
//     WaitKey();

     Serial.println( "***   bend left ankle to shift weight forward" );
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,-1500,0);    // ankle left **** was 400 600 800 1000 1200
//     delay( 1000 );
     Serial.println( "***  straighten right knee a little" );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,100,0);   // knee right
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,1500,0);   // ankle was to much at 2000
     delay( 2500 );
     WaitSpeed();
//     WaitKey();
     
     Serial.println( "***   lift right leg rotating right hip forward " );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,5000,0);   // knee right 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,-4000,0);  // ankle right   
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,400,1);    // hip left
     roboclawR.SpeedAccelDeccelPositionM2(0x82,1000,500,500,600,0);      // hip right *** was 400 600
     delay( 4000 );
     WaitSpeed();
//     WaitKey();
      
     Serial.println( "***   straighten legs & hips home " );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,0,0);    // knee right 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,0,0);    // ankle right   
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,0,0);    // knee left
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,0,0);    // ankle left
     delay( 2000 );
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,0,0);      // hip left
     roboclawR.SpeedAccelDeccelPositionM2(0x82,1000,500,500,0,0);      // hip right
     delay( 1000 );
     Serial.print( "***   ankle rotation right= ");   
     for( t=1; t<58; t++ )   
     {
        AnkleServoR.write( RightAnkleRot - t );
        AnkleServoL.write( LeftAnkleRot + t );
        delay( 100 );
     }
     RightAnkleRot = RightAnkleRot - t;
     LeftAnkleRot = LeftAnkleRot + t;
     Serial.print( RightAnkleRot);
     Serial.print( " left=" );
     Serial.println( LeftAnkleRot);
     delay( 2000 );
     WaitSpeed();
     Serial.println( "***   Step Done" );
}

// just testing wait routines with IonStudio PID numbers
void TestPID()   
{
   int addr = 0x80;             // right leg
   int tstspd = 1500;           // speed for motor
   int tstaccl = 2000;
   int tstpos = 4000;           // position to go to
   Serial.print( "***   test position command right knee " );
   Serial.print( addr );
   Serial.print( " " );
   Serial.print( tstspd );
   Serial.print( " " );
   Serial.print( tstaccl );
   Serial.print( " " );
   Serial.println( tstpos );
   AllStop( 'R' );       // reset encoders
   roboclawR.SpeedAccelDeccelPositionM2(0x80,tstspd,tstaccl,tstaccl,tstpos,1); //addr,speed start,accl,stop accl,pos,flag
   delay( 1000 );     
   WaitSpeed();       // wait for speed to be 0
   Serial.println( "***  now back" );
   roboclawR.SpeedAccelDeccelPositionM2(0x80,tstspd,tstaccl,tstaccl,10,0);  // back to 0
   WaitBuffer();
   WaitSpeed();
   Serial.println( "***   test done" );
}

// lift left foot and stand on right foot working Jan 13
void LeftFoot()   
{
      int t = 0;
      Serial.println( "***   lift left foot" );
      Serial.print( "***   ankle rotation = ");   
      for( t=1; t<57; t++ )  
      {
        AnkleServoR.write( RightAnkleRot - t );
        delay( 50 );
      }
      Serial.println( RightAnkleRot - t );
      RightAnkleRot = RightAnkleRot - t;      // save
      Serial.println( "***   bend right knee & ankle a little pushing over legs to right side" );
      roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,1800,1); // right knee 
      roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,-2000,1);  // right ankle
      delay( 1000 );
      roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,1000,1000,3300,0);    // ankle left push down to tilt
      delay( 4000 );
      WaitSpeed();        // waits till speed is 0
      Serial.println( "***  bend left knee, Left Hip Forward, bend ankle" );
      roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,7200,1); // knee
      roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,-7000,1); // ankle
      roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,-400,1);    // hip
      delay( 4000 );
      ToeServoL.write( LeftToe + 40 );       
      WaitSpeed();        // waits till speed is 0
      delay( 500 );
      ToeServoL.write( LeftToe );        
      Serial.println( "***   straighten knees, ankles flat and Left Hip back" );
      roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,50,0);   // knee right 
      roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,50,0);   // knee left
      roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,0,0);    // ankle left
      roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,0,0);    // ankle right   
      roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,0,0);      // hip left
      delay( 1600 ); // want leg to come down a little before rotating ankles
      Serial.print( "***   ankle rotation right=");   
      for( t=1; t<57; t++ )   
      {
        AnkleServoR.write( RightAnkleRot + t );
        delay( 120 );          
      }
      RightAnkleRot = RightAnkleRot + t;      // save new location
      Serial.println( RightAnkleRot );
      delay( 4000 );
      WaitSpeed();
      KneeRightLS();      // find limit switch knees
      KneeLeftLS();
      Serial.println( "*** Left Foot Done" );
}     // end left foot

// stops program and waits for a key input used for testing routines
void WaitKey()
{
  if( NumIn != 1 )
  {
    Serial.println( "- - - - - waiting key input" );     // NumIn = to 1 skip waiting
    while (Serial.available() == 0) 
    {       
      digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle RED LED pin heart beat
      delay (100);
      digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle RED LED pin heart beat
      delay (100);
    }
    c = Serial.read ();        // dump key in dont need      
  }     
}

// checks roboclaw boards for errors and waits until commands are out of buffers
void WaitBuffer()
{ 
    uint8_t depth1;
    uint8_t depth2;
    bool valid;
    int i = 0;
    // error codes Normal 0x00 M1 OverCurrent 0x01 M2 OverCurrent 0x02 E-Stop 0x04 Temperature 0x08
    // Main Battery High 0x10 Main Battery Low 0x20 Logic Battery High 0x40 Logic Battery Low 0x80
    Serial.println( "...   RoboClaw buffers (128 means no commands in buffers, not that command is finished" );
    Serial.print( "...   RoboClaw controller errors 80=" );
    uint16_t reading = roboclawR.ReadError(0x80, &valid);
    Serial.print( reading );
    Serial.print( " 81=" );
    delay( 20 );
    reading = roboclawR.ReadError(0x81, &valid);
    Serial.print( reading );
    delay( 20 );
    reading = roboclawR.ReadError(0x82, &valid);
    Serial.print( " 82=" );
    Serial.println( reading );
    delay( 20 );
    // The buffer value will be 0x80 if the motors are idle
    // number returned is how many commands are buffered waiting to run
    // Loop until command has completed 80=done 0=busy 1=one command waiting ect

    do
    {
      roboclawR.clear();   
      roboclawR.ReadBuffers( 0x80, depth1, depth2 ); 
      Serial.print( " 80=" );
      Serial.print( depth1 );
      Serial.print( "&" );
      Serial.print( depth2 );
      i++;
      if( i >20 )
        goto Stop1;
      delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
    } while( depth1!=0x80 || depth2!=0x80 );
Stop1:
    Serial.println( " " );

    i = 0;
    do
    {
      roboclawR.clear();
      roboclawR.ReadBuffers( 0x81, depth1, depth2 );
      Serial.print( " 81=" );
      Serial.print( depth1 );
      Serial.print( "&" );
      Serial.print( depth2 );
      i++;
      if( i >20 )         // sometime hangs in these, so a way out
        goto Stop2;
      delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
    } while( depth1!=0x80 || depth2!=0x80 );  //Loop until command has completed 80=done 0=busy
Stop2:
    Serial.println( " " );
    i = 0;
    do
    {
      roboclawR.clear();
      roboclawR.ReadBuffers( 0x82, depth1, depth2 );
      Serial.print( " 82=" );
      Serial.print( depth1 );
      Serial.print( "&" );
      Serial.print( depth2 );
      i++;
      if( i >20 )
        goto Stop3;
     delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
   } while( depth1!=0x80 || depth2!=0x80 );  //Loop until command has completed 80=done 0=busy
Stop3:
    Serial.println( " " );
}

/* watch speed   waits till at 0 speed or quits if opto switch is active on either knee   
    roboclawR.BackwardM1( 0x80, 0x00 );   // stop right ankle
    roboclawR.BackwardM2( 0x80, 0x00 );   // stop right knee
    roboclawR.BackwardM1( 0x81, 0x00 );  // stop left ankle
    roboclawR.BackwardM2( 0x81, 0x00 );  // stop left knee
    roboclawR.BackwardM1( 0x82, 0x00 );   // stop left hip
    roboclawR.BackwardM2( 0x82, 0x00 );   // stop right hip 
*/
// checks for speed to be stopped or limit switch active
void WaitSpeed()
{
    Serial.println( "...waiting for motors stopped" );
    delay( 1000 );               // time for motor to start before checking was 700
    do
    {
      displayspeed2(  'N'  );   
      aval = analogRead( AnalogPins[ 4 ] ); // check upper switch right knee
      if( aval < 500 )
      {
        roboclawR.BackwardM2( 0x80, 0x00 );  // stop right knee
        Serial.print( " RK " );
        delay( 400 );
      }
      
      aval = analogRead( AnalogPins[ 5 ] );  // check upper switch right ankle   
      if( aval < 500 )
      {
        roboclawR.BackwardM1( 0x80, 0x00 );  // stop right ankle
        Serial.print( " RA " );
        delay( 400 );
      }
      
      aval = analogRead( AnalogPins[ 2 ] );  // check upper switch left knee
      if( aval < 500 )
      {
        roboclawR.BackwardM2( 0x81, 0x00 );  // stop left knee
        Serial.print( " LK " );
        delay( 400 );
      }
      
      aval = analogRead( AnalogPins[ 3 ] );  // check upper switch left ankle
      if( aval < 500 )
      {
        roboclawR.BackwardM1( 0x81, 0x00 );  // stop left ankle
        Serial.print( " LA " );
        delay( 400 );
      }
      delay( 75 );                          // need to wait 10ms between reads ion manual
    }while( AnySpeed == 1 );
// next line did not work seems like it should
//    }while( (RightKneeSpd >5) || (LeftKneeSpd >5) || (RightKneeSpd <-5) || (LeftKneeSpd <-5) || (RightAnkleSpd >5) || (LeftAnkleSpd >5) || (RightAnkleSpd <-5) || (LeftAnkleSpd <-5) );
    displayspeed(  'D'  ); 
}     // end speed

// shuts down all motors and homes servos on toes and rotation of ankles
// can reset encoder counters
void AllStop( char disp )
{
      roboclawR.BackwardM1( 0x80, 0x00 );  // stop right ankle
      roboclawR.BackwardM2( 0x80, 0x00 );  // stop right knee
      roboclawR.BackwardM1( 0x81, 0x00 );  // stop left ankle
      roboclawR.BackwardM2( 0x81, 0x00 );  // stop left knee
      roboclawR.BackwardM1( 0x82, 0x00 );  // stop left hip
      roboclawR.BackwardM2( 0x82, 0x00 );  // stop right hip
      ToeServoL.write( LeftToe );          // toes stop and make level arm not set the same on both toes
      ToeServoR.write( RightToe );
      AnkleServoL.write( LeftAnkleRot );   // ankles stop and make level
      AnkleServoR.write( RightAnkleRot );
      Serial.print( "*** Motors at rest" );   
      if( disp == 'R' )      // reset encoders 
      {
        roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
        roboclawR.ResetEncoders( 0x81 );      // reset encoders left leg
        roboclawR.ResetEncoders( 0x82 );      // reset encoders hips
        Serial.print( " & right/left leg & hip encoders reset" );   
      }
      Serial.println( " " );              
}

// displays curent from motors
void DisAmps()
{
int currentFromMotorOne;
int currentFromMotorTwo;
bool gotIt;
    gotIt = roboclawR.ReadCurrents( 0x80, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
     Serial.print("*** Current RghAnk= ");
     Serial.print(currentFromMotorOne);
     Serial.print("ma RghKne=");
     Serial.print(currentFromMotorTwo);
   }
   gotIt = roboclawR.ReadCurrents( 0x81, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
      Serial.print("ma LftAnk= ");
      Serial.print(currentFromMotorOne);
      Serial.print("ma LftKne=");
      Serial.print(currentFromMotorTwo);
   }
   gotIt = roboclawR.ReadCurrents( 0x82, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
      Serial.print("ma LftHip= ");
      Serial.print(currentFromMotorOne);
      Serial.print("ma RghHip=");
      Serial.print(currentFromMotorTwo);
   }
   Serial.println("ma");
}

// displays data from encoders, speed, battery volts
void displayspeed( char DispOff )
{
  uint8_t status1,status2,status3,status4;
  bool valid1,valid2,valid3,valid4;
  address = 0x80;
  int32_t enc1 = roboclawR.ReadEncM1( address, &status1, &valid1);
  int32_t enc2 = roboclawR.ReadEncM2( address, &status2, &valid2);
  int32_t speed1 = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t speed2 = roboclawR.ReadSpeedM2( address, &status4, &valid4);
   
  if( DispOff == 'D' )            // may want to check status but not show on display
  {
   if(valid1)
   {
     Serial.print("  Encoder Right UpperAnkle_M1:");
     Serial.print( enc1,DEC );  
   }
   if(valid2)
   {
     Serial.print( " UpperKnee_M2:" );
     Serial.print( enc2,DEC );
   }
   if(valid3)
   {
     Serial.print(" Sp_M1:");
     Serial.print( speed1,DEC );
   }
   if(valid4)
   {
     Serial.print(" Sp_M2:");
     Serial.println( speed2,DEC );
   }
  }  // end if
  delay( 50 );
  address = 0x81;
  int32_t enc1L = roboclawR.ReadEncM1( address, &status1, &valid1);
  int32_t enc2L = roboclawR.ReadEncM2( address, &status2, &valid2);
  int32_t speed1L = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t speed2L = roboclawR.ReadSpeedM2( address, &status4, &valid4);
 if( DispOff == 'D' )            // may want to check status but not show on display left leg
 {
  if(valid1)
  {
    Serial.print("  Encoder Left  UpperAnkle_M1:");
    Serial.print( enc1L,DEC );  
  }
  if(valid2)
  {
    Serial.print( " UpperKnee_M2:" );
    Serial.print( enc2L,DEC );
  }  
  if(valid3)
  {
    Serial.print(" Sp_M1:");
    Serial.print( speed1L,DEC );
  }   
  if(valid4)
  {
    Serial.print(" Sp_M2:");
    Serial.println( speed2L,DEC );
  }
 }
  delay( 50 );
  address = 0x82;
  int32_t enc1H = roboclawR.ReadEncM1( address, &status1, &valid1);
  int32_t enc2H = roboclawR.ReadEncM2( address, &status2, &valid2);
  int32_t speed1H = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t speed2H = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  long BatVolt = roboclawR.ReadMainBatteryVoltage( address, &valid1 );
//  long LogicVolt = roboclawR.ReadLogicBatteryVoltage( address, &valid1 );

  LeftHipSw =  digitalRead( HipLeft );      // read limit switch on hip
  LeftKneeSw = analogRead( AnalogPins[ 2 ] ); // get raw number
  LeftAnkleSw = analogRead( AnalogPins[ 3 ] ); 
  RightHipSw = digitalRead( HipRight );
  RightKneeSw = analogRead( AnalogPins[ 4 ] ); // get raw number
  RightAnkleSw = analogRead( AnalogPins[ 5 ] ); 

 if( DispOff == 'D' )            // may want to check status but not show on display
 {
  if(valid1)
  {
    Serial.print("  Encoder Hips  Left_M1:");
    Serial.print( enc1H,DEC );  
  }
  if(valid2)
  {
     Serial.print( " Rgh_M2:" );
     Serial.print( enc2H,DEC );
  }
  if(valid3)
  {
     Serial.print(" Sp_M1:");
     Serial.print( speed1H,DEC );
  }
  if(valid4)
  {
     Serial.print(" Sp_M2:");
     Serial.print( speed2H,DEC );
     Serial.print( " BatV:" );
     Serial.println( BatVolt/10.0 );
  }
//  not suppling logic voltage to roboclaw boards so no reason to show
// Serial.print( " LogV:" );
// Serial.println( LogicVolt/10.0 );

  Serial.print( "  Switches Right Hip=" );     
  Serial.print( RightHipSw );     
  Serial.print( " Kne=" );     
  Serial.print( RightKneeSw );     
  Serial.print( " Ank=" );     
  Serial.print( RightAnkleSw );     
  Serial.print( "  Left Hip=" );     
  Serial.print( LeftHipSw );     
  Serial.print( " Kne=" );     
  Serial.print( LeftKneeSw );     
  Serial.print( " Ank=" );     
  Serial.println( LeftAnkleSw );      
  }       // end display off
  
// save new encoder data  
  RightAnkleSpd = speed1;         
  RightKneeSpd = speed2;
  RighHipSpd = speed1H;
  RightAnkleCnt = enc1;
  RightKneeCnt = enc2;
  RightHipCnt = enc1H;
  LeftAnkleSpd = speed1L;
  LeftKneeSpd = speed2L;
  LeftHipSpd = speed2H;
  LeftAnkleCnt = enc1L;
  LeftKneeCnt = enc2L;
  LeftHipCnt = enc2H;
}  // end display routine

// displays speed info only short version of display speed and encoders
void displayspeed2( char DispOff )
{
  uint8_t status3,status4;
  bool valid3,valid4;
  AnySpeed = 0;
  roboclawR.clear();         
  address = 0x80;
  int32_t RightAnkleSpd = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t RightKneeSpd = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  if( RightAnkleSpd>5 || RightAnkleSpd<-5 )
    AnySpeed = 1;
  if( RightKneeSpd>5 || RightKneeSpd<-5 )
    AnySpeed = 1;
  if( DispOff == 'D' )            // may want to check status but not show on display
  {
   if( valid3 )
   {
     Serial.print("___Speeds 80M1_RA:");
     Serial.print( RightAnkleSpd,DEC );
   }
   if( valid4 )
   {
     Serial.print(" 80M2_RK:");
     Serial.print( RightKneeSpd,DEC );
   }
  }  // end if
  roboclawR.clear();       
  address = 0x81;
  int32_t LeftAnkleSpd = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t LeftKneeSpd = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  if( LeftAnkleSpd>5 || LeftAnkleSpd<-5 )
    AnySpeed = 1;
  if( LeftKneeSpd>5 || LeftKneeSpd<-5 )
    AnySpeed = 1;
 if( DispOff == 'D' ) 
 {
  if( valid3 )
  {
    Serial.print(" 81M1_LA:");
    Serial.print( LeftAnkleSpd,DEC );
  }   
  if( valid4 )
  {
    Serial.print(" 81M2_LK:");
    Serial.print( LeftKneeSpd,DEC );
  }
 }
  roboclawR.clear();       
  address = 0x82;
  int32_t RightHipSpd = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  int32_t LeftHipSpd = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  if( RightHipSpd>5 || RighHipSpd<-5 )
    AnySpeed = 1;
  if( LeftHipSpd>5 || LeftHipSpd<-5 )
    AnySpeed = 1;
 if( DispOff == 'D' )       
 {
  if( valid3 )
  {
     Serial.print(" 82M1_RH:");
     Serial.print( RightHipSpd,DEC );
  }
  if( valid4 )
  {
     Serial.print(" 82M2_LH:");
     Serial.print( LeftHipSpd,DEC );
  }
  Serial.println(" ");
 }       // end display off
}        // end display routine


// trying to get hip motors to be at same spot
// hard to do as the legs hanging in the air have momentom when stopping
// readjust linkage Jan 13
void CenterHips( char hipp )    
  {
  Serial.println( "***   Center Hips" );
  Serial.print( "find limit switch right hip " );
  while ( (digitalRead( HipRight )) == HIGH )
  {
     Serial.print( "#" );  
     roboclawR.ForwardM2( 0x82, 100 ); // max 127 for speed
     delay( 80 );                     // how long to have motor on
     roboclawR.ForwardM2( 0x82, 0 );  // motor off
     delay( 70 ); 
  } 
  Serial.println( " " );
  Serial.print( "find limit switch left  hip " );
  while ( (digitalRead( HipLeft )) == HIGH )
  {
     Serial.print( "&" );  
     roboclawR.BackwardM1( 0x82, 100 );  // max speed 127
     delay( 80 );                    
     roboclawR.BackwardM1( 0x82, 0 );  
     delay( 70 ); 
  }     
  Serial.println( " " );

// need to reset hip encoders moving absolute next
  roboclawR.ResetEncoders( 0x82 );      // reset encoders hips

// left hip is a little more forward then the right hip when on limit switch just the way built
  delay( 1000 );
  roboclawR.SpeedAccelDeccelPositionM1(0x82,800,1000,1000,-450,1);   // left forward is minus value
  delay( 1000 );
  roboclawR.SpeedAccelDeccelPositionM2(0x82,800,1000,1000,600,1);  // right forward is plus value
  delay( 2000 );
  displayspeed(  'D'  );        // show me encoders
  roboclawR.ResetEncoders( 0x82 );      // reset encoders hips
  displayspeed(  'D'  );        // show me encoders
  RightHipCnt = 0;
  LeftHipCnt = 0;       
  Serial.println( "***   hips done" );
 }    // end center hips

/* lower limit switches go to motor controllers for now
 * upper switches to mega bd
 A0 
 A1 
 A2 left knee opto switch high>800 low<700
 A3 left ankle opto switch high>800 low<700
 A4 right knee opto switch high>800 low<700
 A5 right ankle opto switch high>800 low<700
 A6 
 A7 
 */

void ZeroEnc( int Encod )  // Encod can be 1=right ankle 2=right knee 3 left ankle 4 left knee
{
  displayspeed(  'D'  );   // get latest values
  if( Encod == 1 )    // right ankle
  {
//    Serial.println( "Zero right ankle" );
    while( (RightAnkleCnt > 30) )
    {
      roboclawR.SpeedDistanceM1( 0x80,-600,0020,1 );
      Serial.println( "RAD plus" );
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
    while( (RightAnkleCnt < -30) )
    {
      roboclawR.SpeedDistanceM1( 0x80,600,0020,1 );
      Serial.println( "RAD minus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }  
  }   // end encod 1
  
  if( Encod == 2 )    // right knee
  {
//    Serial.println( "Zero right knee" );
    while( (RightKneeCnt > 30) )
    {
      roboclawR.SpeedDistanceM2( 0x80,-900,0020,1 );
      Serial.println( "RKD plus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
    while( (RightKneeCnt < -30) )
    {
      roboclawR.SpeedDistanceM2( 0x80,900,0020,1 );
      Serial.println( "RKD minus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
  }     // end encod 2
  
  if( Encod == 3 )    // left ankle
  {
//    Serial.println( "Zero left ankle" );
    while( (LeftAnkleCnt > 30) )
    {
      roboclawR.SpeedDistanceM1( 0x81,-600,0020,1 );
      Serial.println( "LAD plus" );
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
//    while( (LeftAnkleCnt < -30) )
    {
      roboclawR.SpeedDistanceM1( 0x81,600,0020,1 );
      Serial.println( "LAD minus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }  
  }       // end encod 3

  if( Encod == 4 )    // left knee
  {
//    Serial.println( "Zero left knee" );
    while( (LeftKneeCnt > 30) )
    {
      roboclawR.SpeedDistanceM2( 0x81,-900,0020,1 );
      Serial.println( "LKD plus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
    while( (LeftKneeCnt < -30) )
    {
      roboclawR.SpeedDistanceM2( 0x81,900,0020,1 );
      Serial.println( "LKD minus" );                     
      WaitSpeed();      // routine waits till speed is 0 or opto switch triggered
    }
  }     // end encod 2

 Serial.println( "***   Zero end" );
}

 // removed limit switches for display Oct 13  they now go to robocalw inputs
 // not using this routine anymore
void ReadLimitSw()
{
 String area[7] = { " ", 
                    " ",
                    "  LKOpt=",
                   " LAOpt=", 
                   " RKOpt=",     
                   " RAOpt=",     
                   " "};

 for ( i=2; i<6; i++ )
 {
   agDist[i] = analogRead( AnalogPins[i] ); // get raw number
   delay( 10 );
   Serial.print( area[i] );                // Display limit switch
   Serial.print( agDist[i] );              // Display value
 }
}

// reads the 9 axis sensor on left foot
void Compass_Left_Foot( char dispp )
{
  int StartChar;
  String tempstr = " ";

  Serial2.print( "1" );             // request data from compass
  sBuffer = " ";
  while (Serial2.available () > 0)   // dump first reading   
  {
      delay (20);
      c = Serial2.read ();                 
      if (c == '\r')  
        break;
      sBuffer += c;             // make string
  }

  Serial2.print( "1" );             // request data from compass
  sBuffer = " ";
  while (Serial2.available () > 0)      
  {
      delay (20);
      c = Serial2.read ();                 
      if (c == '\r')  
      {
//        Serial.println( sBuffer );     // Echo captured string for testing
        break;
      }
      sBuffer += c;             // make string
   }
  StartChar = sBuffer.indexOf( 'R' );     // roll
  tempstr = sBuffer.substring( (StartChar+1),(StartChar+4) );
  LeftRoll = tempstr.toInt( );

  StartChar = sBuffer.indexOf( 'P' );     // pitch
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  LeftPitch = (tempstr.toInt( ) + 4 );     // dec 31 added correction
  LeftPitch = (tempstr.toInt( ) );     // not sure what is going on with this
  
  StartChar = sBuffer.indexOf( 'Y' );     // yaw
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  LeftYaw = tempstr.toInt( );
  
  if( dispp == 'D' ) 
  {  
    Serial.print( "  Gyro Left R:" );    
    Serial.print( LeftRoll );  
    Serial.print( " P:" );    
    Serial.print( LeftPitch );    
    Serial.print( " Y:" );    
    Serial.print( LeftYaw );  
    Serial.print( " AnkleRotCnt=" );    
    Serial.println( LeftAnkleRot );  
  }  
}     // end compass left

// reads the 9 axis sensor on right foot
void Compass_Right_Foot( char dispp )
{
  int StartChar;
  String tempstr = " ";
  while (Serial3.available () > 0)   // dump first reading   
  {
      delay (20);
      c = Serial3.read ();                 
      if (c == '\r')  
        break;
      sBuffer += c;             // make string
  }
  Serial3.print( "1" );             // request data from compass
  sBuffer = " ";
  delay (20);
  while (Serial3.available () > 0)      
  {
      delay (10);
      c = Serial3.read ();                 
      if (c == '\r')  
      {
//        Serial.println( sBuffer );     // Echo captured string testing
        break;
      }
      sBuffer += c;             // make string
  } 
  StartChar = sBuffer.indexOf( 'R' );
  tempstr = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RightRoll = tempstr.toInt( );

  StartChar = sBuffer.indexOf( 'P' );
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RightPitch = tempstr.toInt( );
  
  StartChar = sBuffer.indexOf( 'Y' );
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RightYaw = tempstr.toInt( );
  
  if( dispp == 'D' )     
  {  
    Serial.print( "  Gyro Right R:" );    
    Serial.print( RightRoll );  
    Serial.print( " P:" );    
    Serial.print( RightPitch );    
    Serial.print( " Y:" );    
    Serial.print( RightYaw );  
    Serial.print( " AnkleRotCnt=" );    
    Serial.println( RightAnkleRot );  
  }  
}     // end compass right

 // control platform by keypad numbers  manual mode
void NumDrive()
{
  int last = RightAnkleRot;                // starting place for ankle servos
  int lastt = RightToe;                    // starting place for ankle servos
  Serial.print( "Number Pad Control " );  
  Serial.println( sBuffer[ 1 ] );  
  if( sBuffer[ 1 ] == 'L' )         // left leg testing
        swleg = 1;
  if( sBuffer[ 1 ] == 'R' )         // right leg testing
        swleg = 2;
  if( sBuffer[ 1 ] == 'T' )         // toes testing
        swleg = 3;
  if( sBuffer[ 1 ] == 'A' )         // ankles testing
        swleg = 4;
  if( sBuffer[ 1 ] == 'H' )         // hip testing
        swleg = 5;

NumRepeat:
  {
    c = Serial.read ();      // get number from keypad             
    switch ( c )             // look at first character
    {   
                
    case '8':
      {
        if( swleg == 1 )           // left knee testing
        {
          Serial.println( "Upper Left Leg straight" );                     
          roboclawR.SpeedDistanceM2( 0x81,-1500,100 );  
        }
        if( swleg == 2 )           // right knee testing
        {
          Serial.println( "Upper Right Leg straight" );                     
          roboclawR.SpeedDistanceM2( 0x80,-1500,100 );  
        }
        if( swleg == 3 )          // toe testing
        {
          lastt = lastt + 5;
          ToeServoL.write( lastt );
          ToeServoR.write( lastt );
          Serial.print( "both toes up " );                     
          Serial.println( lastt );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          last = last + 5;
          AnkleServoR.write( last );
          Serial.print( "right ankle rotate to left (count up)" );                     
          Serial.println( last );
        }
        if( swleg == 5 )          // hip rotation testing
        {
          Serial.println( "Right Hip Back" );                     
          roboclawR.SpeedDistanceM2( 0x82,-1000,02 );  // distance 2400 would be 1 rev
        }
        break;    
      }
      
    case '2':
      {
        if( swleg == 1 )           // left knee testing
        {
          Serial.println( "Upper Left Leg bend" );                     
          roboclawR.SpeedDistanceM2( 0x81,1500,100 );  
        }
        if( swleg == 2 )           // right knee testing
        {
          Serial.println( "Upper Right Leg bend" );                     
          roboclawR.SpeedDistanceM2( 0x80,1000,100 );  
        }
        if( swleg == 3 )          // toe testing
        {
          lastt = lastt - 5;
          ToeServoL.write( lastt );
          ToeServoR.write( lastt );
          Serial.print( "both toes down " );                     
          Serial.println( lastt );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          last = last - 5;
          AnkleServoR.write( last );
          Serial.print( "right ankle rotate to right (count down)" );                     
          Serial.println( last );
        }
       if( swleg == 5 )          // hip rotation testing
        {
          Serial.println( "Right Hip Forward" );                     
          roboclawR.SpeedDistanceM2( 0x82,1000,02 );  // distance 2400 would be 1 rev
        }
        break;   
      }
        
    case '4':
      {
        if( swleg == 1 )          // left ankle up testing
        {
          roboclawR.SpeedDistanceM1( 0x81,1500,100 );  
          Serial.println( "left foot down" );                     
        }
        if( swleg == 2 )           // right ankle up testing
        {
          roboclawR.SpeedDistanceM1( 0x80,1500,100 );  
          Serial.println( "right foot down" );                     
        }                 
        if( swleg == 4 )          // ankle rotation testing
        {
          last = last + 5;
          AnkleServoL.write( last );
          Serial.print( "left ankle rotate to left (count up)" );                     
          Serial.println( last );
        }
        if( swleg == 5 )          // hip rotation testing
        {
          Serial.println( "Left Hip Forward" );                     
          roboclawR.SpeedDistanceM1( 0x82,-1000,02 );  // distance 2400 would be 1 rev
        }
        break;           
      }
      
    case '6':
      {
        if( swleg == 1 )        // left ankle down testing
        {
          roboclawR.BackwardM1( 0x81, 70 );   
          roboclawR.SpeedDistanceM1( 0x81,-1500,100 );  
          Serial.println( "left foot up" );                     
        }
        if( swleg == 2 )          // right ankle down testing
        {
          roboclawR.SpeedDistanceM1( 0x80,-1500,100 );  
          Serial.println( "right foot up" );                     
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          last = last - 5;
          AnkleServoL.write( last );
          Serial.print( "left ankle rotate to right (count down)" );                     
          Serial.println( last );
        }                   
        if( swleg == 5 )          // hip rotation testing
        {
          Serial.println( "Left Hip Back" );                     
// all distances and speeds are in quad pulses per second for next command
          roboclawR.SpeedDistanceM1( 0x82,1000,02 );  // distance 2400 would be 1 rev
        }
        break;           
      }
      
    case '5':
      {
        displayspeed(  'D'  );      // read encoders 
        Compass_Right_Foot( 'D' );
        Compass_Left_Foot( 'D' );
        break;           
      }
      
    case '0':
      {
        goto NumStop;                    
        break;           
      }
    }   // end case statement
    
  delay( 100 );         // hip rotation testing
  goto NumRepeat;
  }
NumStop:
  roboclawR.BackwardM1( 0x80, 0x00 );  // stop right ankle
  roboclawR.BackwardM2( 0x80, 0x00 );  // stop right knee
  roboclawR.BackwardM1( 0x81, 0x00 );  // stop right ankle
  roboclawR.BackwardM2( 0x81, 0x00 );  // stop right knee
  roboclawR.BackwardM1( 0x82, 0x00 );  // stop right hip
  roboclawR.BackwardM2( 0x82, 0x00 );  // stop right hip
  Serial.println( "*** exit keypad" );               
}

