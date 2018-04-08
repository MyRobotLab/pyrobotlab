/*  modified for mega and roboclaw   
 *  roboclaw right leg 2X15A firmware 4.1.23 hardware V5D Oct 1
 *  roboclaw  left leg 2X15A firmware 4.1.23 hardware V5D  Oct 6
 *  roboclaw  hips (older 2X15A firmware 4.1.23 hardware V5D  Nov 7
 *  trying to use position command on roboclaw instead of distance Jan 5
 *  have legs taking steps Jan 18
 *  added batteries, removed code not needed, moved 9 axis sensor to electronics base Jan 23
 *  removed toes and installed new ankles/feet Jan 28
 *  added 3dr axis for ankles, so now can up/down-pitch, rotate-roll, turn-yaw  Feb 7
 *  moved roboclaw boards to back of legs and changed limit switch outputs to go into roboclaw bds. used to be analog inputs
 *  added 9 axis sensors to each foot Feb 23 using hardware serial
 */

#include <Arduino.h>
#include <stdio.h>
#include <Servo.h>            // used for feet
#include <Wire.h>             // needed for compass
#include "RoboClaw.h"         // motor control
//#include <SoftwareSerial.h> // compass this has a problem that output to softserial moves servos on output lines

Servo ToeServoR;            // create servo object for toe right
Servo ToeServoL;            // create servo object for toe left
Servo AnkleServoR;          // create servo object for ankle right
Servo AnkleServoL;          // create servo object for ankle left

String sBuffer = "";        // string to hold asci key input string
String inString = "";       // string to hold numbers input
char c;                     // used in input key many places
String SendStr = " ";       // used for outputing data to terminal or bluetooth
long SendNo;                // used for outputing data to terminal or bluetooth
String verDate = "Feb 24,2018 afternoon";

int32_t LeftKneeCnt = 0;          // current positon of various joints
int32_t LeftAnkleCnt = 0;
int32_t LeftHipCnt = 0;
int LeftHipSw = 0;
int LeftKneeSw = 0;
int LeftAnkleSw = 0;
int32_t LeftKneeSpd = 0;
int32_t LeftAnkleSpd = 0;
int32_t LeftHipSpd = 0;
int LeftAnkleRot = 100;    // starting position should be level with floor
int LeftToe = 70;        // servo starting position 

int32_t RightKneeCnt = 0;
int32_t RightAnkleCnt = 0;
int32_t RightHipCnt = 0;
int RightHipSw = 0;
int RightKneeSw = 0;
int RightAnkleSw = 0;
int32_t RightKneeSpd = 0;
int32_t RightAnkleSpd = 0;
int32_t RightHipSpd = 0;
int RightAnkleRot = 95;   // starting position should be level with floor
int RightToe = 63;        // servo starting position
int BaseRoll;             // data from gyro on base
int BasePitch;
int BaseYaw;
int RfootRoll;             // data from gyro on right foot
int RfootPitch;
int RfootYaw;

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
int bluetooth = 2;      // 2=icstation bluetooth  1=sparkfun bluetooth 0=no bluetooth
int NumSteps = 1;       // number of steps to take on walk
int NumStepsLeft = 0;   // used in loop to watch how many steps to go
int StepTurn = 0;       // how far to turn feet yaw

// for circular buffer note to use this will need multiple values
int const BUFFER_SIZE = 10;   // Number of samples you want to smooth out
int datatoavg, indexBuffer = 0;
int circularBuffer[ BUFFER_SIZE ];
int sensorDataCircularSum;
int filteredOutput;
int average;                  // value from your sensor

const byte redLEDpin = 13;     // Pin heart beat
const int HipRight = 9;        // limit switch for hip
const int HipLeft = 8;

// used for special delay so having commands run while in delay
unsigned long interval = 5000;     // the time we need to wait
unsigned long previousMillis = 0;  // millis() returns an unsigned long.
unsigned long currentMillis = 0;

/* 
 *  software serial library has the following known limitations:
 *  If using multiple software serial ports, only one can receive data at a time.
 *  Not all pins on the Mega and Mega 2560 support change interrupts, so only the following can be used 
 *  for RX: 10, 11, 12, 13, 14, 15, 50, 51, 52, 53, A8 (62), A9 (63), A10 (64), A11 (65), A12 (66), 
 *  A13 (67), A14 (68), A15 (69).
 */
//  SoftwareSerial SerialRIMU( 10, 11 );   // RX, TX not using now
//  SoftwareSerial SerialLIMU( 12, 3 );    // RX, TX not using now
//  Serial1 pins 19(RX) 18(TX), Serial2 pins 17(RX) 16(TX), Serial3 pins 15(RX) 14(TX) 
  RoboClaw roboclawR( &Serial1,10000 );  

void setup() {
  pinMode (4, OUTPUT);      // left toe servo 
  pinMode (5, OUTPUT);      // right toe servo 
  pinMode (6, OUTPUT);      // left ankle servo
  pinMode (7, OUTPUT);      // right ankle servo
  pinMode (redLEDpin, OUTPUT);      //  heart beat led 
  pinMode( HipLeft, INPUT );       // limit switch hip right
  pinMode( HipRight, INPUT );       // limit switch hip left
  digitalWrite( redLEDpin, LOW);    // led off
  // roboclaw
  pinMode (18, OUTPUT);      // tx 1
  pinMode (19, INPUT);       // rx 1
  // gyro on base
  pinMode (16, OUTPUT);      // tx 2 
  pinMode (17, INPUT);       // rx 2
  // bluetooth
  pinMode (14, OUTPUT);      // tx 3 
  pinMode (15, INPUT);       // rx 3
// not using this way now
// gyro on right foot
//  pinMode(10, INPUT);        // Rx softserial
//  pinMode(11, OUTPUT);       // Tx softserial
// gyro on left foot
//  pinMode(12, INPUT);        // Rx softserial
//  pinMode(3, OUTPUT);        // Tx softserial

  Serial.begin( 57600 );        // terminal
  Serial2.begin( 38400 );       // IMUs on base and feet
  roboclawR.begin( 38400 );     // roboclaw serial 1 both legs and hips
//  SerialRIMU.begin( 19200 );  // IMU on right foot
//  SerialLIMU.begin( 19200 );  // IMU on left foot

//bluetooth can be ICstation 9600 or Sparkfun module defaults to 115200
  if( bluetooth == 1 )
    {
    Serial3.begin( 115200, SERIAL_8N1 );       
    InOut( "SparkFun bluetoth at 115200 RNBT-C96A key code 1234 on unit 3", 55, 'Y' );   
//    Serial3.print( "$" );             
//    Serial3.print( "$" );             
//    Serial3.print( "$" );             
//    delay( 100 );
//    Serial3.println( "U,9600,N" );       
//    Serial3.begin( 9600 );       
   }
  else if( bluetooth == 2 )
    {
    Serial3.begin( 9600, SERIAL_8N1 );       
    Serial3.println( "" );
    InOut( "ICstation bluetooth at 9600 HC-06 or BT-05 key code 1234", 55, 'Y' );    // original
    }
  else
    InOut( "no bluetooth", 55, 'Y'  );
      
  InOut(  " ",  55, 'Y' );
  InOut( "Leg Control ", 55, 'N'  );
  InOut( verDate, 55, 'Y' );

// servo setup pins for toes and rotation of ankles
  ToeServoR.attach( 5 ); 
  ToeServoL.attach( 4 ); 
  AnkleServoL.attach( 6 ); 
  AnkleServoR.attach( 7 ); 
  
/*  looking at QPPS again on Nov 10 spent most of day
 *  values from auto tuning in ion studio are being used
 *  SO NOT SETTING LISTED HERE!
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
 
  AllStop( 'N' );               // stop everything and 'R' = reset encoders
  Compass_Base( 'N' );          // dump compass data 
  Compass_Rfoot( 'N' );  
  Compass_Lfoot( 'N' );  
  while (Serial.available() > 0)  // clean out any characters in serial buffer at start up
      c = Serial.read();          // dump keys in dont need    
  sBuffer = "";                   // reset buffer for strings
}

void loop() 
{
  LedCnt ++;          // just a blinking led on mega heart
  if( LedCnt > 25 )
  {
    digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle red heart beat
    LedCnt = 0;
  }
  delay( 25 );
  TerminalIn();
  delay( 25 );
  BlueToothIn();
}

// check terminal for character in?
void TerminalIn () 
{ 
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

// check bluetooth for character in?
void BlueToothIn()
{
  if (Serial3.available () > 0)             
    {
    SignString = 1;     // positive number
    while (Serial3.available () > 0)        
      {
      delay (10);
      c = Serial3.read ();                    
      if (c == '\r')                  // look for end of line to exit
      {
        NumIn = inString.toInt();    // Convert readString into a number
        NumIn = constrain(NumIn, -12001, 12001);      // limit number

// next print lines for testing
        Serial3.print( ">" );         
        Serial3.println( sBuffer );   
        Serial.print( "B>" );         
        Serial.println( sBuffer );   
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
  }      // end if
}        // end bluetoothin

void ProcessCommand ()            
{
  if (sBuffer.length () > 0)
    {
    sBuffer.toUpperCase ();       
    if( sBuffer[0] == 'B' )        // bend down  
      BendDown();
    else if( sBuffer[0] == 'C' )   // read current
      DisAmps(); 
    else if( sBuffer[0] == 'D' )   // display encoder counts and speed data
    {
      roboclawR.clear();       
//      roboclawR.flush();       
      DisplaySpeed( 'D' );      // 1 turns on display
    }
    else if( sBuffer[0] == 'E' )  // errors and command buffer status
      WaitBuffer();      
    else if( sBuffer[0] == 'F' )  // stand on one foot
      LeftFoot();
    else if( sBuffer[0] == 'G' )  // gyro compass on base
      Compass_All( 'D' );     
    else if( sBuffer[0] == 'H' )  // find center for hips
      CenterHips( 'B' );          // B for both hips could do L for left or R for right
    else if( sBuffer[0] == 'I' )  // information on limit switches
      DisplayLmSwitch( 'D' );
    else if( sBuffer[0] == 'K' )  // both knees to home
    {
      KneeLeftLS();
      KneeRightLS();
    }
    else if( sBuffer[0] == 'L' )  // level feet
      LevelBothFeet();    
    else if( sBuffer[0] == 'N' )  // using number pad to control leg motors in small steps
      NumDrive();     
    else if( sBuffer[0] == 'S' )  // motors stop if 2nd char is R the encoders are reset
      AllStop( sBuffer[ 1 ] );     
    else if( sBuffer[0] == 'T' )  // test routine for figuring out pid values and delays
      TestPID();             
    else if( sBuffer[0] == 'U' )  // test routine for leveling foot
      TestLevelFoot();             
    else if( sBuffer[0] == 'W' )  // walk input number of steps to take
    {
      NumSteps = NumIn;
      if( NumSteps == 0 )
        NumSteps = 1;
      if( NumSteps > 10 )
        NumSteps = 10;
      InOut( "****** Total Steps =", NumSteps, 'Y' );
      for( NumStepsLeft=0; NumStepsLeft<NumSteps; NumStepsLeft++ )
      { 
        StepTurn = 0;
        Step();
      }      
    }
    else if( sBuffer[0] == 'X' )  // walk and turn input number of steps to take
    {
      NumSteps = NumIn;
      if( NumSteps == 0 )
        NumSteps = 1;
      if( NumSteps > 10 )
        NumSteps = 10;
      InOut( "****** Total Steps =", NumSteps, 'Y' );
      for( NumStepsLeft=0; NumStepsLeft<NumSteps; NumStepsLeft++ )
      { 
        StepTurn = 1;
        Step();
      }
    }      
    else if( sBuffer[0] == 'Z' )  // big test
    {
      InOut( "****** step ahead 3 times", 55, 'Y' );
      NumSteps = 3;
      StepTurn = 0;
      Step();
      NumSteps = 2;
      StepTurn = 0;
      Step();
      NumSteps = 1;
      StepTurn = 0;
      Step();
      InOut( "****** turn left 3 times", 55, 'Y' );
      NumSteps = 3;
      StepTurn = 1;
      Step();
      NumSteps = 2;
      StepTurn = 1;
      Step();
      NumSteps = 1;
      StepTurn = 1;
      Step();
    }

   else                               
      InOut( "?", 55, 'Y' );  // unknown input
  }
}

// uses knees and ankles to bend down, limit is plastic knee parts
void BendDown()
{
     int t;
     InOut( "***   bend knees & ankles, twist right/left", 55, 'Y' );
     DisplaySpeed(  'D'  );         // just to see where we start
     Compass_All( 'D' );
      
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000,7000,1);  // knee
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000,7000,1);  // knee
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000,-6000,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000,-6000,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x82,800,500,500,-1500,1); 
     roboclawR.SpeedAccelDeccelPositionM2(0x82,800,500,500,1500,1); 
     delay( 4000 );     // just see stop in between commands  
     WaitSpeed();       // wait for speed to be 0

     InOut( "***   twist to right", 55, 'Y' );
     for( t=1; t<60; t++ )  
     {
        RightToe = RightToe + 1;
        ToeServoR.write( RightToe );   
        ToeServoL.write( RightToe );   
        delay( 10 );          
     }
     delay( 1000 );
     Compass_All( 'D' );
     InOut( "***   twist to left", 55, 'Y' );
     for( t=1; t<60; t++ )  
     {
        RightToe = RightToe - 2;
        ToeServoR.write( RightToe );   
        ToeServoL.write( RightToe );   
        delay( 10 );          
     }
     delay( 1000 );
     Compass_All( 'D' );
     InOut( "***   twist back straight", 55, 'Y' );
     for( t=1; t<62; t++ )              // differance is slop in linkage
     {
        RightToe = RightToe + 1;
        ToeServoR.write( RightToe );   
        ToeServoL.write( RightToe );   
        delay( 10 );          
     }
     delay( 2000 );
     InOut( "****   straighten knees & ankles down", 55, 'Y' );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000,0,1); 
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000,0,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1700,4000,4000,0,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1700,4000,4000,0,1); 
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,0,1); // move left hip
     roboclawR.SpeedAccelDeccelPositionM2(0x82,1000,500,500,0,1); // move right hip 
     delay( 1000 );     
     WaitSpeed();       // wait for speed to be 0
     Compass_All( 'D' );
     InOut( "***   Kneel Done", 55, 'Y' );
}

// use base pitch to level feet
void LevelBothFeet()
{
  LevelLeftFoot();
  LevelRightFoot();
  Compass_All( 'D' );               // check pitch and show me
}

// set left foot to known absolute position 
void LevelLeftFoot()
{
     InOut( "***   level left foot, find limit switch", 55, 'Y' );
     roboclawR.BackwardM1( 0x81,70 );       // make ankle up address and speed
     WaitSpeed();             // wait for speed to be 0
     roboclawR.ResetEncoders( 0x81 );       // reset encoders left leg
     delay( 10 );                    
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000,7700,1); // move off switch was 8000 tried 7000 to much 7500
     WaitSpeed();                           // wait for speed to be 0
     roboclawR.ResetEncoders( 0x81 );       // reset encoders left leg
     InOut( "level done & reset", 55, 'Y' );
}

void LevelRightFoot()
{
     InOut( "***   level right foot, find limit switch", 55, 'Y' );
     roboclawR.BackwardM1( 0x80,70 );       // make ankle up address and speed
     WaitSpeed();                           // wait for speed to be 0
     roboclawR.ResetEncoders( 0x80 );       // reset encoders right leg
     delay( 10 );                    
     roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000,5500,1); // move off switch was 6000
     WaitSpeed();                           // wait for speed to be 0
     roboclawR.ResetEncoders( 0x80 );       // reset encoders right leg
     InOut( "level done & reset", 55, 'Y' );
}

// moving left knee to limit switch
void KneeLeftLS()
{
     InOut( "***   left  knee to ls", 55, 'Y' );
     roboclawR.BackwardM2( 0x81,100 );       // make knee straight address and speed
     delay( 1000 );
     WaitSpeed();             
     roboclawR.ResetEncoders( 0x81 );       // reset encoders left leg to move absolute
     delay( 10 );                    
     roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,2200,1); // move off switch
     WaitSpeed();                           // wait for speed to be 0
     roboclawR.ResetEncoders( 0x81 );       // reset encoders left leg
     InOut( "done on switch & reset", 55, 'Y' );
}

// moving right knee to limit switch updated feb 19
void KneeRightLS()
{
     InOut( "***   right knee to ls", 55, 'Y' );
     roboclawR.BackwardM2( 0x80,100 );     // make knee straight address and speed
     delay( 1000 );
     WaitSpeed();             
     roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg to move absolute
     delay( 10 );                    
     roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,2700,1); // move off switch
     WaitSpeed();                          // wait for speed to be 0
     roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
     InOut( "done on switch & reset", 55, 'Y' );
} 

void Step()    // takes around 22 sec per step Feb 21
{
     int t;
     InOut( "***   take a step ", NumStepsLeft, 'Y' );
     if( NumStepsLeft == 0 );           // first step show me info
     {
       DisplaySpeed( 'D' );               // let me know where we start
       Compass_All( 'D' );               // check pitch 
     }
     InOut( "*1*   ankle rotation right=", RightAnkleRot, 'N' );    // shift weight to right foot
     InOut( " & left=", LeftAnkleRot, 'Y');   
     for( t=1; t<58; t++ )                      // was 58
     {
        RightAnkleRot = RightAnkleRot - 1;      // remember position
        AnkleServoR.write( RightAnkleRot );     // rotating ankle but slowly
        delay( 15 );                            // tried 10 and body really rocks started with 20
        if( t == 25 )
        {
          InOut( "*2*   bend right knee & ankle a little leaning legs to right side", 55, 'Y' );
          roboclawR.SpeedAccelDeccelPositionM2(0x80,2400,2000,2000,1800,1);    // right knee
          roboclawR.SpeedAccelDeccelPositionM1(0x80,2400,2000,2000,-2000,1);   // right ankle  
        }
     }
     InOut( "*3*   ankle rotation right=", RightAnkleRot, 'N');    // shift weight to right foot
     InOut( " & left=", LeftAnkleRot, 'Y');   
                  
     InOut( "*4*   balanced on right leg & raise left leg a little so does not drag", 55, 'Y' ); 
     roboclawR.SpeedAccelDeccelPositionM2(0x81,2400,4000,4000,4000,1);    // left knee raise so does not touch floor
     delay( 500 );                                  
     WaitSpeed();

     if( StepTurn == 1 )
     {
     InOut( "*4a*   turn left", 55, 'N');    // turn left foot
      for( t=1; t<50; t++ )                  // started with count of 60
      {
        RightToe = RightToe + 1;
        ToeServoR.write( RightToe );   
        delay( 20 );          
      }
     }
     if( StepTurn == 2 )
     {
     InOut( "*4b*   turn right", 55, 'N');    // turn right foot
      for( t=1; t<50; t++ )  
      {
        RightToe = RightToe - 1;
        ToeServoR.write( RightToe );   
        delay( 20 );          
      }
     }
     Compass_All( 'D' );
         
     InOut( "*5*   straighten left knee & ankle, rotating left hip forward", 55, 'Y' );  
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1500,500,500,-500,1);    // hip
     roboclawR.SpeedAccelDeccelPositionM2(0x81,2400,2000,2000,-1000,0); // left knee
     roboclawR.SpeedAccelDeccelPositionM1(0x81,2400,2000,4000,1000,0);  // left ankle
     delay( 1000 );                                                     // 
     WaitSpeed();
       
     InOut( "*6*   roll ankles to left & bend left leg a little", 55, 'Y' ); 
     for( t=1; t<53; t++ )   
     {
        LeftAnkleRot = LeftAnkleRot + 1;          // this is starting at rest point
        AnkleServoL.write( LeftAnkleRot );
        RightAnkleRot = RightAnkleRot + 2;        // this has been angled over above so catch up
        AnkleServoR.write( RightAnkleRot );
        delay( 20 );                                   
        if( t == 25 )
        {
          InOut( "*7*   bend left knee & ankle", 55, 'Y' );
          roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,1800,0,1);  // knee left a little slower for motors
          roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,-2400,0,1); // ankle left 
        }
     }
     InOut( "*8*   ankle rotation right=", RightAnkleRot, 'N'); 
     InOut( " & left=", LeftAnkleRot, 'Y'); 

     InOut( "*9*   balanced on left leg", 55, 'Y' );
     WaitSpeed();  
       
     InOut( "*10*   raise right foot a little so it does not drag", 55, 'Y' );
     roboclawR.SpeedAccelDeccelPositionM2(0x80,2000,2000,2000,3500,1);    // right knee
     RightAnkleRot = RightAnkleRot - 52;
     AnkleServoR.write( RightAnkleRot );        // right ankle back flat
     InOut( "*10z*   ankle rotation right=", RightAnkleRot, 'N'); 
     InOut( " & left=", LeftAnkleRot, 'Y'); 
     WaitSpeed();    

     if( StepTurn == 1 )
     {
     InOut( "*10a*   turn right foot back & left foot turn left", 55, 'Y');    // turn foot back
      for( t=1; t<51; t++ )  
      {
        RightToe = RightToe - 1;
        ToeServoR.write( RightToe );
        LeftToe = LeftToe + 1;
        ToeServoL.write( LeftToe );   
        delay( 20 );          
      }
     }
    
     if( StepTurn == 2 )
     {
     InOut( "*10b*   turn right foot back left foot turn right", 55, 'N');    // turn foot back
     for( t=1; t<51; t++ )  
      {
        RightToe = RightToe + 1;
        ToeServoR.write( RightToe );   
        LeftToe = LeftToe - 1;
        ToeServoL.write( LeftToe );   
        delay( 20 );          
      }
     }    
     Compass_All( 'D' );

     InOut( "*11*   rotating right hip forward, left hip back then straighten right leg ", 55, 'Y' );
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1500,500,500,500,1);     // hip left
     roboclawR.SpeedAccelDeccelPositionM2(0x82,1500,500,500,700,1);     // hip right
     delay( 1000 );                               
     roboclawR.SpeedAccelDeccelPositionM1(0x80,2000,2000,2000,1000,1);  // ankle right
     roboclawR.SpeedAccelDeccelPositionM2(0x80,2000,2000,2000,0,1);     // knee right
     delay( 500 );
     roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,-1500,1); // ankle left bend up pushing right leg forward speed was 2000
     delay( 1000 );
     WaitSpeed();
     
     InOut( "*12*   straighten legs & hips", 55, 'Y' );
     roboclawR.SpeedAccelDeccelPositionM1(0x80,2000,2000,2000,0,0);    // ankle right
     roboclawR.SpeedAccelDeccelPositionM2(0x81,2000,2000,2000,0,0);    // knee left 
     roboclawR.SpeedAccelDeccelPositionM1(0x81,2000,2000,2000,0,0);    // ankle left
     delay( 1500 );                                                    // was 2000
     roboclawR.SpeedAccelDeccelPositionM1(0x82,1500,500,500,0,0);      // hip left
     roboclawR.SpeedAccelDeccelPositionM2(0x82,1500,500,500,0,0);      // hip right
     for( t=1; t<53; t++ )   
     {
        LeftAnkleRot = LeftAnkleRot - 1;
        AnkleServoL.write( LeftAnkleRot );
        delay( 20 );                            
     }
     InOut( "*13*   ankle rotation right=", RightAnkleRot, 'N');   
     InOut( " & left=", LeftAnkleRot, 'Y');    

     if( StepTurn == 1 )
     {
     InOut( "*13a*   turn left foot back", 55, 'N');    // trun foot back
      for( t=1; t<61; t++ )  
      {
        LeftToe = LeftToe - 1;
        ToeServoL.write( LeftToe );   
        delay( 20 );          
      }
     }
    
     if( StepTurn == 2 )
     {
     InOut( "*13b*   turn left foot back", 55, 'N');    // turn foot back
     for( t=1; t<51; t++ )  
      {
        LeftToe = LeftToe + 1;
        ToeServoL.write( LeftToe );   
        delay( 5 );          
      }
     }

     WaitSpeed();
     Compass_All( 'D' );               // check pitch and show me
     StepTurn = 0;                      // set back to straight ahead
     InOut( "*14*   Step Done ", NumSteps, 'Y' );
}

// testing level foot using IMU on foot
void TestLevelFoot()   
{
     InOut( "***   level right foot ", 55, 'Y' );
     Compass_Rfoot( 'D' );                // check pitch and show me seems to need to read once before starting
     int LevelAnkleR = RightAnkleCnt;
// loop here read gyro move motor read gyro move motor until level
     for( int q=1; q<20; q++ )            // loop is just a way to end so not stuck here forever
     {
       Compass_Rfoot( 'D' );              // check pitch and show me
       if( (RfootPitch > -2) && (RfootPitch < 2) )        // time to exit we are there must be -1 0 +1
       {
          InOut( "%%%   right ankle level", 55, 'Y' );
          goto StpLvR;           // just a way out of for loop
       }
// remember we are doing absolute position not realative so amount you add needs to get higher
       if( RfootPitch >1 )
         roboclawR.SpeedAccelDeccelPositionM1(0x80,2000,4000,4000,(LevelAnkleR + (400*q)),1 ); 
       if( RfootPitch <1 )
         roboclawR.SpeedAccelDeccelPositionM1(0x80,2000,4000,4000,(LevelAnkleR - (400*q)),1 ); 
       do
       {
         DisplaySpeed( 'S' );                   // dont need to see current speed just set vars
         aval = analogRead( AnalogPins[ 5 ] );  // check upper switch Right ankle  dont break something
         if( aval < 100 )
           roboclawR.BackwardM1( 0x80, 0x00 );  // stop left ankle into stop or switch
       } while( (RightAnkleSpd >5) || (RightAnkleSpd <-5) );  // looking for speed to be 0
     }         // end for loop
StpLvR:
     Compass_Rfoot( 'D' );
     DisplaySpeed( 'D' );      // dont need to see current speed just set vars
     InOut( "***   Done ", 55, 'Y' );
}

// just testing wait routines with IonStudio PID numbers
void TestPID()   
{
   int addr = 0x80;             // right leg
   int tstspd = 2500;           // speed for motor
   int tstaccl = 4000;
   int tstpos = 5000;           // position to go to
   InOut( "***   test position command right knee ", addr, 'N' );
   InOut( " ", tstspd, 'N' );
   InOut( " ", tstaccl, 'N' );
   InOut( " ", tstpos, 'Y' );
   AllStop( 'R' );       // reset encoders
   roboclawR.SpeedAccelDeccelPositionM2(0x80,tstspd,tstaccl,tstaccl,tstpos,1); //addr,speed start,accl,stop accl,pos,flag
   WaitSpeed();       // wait for speed to be 0
   InOut( "***  now back", 55, 'Y' );
   roboclawR.SpeedAccelDeccelPositionM2(0x80,tstspd,tstaccl,tstaccl,10,0);  // back to 0
   WaitBuffer();
   WaitSpeed();
   InOut( "***   test done", 55, 'Y' );
}

// lift left foot and stand on right foot adjusted for new right foot/ankle updated Feb.8 
// added looking at gyro for how much to angle ankle
void LeftFoot()   
{
      int t = 0;
      int tangle = 65;   // how much to angle the ankle
      InOut( "***   stand on left foot", 55, 'Y' );

      InOut( "***   bend right knee & ankle a little pushing over legs to right side", 55, 'Y' );   // this is needed removed does not work
      roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,2000,1);    // right knee 
      roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,-1800,1);  // right ankle 
      for( t=1; t<tangle; t++ )   
      {
        RightAnkleRot = RightAnkleRot - 1;
        AnkleServoR.write( RightAnkleRot );        // start position - amount which gets bigger in loop move servo
        delay( 20 );              // delay prevents jerking
      }
      InOut( "***   ankle rotation =", RightAnkleRot, 'Y' );
      delay( 1000 );
      WaitSpeed();        // waits till speed is 0
      Compass_All( 'D' );
     
      InOut( "***  bend left knee & ankle move left Hip Forward",55, 'Y' );
      roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,7200,1); // knee
      roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,-7000,1); // ankle
      roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,-400,1);    // hip      
      InOut( "***   should be balanced on right leg", 55, 'Y' );
      delay( 4000 );      // lets see standing on one foot
      WaitSpeed();        // waits till speed is 0
      
      InOut( "***   turn to left", 55, 'Y' );
      for( t=1; t<60; t++ )  
      {
        RightToe = RightToe + 1;
        ToeServoR.write( RightToe );   
        delay( 25 );          
      }
      delay( 1000 );            // delay for show
      Compass_All( 'D' );

      InOut( "***   turn back", 55, 'Y' );
      for( t=1; t<61; t++ )  
      {
        RightToe = RightToe - 1;
        ToeServoR.write( RightToe );   
        delay( 25 );          
      }
      delay( 1000 );
      Compass_All( 'D' );
 
      InOut( "***   straighten knees, ankles flat and Left Hip back", 55, 'Y' );
      roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,2000,2000,0,1);   // knee right 
      roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,2000,2000,0,1);   // knee left
      roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,2000,2000,0,1);    // ankle left
      roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,2000,2000,0,1);    // ankle right   
      roboclawR.SpeedAccelDeccelPositionM1(0x82,1000,500,500,0,1);      // hip left
      delay( 2700 ); // want leg to come down a little before rotating ankles
      for( t=1; t<tangle; t++ )  
      {
        RightAnkleRot = RightAnkleRot + 1;
        AnkleServoR.write( RightAnkleRot );
        delay( 60 );          
      }
      InOut( "***   ankle rotation = ", RightAnkleRot, 'Y' );
      WaitSpeed();
      Compass_All( 'D' );
      InOut( "*** Left Foot Done", 55, 'Y' );
}     // end left foot

// stops program and waits for a key input used for testing routines
void WaitKey()
{
    InOut( "- - - - - waiting for key input", 55, 'Y' );     // NumIn = to 1 skip waiting
    while (Serial.available() == 0) 
    {       
      digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle RED LED pin heart beat
      delay (100);
      digitalWrite(redLEDpin, digitalRead(redLEDpin) ^ 1);   // toggle RED LED pin heart beat
      delay (100);
    }
    c = Serial.read ();        // dump key in dont need     
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
    uint16_t reading = roboclawR.ReadError(0x80, &valid);
    InOut( "...   RoboClaw controller errors", 55, 'N' );
    InOut( " 80=", reading, 'N' );
    delay( 20 );
    reading = roboclawR.ReadError(0x81, &valid);
    InOut( " 81=", reading, 'N' );
    delay( 20 );
    reading = roboclawR.ReadError(0x82, &valid);
    InOut( " 82=", reading, 'Y' );
    delay( 20 );
    // The buffer value will be 0x80 if the motors are idle
    // number returned is how many commands are buffered waiting to run
    // Loop until command has completed 80=done 0=busy 1=one command waiting ect

    InOut( "...   RoboClaw buffers (128 means no commands in buffers", 55, 'Y' );
    do
    {
      roboclawR.clear();   
      roboclawR.ReadBuffers( 0x80, depth1, depth2 ); 
//      Serial.print( " 80=" );
//      Serial.print( depth1 );
//      Serial.print( "&" );
//      Serial.print( depth2 );
      i++;
      if( i >20 )
        goto Stop1;
      delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
    } while( depth1!=0x80 || depth2!=0x80 );
Stop1:
        InOut( "Bd.80=", depth1, 'N' );
        InOut( " &", depth2, 'N' );

    i = 0;
    do
    {
      roboclawR.clear();
      roboclawR.ReadBuffers( 0x81, depth1, depth2 );
//      Serial.print( " 81=" );
//      Serial.print( depth1 );
//      Serial.print( "&" );
//      Serial.print( depth2 );
      i++;
      if( i >20 )         // sometime hangs in these, so a way out
        goto Stop2;
      delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
    } while( depth1!=0x80 || depth2!=0x80 );  //Loop until command has completed 80=done 0=busy
Stop2:
        InOut( " Bd.81=", depth1, 'N' );
        InOut( " &", depth2, 'N' );
    i = 0;
    do
    {
      roboclawR.clear();
      roboclawR.ReadBuffers( 0x82, depth1, depth2 );
//      Serial.print( " 82=" );
//      Serial.print( depth1 );
//      Serial.print( "&" );
//      Serial.print( depth2 );
      i++;
      if( i >20 )
        goto Stop3;
     delay( 50 );  // need to wait atleast 10ms for the roboclaw to clear its packet buffer
   } while( depth1!=0x80 || depth2!=0x80 );  //Loop until command has completed 80=done 0=busy
Stop3:
        InOut( " Bd.82=", depth1, 'N' );
        InOut( " &", depth2, 'Y' );
}

// checks for speed to be stopped or limit switch active
void WaitSpeed()
{
    InOut( "...waiting", 55, 'Y' );
    delay( 1000 );               // time for motor to start before checking
    do
    {
      DisplaySpeed(  'S'  );   // get speed data but do not show me
    }while( AnySpeed == 1 );
    DisplaySpeed(  'D'  );      // show me speed data
}     // end speed

// shuts down all motors and homes servos on ankles
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
      InOut( "*** Motors at rest", 55, 'N' );   
      if( disp == 'R' )      // reset encoders ?
      {
        roboclawR.ResetEncoders( 0x80 );      // reset encoders right leg
        roboclawR.ResetEncoders( 0x81 );      // reset encoders left leg
        roboclawR.ResetEncoders( 0x82 );      // reset encoders hips
        InOut( " right/left leg & hip encoders reset", 55, 'N' );   
      }        
      InOut( " ", 55, 'Y' );   
}

// displays curent from motors
void DisAmps()
{
int currentFromMotorOne;
int currentFromMotorTwo;
uint8_t status1,status2,status3,status4;
bool valid1;
bool gotIt;
    gotIt = roboclawR.ReadCurrents( 0x80, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
     InOut( "*** Current in ma RghAnk:", currentFromMotorOne, 'N' );
     InOut( " & RghKne:", currentFromMotorTwo, 'N' );
   }
   gotIt = roboclawR.ReadCurrents( 0x81, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
     InOut( " LftAnk:", currentFromMotorOne, 'N');
     InOut( " & LftKne:", currentFromMotorTwo, 'N');
   }
   gotIt = roboclawR.ReadCurrents( 0x82, currentFromMotorOne, currentFromMotorTwo );
   if( gotIt )
   {
     InOut( " LftHip:", currentFromMotorOne, 'N');
     InOut( " & RghHip:", currentFromMotorTwo, 'Y');
   }
   
   long BatVolt = roboclawR.ReadMainBatteryVoltage( 0x80, &valid1 );
   if(valid1)
       InOut( "*** BatVoltage bd80:", ( BatVolt/10.0 ), 'N');
   BatVolt = roboclawR.ReadMainBatteryVoltage( 0x81, &valid1 );
   if(valid1)
       InOut( "   bd81:", ( BatVolt/10.0 ), 'N');
   BatVolt = roboclawR.ReadMainBatteryVoltage( 0x82, &valid1 );
   if(valid1)
       InOut( "   bd82:", ( BatVolt/10.0 ), 'Y');
}

// displays data from limit switches
void DisplayLmSwitch( char DispOff )
{
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
  LeftHipSw =  digitalRead( HipLeft );      // read limit switch on hip
  LeftKneeSw = analogRead( AnalogPins[ 2 ] ); // get raw number
  LeftAnkleSw = analogRead( AnalogPins[ 3 ] ); 
  RightHipSw = digitalRead( HipRight );
  RightKneeSw = analogRead( AnalogPins[ 4 ] ); // get raw number
  RightAnkleSw = analogRead( AnalogPins[ 5 ] ); 

  if( DispOff == 'D' )            // may want to check status but not show on display
  {
    InOut( " Switches Right Hip=", RightHipSw, 'N' );     
    InOut( " Kne=", RightKneeSw, 'N' );     
    InOut( " Ank=", RightAnkleSw, 'N' );     
    InOut( " Left Hip=", LeftHipSw, 'N' );     
    InOut( " Kne=", LeftKneeSw, 'N' );     
    InOut( " Ank=", LeftAnkleSw, 'Y' );      
  }       // end display off
}  // end display routine


// displays speed & encoder info
void DisplaySpeed( char DispOff )
{
  uint8_t status1,status2,status3,status4;
  bool valid1,valid2,valid3,valid4;
  AnySpeed = 0;
  roboclawR.clear();         
  address = 0x80;
  if( DispOff != 'S' )          // just want speed skip encoder position
  {
    RightAnkleCnt = roboclawR.ReadEncM1( address, &status1, &valid1);
    RightKneeCnt = roboclawR.ReadEncM2( address, &status2, &valid2);
    delay( 12 );
  }
  RightAnkleSpd = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  RightKneeSpd = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  if( RightAnkleSpd>5 || RightAnkleSpd<-5 )
    AnySpeed = 1;
  if( RightKneeSpd>5 || RightKneeSpd<-5 )
    AnySpeed = 1;
  if( DispOff == 'D' )            // may want to check status but not show on display
  {
   if(valid1)
     InOut( "  Encoder Right Ankle_M1:", RightAnkleCnt, 'N' );  
   if(valid2)
     InOut( " Knee_M2:", RightKneeCnt, 'N' );  
   if( valid3 )
     InOut( " Speeds Bd80 M1_RA", RightAnkleSpd, 'N' );  
   if( valid4 )
     InOut( " M2_RK", RightKneeSpd, 'Y' );  
  }  // end if
  roboclawR.clear();       
  address = 0x81;
  if( DispOff != 'S' )          // just want speed skip encoder position
  {
    LeftAnkleCnt = roboclawR.ReadEncM1( address, &status1, &valid1);
    LeftKneeCnt = roboclawR.ReadEncM2( address, &status2, &valid2);
    delay( 12 );
  }
  LeftAnkleSpd = roboclawR.ReadSpeedM1( address, &status3, &valid3);
  LeftKneeSpd = roboclawR.ReadSpeedM2( address, &status4, &valid4);
  if( LeftAnkleSpd>5 || LeftAnkleSpd<-5 )
    AnySpeed = 1;
  if( LeftKneeSpd>5 || LeftKneeSpd<-5 )
    AnySpeed = 1;
 if( DispOff == 'D' ) 
 {
   if(valid1)
    InOut( "  Encoder Left Ankle_M1:", LeftAnkleCnt, 'N' );  
   if(valid2)
    InOut( " Knee_M2:", LeftKneeCnt, 'N' );  
   if( valid3 )
    InOut( " Speeds Bd81 M1_LA", LeftAnkleSpd, 'N' );  
   if( valid4 )
     InOut( " M2_LK", LeftKneeSpd, 'Y' );  
 }
  roboclawR.clear();       
  address = 0x82;
  if( DispOff != 'S' )          // just want speed skip encoder position
  {
    RightHipCnt = roboclawR.ReadEncM2( address, &status1, &valid1);
    LeftHipCnt = roboclawR.ReadEncM1( address, &status2, &valid2);
    delay( 12 );
  }
  RightHipSpd = roboclawR.ReadSpeedM2( address, &status3, &valid3);
  LeftHipSpd = roboclawR.ReadSpeedM1( address, &status4, &valid4);
  if( RightHipSpd>5 || RightHipSpd<-5 )
    AnySpeed = 1;
  if( LeftHipSpd>5 || LeftHipSpd<-5 )
    AnySpeed = 1;
 if( DispOff == 'D' )       
 {
   if(valid1)
    InOut( "  Encoder Hips Left_M1:", LeftHipCnt, 'N' );  
   if(valid2)
    InOut( " Rgh_M2:", RightHipCnt, 'N' );  
   if( valid3 )
    InOut( " Speeds Bd82 M1_RH", LeftHipSpd, 'N' );  
  if( valid4 )
    InOut( " M2_LH", RightHipSpd, 'Y' );  
 }       // end display off
}        // end display routine

// trying to get hip motors to be at same spot
// hard to do as the legs hanging in the air have momentom when stopping
void CenterHips( char hipp )    
  {
  InOut( "***   Center Hips", 55, 'Y' );
  InOut( "find limit switch right hip", 55, 'Y' );
  while ( (digitalRead( HipRight )) == HIGH )
  {
     Serial.print( "#" );  
     roboclawR.ForwardM2( 0x82, 100 ); // max 127 for speed
     delay( 80 );                     // how long to have motor on
     roboclawR.ForwardM2( 0x82, 0 );  // motor off
     delay( 70 ); 
  } 
  Serial.println( " " );
  
  InOut( "find limit switch left  hip", 55, 'Y' );
  while ( (digitalRead( HipLeft )) == HIGH )
  {
     Serial.print( "&" );  
     roboclawR.BackwardM1( 0x82, 100 );  // max speed 127
     delay( 80 );                    
     roboclawR.BackwardM1( 0x82, 0 );  
     delay( 70 ); 
  }     
  Serial.println( " " );
//  WaitKey();

// want platform to be more level and then reset encoders  
  roboclawR.ResetEncoders( 0x82 );      // reset encoders hips
  delay( 1000 );
  roboclawR.SpeedAccelDeccelPositionM1(0x82,800,1000,1000,-850,1);   // left forward is minus value used to be -250
  delay( 1000 );
  roboclawR.SpeedAccelDeccelPositionM2(0x82,800,1000,1000,250,1);  // right forward is plus value
  delay( 3000 ); 
  roboclawR.ResetEncoders( 0x82 );      // reset encoders hips
  DisplaySpeed(  'D'  );        // show me encoders
  RightHipCnt = 0;
  LeftHipCnt = 0;       
  InOut( "***   hips done", 55, 'Y' );
 }    // end center hips

int smoothSensorReadings(int datatoavg)
{
// We remove the oldest value from the buffer
  sensorDataCircularSum = sensorDataCircularSum - circularBuffer[indexBuffer];
  circularBuffer[indexBuffer] = datatoavg;  // new input from the sensor is placed in the buffer
  sensorDataCircularSum += datatoavg;       // added to the total sum of the buffer
  indexBuffer++;                        // increment pointer
  if( indexBuffer == BUFFER_SIZE )
    indexBuffer = 0;                    // end of the buffer?
  filteredOutput=( sensorDataCircularSum/BUFFER_SIZE );  // output mean value of the circular buffer
  return filteredOutput;
}

void Compass_All( char dispp )
{
  Compass_Base( dispp );
  Compass_Rfoot( dispp );
  Compass_Lfoot( dispp );
}


// reads the 9 axis sensor on left foot
void Compass_Base( char dispp )
{
  int StartChar;
  String tempstr = " ";

  while (Serial2.available () > 0)      // clean out any data
  {
    delay( 1 );                  
    c = Serial2.read ();     
  }            

  Serial2.print( "1" );             // request data from compass
  sBuffer = " ";
  delay( 30 );                  // thinking about delay here at 38,400 baud a bit is 26us or char is 10 * that or .26ms
  while (Serial2.available () > 0)      
  {
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
  BaseRoll = tempstr.toInt( );

  StartChar = sBuffer.indexOf( 'P' );     // pitch
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  BasePitch = (tempstr.toInt( ) );   
  
  StartChar = sBuffer.indexOf( 'Y' );     // yaw
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  BaseYaw = tempstr.toInt( );
  
  if( dispp == 'D' ) 
  {  
    InOut( "$$$   Base R:", BaseRoll, 'N' );  
    InOut( " P:", BasePitch, 'N' );    
    InOut( " Y:", BaseYaw, 'Y' );  
  }  
}     // end compass

// reads the 9 axis sensor on left foot
void Compass_Rfoot( char dispp )
{
  int StartChar;
  String tempstr = " ";

  while (Serial2.available () > 0)      // clean out any data
  {
    delay( 1 );                  
    c = Serial2.read ();     
  }            


  Serial2.print( "2" );             // request data from compass
  sBuffer = " ";
  delay ( 30 );                  // thinking about delay here at 38,400 baud a bit is 26us or char is 10 * that or .26ms
  while (Serial2.available () > 0)      
  {
      c = Serial2.read ();                 
      if (c == '\r')  
      {
//        Serial.println( sBuffer ); // Echo captured string for testing
        break;
      }
      sBuffer += c;                  // make string
  }
  StartChar = sBuffer.indexOf( 'R' );     // roll
  tempstr = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootRoll = tempstr.toInt( );

  StartChar = sBuffer.indexOf( 'P' );     // pitch
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootPitch = (tempstr.toInt( ) );     
  
  StartChar = sBuffer.indexOf( 'Y' );     // yaw
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootYaw = tempstr.toInt( );
  
  if( dispp == 'D' ) 
  {  
    InOut( "$$$   R_Ft R:", RfootRoll, 'N' );  
    InOut( " P:", RfootPitch, 'N' );    
    InOut( " Y:", RfootYaw, 'Y' );  
  }  
}     // end compass

 
// reads the 9 axis sensor on left foot
void Compass_Lfoot( char dispp )
{
  int StartChar;
  String tempstr = " ";

  while (Serial2.available () > 0)      // clean out any data
  {
    delay( 1 );                  
    c = Serial2.read ();     
  }            

  Serial2.print( "3" );             // request data from compass
  sBuffer = " ";
  delay ( 30 );                  // thinking about delay here at 38,400 baud a bit is 26us or char is 10 * that or .26ms
  while (Serial2.available () > 0)      
  {
      c = Serial2.read ();                 
      if (c == '\r')  
      {
//        Serial.println( sBuffer ); // Echo captured string for testing
        break;
      }
      sBuffer += c;                  // make string
  }
  StartChar = sBuffer.indexOf( 'R' );     // roll
  tempstr = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootRoll = tempstr.toInt( );

  StartChar = sBuffer.indexOf( 'P' );     // pitch
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootPitch = (tempstr.toInt( ) );      
  
  StartChar = sBuffer.indexOf( 'Y' );     // yaw
  tempstr  = sBuffer.substring( (StartChar+1),(StartChar+4) );
  RfootYaw = tempstr.toInt( );
  
  if( dispp == 'D' ) 
  {  
    InOut( "$$$   L_Ft R:", RfootRoll, 'N' );  
    InOut( " P:", RfootPitch, 'N' );    
    InOut( " Y:", RfootYaw, 'Y' );  
  }  
}     // end compass


void InOut( String msg, float num, char newline )
{
  Serial.print( msg );
  Serial.print( " " );
  if( num != 55 )
    Serial.print( num,0 );      // added 1 digit decimal point this shows up every place
  if( newline == 'Y' )
    Serial.println( "" );
  if( bluetooth > 0 )
    {
    Serial3.print( msg );
    Serial3.print( " " );
    if( num != 55 )
      Serial3.print( num,2 );
    if( newline == 'Y' )
      Serial3.println( "" );
    }
}

 // control platform by keypad numbers  manual mode for motors    working Jan 29 changed to position control
void NumDrive()
{
  int Rlast = RightAnkleRot;               // starting place for ankle servos
  int Llast = LeftAnkleRot;               
  int FlastR = RightToe;                    
  int FlastL = LeftToe;                    
  int SpdHip = 500;
  InOut( "Number Pad Control ", (sBuffer[ 1 ]), 'Y' );  
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
          InOut( "Upper Left Leg straight",LeftKneeCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000, (LeftKneeCnt-500) ,1);  // left knee
        }
        if( swleg == 2 )           // right knee testing
        {
          InOut( "Upper Right Leg straight", RightKneeCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000, (RightKneeCnt-500) ,1);  // right knee
        }
        if( swleg == 3 )          // toe testing
        {
          FlastL = FlastL + 5;
          ToeServoL.write( FlastL );
          Serial.print( "turn left foot" );                     
          Serial.println( FlastL );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          Rlast = Rlast + 5;
          AnkleServoR.write( Rlast );
          InOut( "right ankle rotate to left (count up)", Rlast, 'Y' );                     
        }
        if( swleg == 5 )          // hip rotation testing
        {
          InOut( "Right Hip Back", RightHipCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x82,SpdHip,2000,2000, (RightHipCnt-300) ,1); // right hip
        }
        break;    
    }
      
    case '2':
    {
        if( swleg == 1 )           // left knee testing
        {
          InOut( "Upper Left Leg bend", LeftKneeCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x81,1500,4000,4000, (LeftKneeCnt+500) ,1);  // left knee
        }
        if( swleg == 2 )           // right knee testing
        {
          InOut( "Upper Right Leg bend", RightKneeCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x80,1500,4000,4000, (RightKneeCnt+500) ,1);  // right knee
        }
        if( swleg == 3 )          // toe testing
        {
          FlastL = FlastL - 5;
          ToeServoL.write( FlastL );
          Serial.print( "turn left foot " );                     
          Serial.println( FlastL );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          Rlast = Rlast - 5;
          AnkleServoR.write( Rlast );
          InOut( "right ankle rotate to right (count down)", Rlast, 'Y' );                     
        }
       if( swleg == 5 )          // hip rotation testing
        {
          InOut( "Right Hip Forward", RightHipCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM2(0x82,SpdHip,2000,2000, (RightHipCnt+300) ,1); // right hip
        }
        break;   
    }
        
    case '4':
    {
        if( swleg == 1 )          // left ankle up testing
        {
          InOut( "left foot down", LeftAnkleCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000, (LeftAnkleCnt+500) ,1);  // left ankle
        }
        if( swleg == 2 )           // right ankle up testing
        {
          InOut( "right foot down", RightAnkleCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000, (RightAnkleCnt+500) ,1);  // right ankle
        }                 
        if( swleg == 3 )          // toe testing
        {
          FlastR = FlastR + 5;
          ToeServoR.write( FlastR );
          Serial.print( "turn right foot" );                     
          Serial.println( FlastR );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          Llast = Llast - 5;
          AnkleServoL.write( Llast );
          InOut( "left ankle rotate to left (count down)", Llast, 'Y' );                     
        }
        if( swleg == 5 )          // hip rotation testing
        {
          InOut( "Left Hip Forward", LeftHipCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x82,SpdHip,2000,2000, (LeftHipCnt+300) ,1 ); // move left hip 
        }
        break;           
    }
      
    case '6':
    {
        if( swleg == 1 )
        {
          InOut( "left foot up", LeftAnkleCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x81,1500,4000,4000, (LeftAnkleCnt-500) ,1) ;  // left ankle
        }
        if( swleg == 2 )
        {
          InOut( "right foot up", RightAnkleCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x80,1500,4000,4000, (RightAnkleCnt-500) ,1 );  // right ankle
        }
        if( swleg == 3 )          // toe testing
        {
          FlastR = FlastR - 5;
          ToeServoR.write( FlastR );
          Serial.print( "trun right foot " );                     
          Serial.println( FlastR );
        }
        if( swleg == 4 )          // ankle rotation testing
        {
          Llast = Llast + 5;
          AnkleServoL.write( Llast );
          InOut( "left ankle rotate to right (count up)", Llast, 'Y' );
        }                   
        if( swleg == 5 )          // hip rotation testing
        {
          InOut( "Left Hip Back", LeftHipCnt, 'Y' );                     
          roboclawR.SpeedAccelDeccelPositionM1(0x82,SpdHip,2000,2000, (LeftHipCnt-300) ,1 ); // move left hip 
        }
        break;           
    }
      
    case '5':
    {
      DisplaySpeed(  'D'  );      // read encoders and update variables
      DisplayLmSwitch( 'D' );
      Compass_All( 'D' );
      break;           
    }
      
    case '0':
    {
        goto NumStop;                    
        break;           
    }
  }   // end case statement
    
  delay( 500 );         // hip rotation testing
  c = '0';
  DisplaySpeed(  'N'  );      // read encoders and update variables
  goto NumRepeat;
  }
NumStop:
  roboclawR.BackwardM1( 0x80, 0x00 );  // stop right ankle
  roboclawR.BackwardM2( 0x80, 0x00 );  // stop right knee
  roboclawR.BackwardM1( 0x81, 0x00 );  // stop right ankle
  roboclawR.BackwardM2( 0x81, 0x00 );  // stop right knee
  roboclawR.BackwardM1( 0x82, 0x00 );  // stop right hip
  roboclawR.BackwardM2( 0x82, 0x00 );  // stop right hip
  InOut( "*** exit keypad", 55, 'Y' );               
}

