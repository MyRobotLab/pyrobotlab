/*
Platform5.ino  for azul mobile platform
which has:
parallax pings
i/r sensors
servo motor drivers
beacon sensor
compass HMC5883L
 */

#include <Wire.h>
#include <SPI.h>
#include <HMC5883L.h>
HMC5883L compass;
#include <Servo.h>
Servo servoR; // create servo object to control a servo
Servo servoL; // create servo object to control a servo
#include <SoftwareSerial.h>
//lots of testing for the correct port address and pins on
//tinker mega board no documentation could be found UHG! wasted hours
SoftwareSerial LedSerial(17, 16); // RX2=17 and TX2=16, RX1=19 and TX1=18, RX3=15 and TX3=14

String serdata = "";
// I/R sensors data  turns out this data is not very good
int distcen = 0;
int distright = 0;
int distleft = 0;
// ping sensors left and right  info very good
int DistPingRight = 0;
int DistPingLeft = 0;
// compass data
float headingDegrees = 0;     
// input routine
String cmd;
String sBuffer = "";
String sResp = "?";
String verDate = "ver May 11,2016";
// motors are controlled like servo
int OldSpeed = 90;   // storage of last speed for stopping
int speed = 90;
int wheeloffsetR = 0;   // try to adjust for different speed motors
int wheeloffsetL = 0;	// right motor seems slower not going straight
		
int AnalogPinCount = 5;     // number of channels in use
const int AnalogPins [] = 
{
  0,  // back center i/r sensor higher number is closer above 400 around 12 inches
  1,  // front right i/r sensor
  2,  // front left  i/r sensor
  3,  // battery voltage 14.8v= 1008cnt and 12.7v=865cnt
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
};

int OutputPinCount = 4;     // number of channels in use
const int MaOutputPins [] = 
{
  4,   // servo motor wheel right
  2,   // servo motor wheel left
  3,
  5,
  6,
  7,   // ping right rear
  8,   // ping left rear
  9,
  10,
  11,  // ping center front
  12,  // ping left front
  13,  // ping right front
};

int PingPinCount = 5;     // number of channels in use
const int PingPin [] = 
{
  7,   // ping rear right
  8,   // ping rear left
  11,  // ping front center
  12,  // ping front left
  13,  // ping front right
};


// could calculate this by #define OutPinCount (sizeof (MaOutputPins) / sizeof (MaOutputPins [0]))

void setup()
{
  int i;
  for (i = 0; i < OutputPinCount; i++)
  {
    pinMode (MaOutputPins [i], OUTPUT);     // set to output mode
    digitalWrite (MaOutputPins [i], LOW);  // set chip enable off
  }
// setup SPI channel
// SPI.begin();         		            // wake up the SPI bus.
// SPI.setBitOrder(MSBFIRST);  	      // wants data most significant byte first
// SPI.setDataMode(SPI_MODE3);          //  Set for clock rising edge
// SPI.setClockDivider(SPI_CLOCK_DIV64);    //  Set clock divider (optional)
// servo setup pins
  servoR.attach(MaOutputPins [0]); 
  servoL.attach(MaOutputPins [1]); 
  Wire.begin();                        // Start the I2C interface.
  compass = HMC5883L();                // Construct a new HMC5883 compass.
  setupHMC5883L();                    //setup the HMC5883L
  LedSerial.begin(38400);            // separate board that controls lights
//LedSerial.begin(2400);            // separate board that controls lights for testing lower
  LedSerial.print( "!DC16");     // start command for DC-16 board
  LedSerial.print( '\0' );        // board address need null chacter
  LedSerial.print( "X");       // X is all off for lights
  Serial.begin (57600);             // setup Serial port at 57,600 baud
  Serial.println(verDate);
}
// main loop only watches serial input
void loop() 
{
  char c;
  if (Serial.available () > 0)
  {
    while (Serial.available () > 0)
    {
      delay (10);
      c = Serial.read ();
      if (c == '\r')
      {
        ProcessCommand ();
        sBuffer = "";
        continue;
      }
      sBuffer += c;             // make string
    }
  }
//  delay (50);
}

void ProcessCommand ()
{
  sResp = " ";                    // may use this later
  if (sBuffer.length () > 0)
  {
    sBuffer.toUpperCase ();
//    Serial.println(sBuffer);
    switch (sBuffer [0])            // look at first character in string
    {             
      case 'A':
        ReadAnalog();        
        break;
      case 'P':
        ReadPing();        
         break;
      case 'C':
        ReadCompass();        
        break;
      case 'F':         // go forward with speed number
 //       Serial.println("Fwd");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
           speed = 12;
        }
        MrtFwd( speed );        
        break;
      case 'B':         // go backward with speed number
//        Serial.println("Bck");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          speed = 12;
        }
        MrtRev( speed );        
        break;
      case 'W':         // go backward look at rear sensors
//        Serial.println("Bck sensors");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          speed = 12;
        }
        MoveRev( speed );        
        break;
      case 'R':         // turn right
//        Serial.println("Rgh");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          speed = 12;
        }
        TurnRight( speed );        
        break;
      case 'G':       // lights and light board which is a Parallax DC16 input on white wire hook to tx out on mega
        LedsOnOff();
        break;
      case 'L':         // turn left
//        Serial.println("Lft");
        ProcessRestCmd (sBuffer.substring (1));
       if (speed > 55){
          speed = 12;
        }
        TurnLeft( speed );        
        break;
      case 'M':         // move forward looking at sensors
//        Serial.println("fwd sensors");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          speed = 12;
        }
        MoveFwd( speed );        
        break;
      case 'N':         // find north
//        Serial.println("find North");
        North( speed );        
        break;
      case 'Q':         // run square pattern
//        Serial.println("square");
        ProcessRestCmd (sBuffer.substring (1));
       if (speed > 10){
          speed = 2;
        }
        Square( speed );        
        break;
      case 'S':
//        Serial.println("Stp");
        MrtStop();        
        break;
      case 'T':
//        Serial.println("rightwheel offset +");
        wheeloffsetR = wheeloffsetR + 1;        
        break;
      case 'U':
//        Serial.println("rightwheel offset -");
        wheeloffsetR = wheeloffsetR - 1;        
        if (wheeloffsetR < 1){
          wheeloffsetR = 0;
          }
        break;
      case 'X':
//        Serial.println("leftwheel offset +");
        wheeloffsetL = wheeloffsetL + 1;        
        break;
      case 'Y':
//        Serial.println("leftwheel offset -");
        wheeloffsetL = wheeloffsetL - 1;        
        if (wheeloffsetL < 1){
          wheeloffsetL = 0;
          }
        break;
     case '?':
        Serial.println(verDate);
        Serial.println("P ping distance readings ");
        Serial.println("A analog readings ");
        Serial.println("C compass");
        Serial.println("F forward motors 0 to 50 ");
        Serial.println("B reverse motors 0 to 50 ");
        Serial.println("R turn right 0 to 50");
        Serial.println("L turn left 0 to 50");
        Serial.println("S stop");
        Serial.println("G lights");
        break;
    }
//  Serial.println (sResp);           // Prompts
  Serial.println (">");  
  }
}

void ProcessRestCmd (String NumCmd)
{
  long speed1;
  speed1 = NumCmd.toInt ();
  speed = (speed1);                    // save number int
//  Serial.println(speed); 
}

void ReadAnalog(){
 int reading;                        // reading from a to d 
 float voltage;                       // voltage calculated from a to d
 for (int x=0; x < (AnalogPinCount-1); x++){
   reading = analogRead(AnalogPins[x]);        // get raw number
   Serial.print("A"); 
   Serial.print(x);
   Serial.print("=");
   Serial.print(reading);         // show raw number
   Serial.print(",");
   if (x == 3){
     voltage = reading * 5.0;
     voltage /= 1024.0; 
     voltage = 0.014159 * reading;        // 5 / 1024 = .00488
     Serial.print("v");
     Serial.print(voltage);         // show voltage calculated, sortof right
     Serial.print(", ");
   }
 }
 Serial.println();
}

void LedsOnOff(){
// test lights and light board which is a Parallax DC16 input on white wire hook to tx out on mega
//        Serial.println("Led");
        ProcessRestCmd (sBuffer.substring (1));
        if (speed == 1 ){                       // left side of face
          LedSerial.print( "!DC16" );  // board cmd
          LedSerial.print(  '\0' );     // board address
          LedSerial.print( "L" );      // low bits on 
          LedSerial.print( B10000000 );  
        }
        if (speed == 2){              // top center of head, all of face
          LedSerial.print( "!DC16" );  // board cmd
          LedSerial.print(  '\0' );     // board address
          LedSerial.print( "L" );      // high bits on
          LedSerial.print( B01000000 );  
        }
        if (speed == 3){
          LedSerial.print( "!DC16" );  // board cmd
          LedSerial.print(  '\0' );     // board address
          LedSerial.print( "L" );      // low bits on 
          LedSerial.print( B00100000 );  
        }
        if (speed == 4){
        LedSerial.print( "!DC16" );  // board cmd
        LedSerial.print(  '\0' );     // board address
        LedSerial.print( "L" );      // high bits on
        LedSerial.print( B00010000 );  
        }
        if(speed == 5){               // green eye
        LedSerial.print( "!DC16" );  // board cmd
        LedSerial.print(  '\0' );     // board address
        LedSerial.print( "L" );      // low bits on
        LedSerial.print( B00001000 );  
        }
        if (speed == 6){            // right side of face
        LedSerial.print( "!DC16" );  // board cmd
        LedSerial.print(  '\0' );     // board address
        LedSerial.print( "L" );      // low bits on
        LedSerial.print( B00000100 );  
        }
        if (speed == 7){
        LedSerial.print( "!DC16" );  // board cmd
        LedSerial.print(  '\0' );     // board address
        LedSerial.print( "L" );      // high bits on
        LedSerial.print( B00000010 );  
        }
        if (speed == 8){
        LedSerial.print( "!DC16" );  // board cmd
        LedSerial.print(  '\0' );     // board address
        LedSerial.print( "L" );      // low bits on
        LedSerial.print( B00000001 );  
        }
        if(speed == 9){               // green eye wink
          for (int x=0; x<3; x++){
            LedSerial.print( "!DC16" );  // board cmd
            LedSerial.print(  '\0' );     // board address
            LedSerial.print( "L" );      // low bits on
            LedSerial.print( B00001000 );  
            delay(300);                  // delay is in ms
            LedSerial.print( "!DC16" );  // board cmd
            LedSerial.print(  '\0' );     // board address
            LedSerial.print( "X" );      // all off
            delay(300);                  // delay is in ms
            }
        }
        if (speed == 10 ){               // left and right side of face does not work
            LedSerial.print( "!DC16" );  // board cmd
            LedSerial.print(  '\0' );    // board address
            LedSerial.print( "TA" );      // toggle all
       }
        if (speed == 0){                  // all off
          LedSerial.print( "!DC16" );  // board cmd
          LedSerial.print(  '\0' );     // board address
          LedSerial.print( "X" );      // high bits on
        }
}

void ReadPing(){
  long duration, inches, cm;

 for (int x=0; x < PingPinCount; x++){
  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(PingPin[x], OUTPUT);
  digitalWrite(PingPin[x], LOW);
  delayMicroseconds(2);
  digitalWrite(PingPin[x], HIGH);
  delayMicroseconds(5);
  digitalWrite(PingPin[x], LOW);
  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(PingPin[x], INPUT);
  duration = pulseIn(PingPin[x], HIGH);
  // convert the time into a distance
  inches = microsecondsToInches(duration);
  Serial.print("P");
  Serial.print(x);
  Serial.print("=");
  Serial.print(inches);
  Serial.print(",");
//  Serial.print("in, ");
 }
  Serial.println();
}

long microsecondsToInches(long microseconds) {
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  return microseconds / 74 / 2;
}

void ReadCompass(){
  MagnetometerScaled scaled = compass.ReadScaledAxis();
  int MilliGauss_OnThe_XAxis = scaled.XAxis;
  float heading = atan2(scaled.YAxis, scaled.XAxis);
  float declinationAngle = 0.0457;
  heading += declinationAngle;
  if(heading < 0)
    heading += 2*PI;
  if(heading > 2*PI)
    heading -= 2*PI;
  headingDegrees = heading * 180/M_PI; 
  Serial.print("C0="); 
  Serial.println(headingDegrees);
//  delay(500);     
}

void Output(float headingDegrees)
{
   Serial.print("Head Deg=");
   Serial.print(headingDegrees);
   Serial.println("\t");
}

void setupHMC5883L(){
  //Setup the HMC5883L, and check for errors
  int error;  
  error = compass.SetScale(1.3); //Set the scale of the compass.
  if(error != 0) Serial.println(compass.GetErrorText(error)); //check if there is an error, and print if so

  error = compass.SetMeasurementMode(Measurement_Continuous); // Set the measurement mode to Continuous
  if(error != 0) Serial.println(compass.GetErrorText(error)); //check if there is an error, and print if so
}

void MrtStop(){                     // motors stop at 90
      while(OldSpeed > 90){         // want slow stop
        speed = OldSpeed - 1;
        OldSpeed = speed;
        servoR.write(speed);               
        servoL.write(speed); 
        delay(50);  
//        Serial.println(speed);   // make sure working right
      }            
      while(OldSpeed < 90){     
        speed = OldSpeed + 1;
        OldSpeed = speed;
        servoR.write(speed);               
        servoL.write(speed);   
        delay(40);		   // timing for slow speed slowdown
//        Serial.println(speed);   // make sure working right
      }
      servoR.write(90);            // all stop for sure    
      servoL.write(90);             
}

void MrtFwd( int speed ){ 
     OldSpeed = speed + 90;           //storing for stopping             
     servoR.write(90 + speed + wheeloffsetR);   // try to adjust for different speed motors
     servoL.write(90 + speed + wheeloffsetL);          
}

void MoveRev( int speed ){   
     OldSpeed = 90 - speed;          //storing for stopping        
//     servoR.write(90 - speed + wheeloffsetR);               
//     servoL.write(90 - speed + wheeloffsetL);     
     servoR.write(90 - speed);               
     servoL.write(90 - speed);     
     int ir0=100;
     while( ir0<400 ){                // numbers get bigger as you get closer
        ir0 = analogRead(AnalogPins[0]);        // check i/r sensor back
        delay(50);
     }
//      ReadAnalog();        // just checking to see if working
      MrtStop();  
}

void MrtRev( int speed ){   
     OldSpeed = 90 - speed;          //storing for stopping         
     servoR.write(90 - speed);               
     servoL.write(90 - speed);     
}

void MoveFwd( int speed ){ 
     OldSpeed = speed + 90;           //storing for stopping             
     servoR.write(90 + speed + wheeloffsetR);        
     servoL.write(90 + speed + wheeloffsetL);    
     int ir1=100;
     int ir2=100;
     while( (ir1<400) && (ir2<400) ){ 
        ir1 = analogRead(AnalogPins[1]);        // check i/r sensors front 1,2
        delay(25);
        ir2 = analogRead(AnalogPins[2]);     
        delay(25);
     }
//      ReadAnalog();        // just checking to see if working
      MrtStop();  
}

void TurnLeft( int speed ){              
     servoR.write(90 - speed);               
     servoL.write(speed + 90);   
}     

void TurnRight( int speed ){          
     servoR.write(speed + 90);               
     servoL.write(90 - speed);     // reverse direction         
}

void North( int speed ){        // move to north pointing direction
  ReadCompass();		// get current heading
  int adjheading = 360 - headingDegrees;	// amount to turn in degrees
  Serial.println(adjheading);  
  while( adjheading > 5 ){
     servoR.write(12 + 90);     // wheels move speed       
     servoL.write(90 - 12);     // reverse direction of 2nd wheel so spins in place
     delay(155);	        // how long wheels turn  adjust for 5 degree per count
     if(adjheading < 6){
       adjheading = 0;
       }
     else{
       adjheading = adjheading - 5;
       Serial.println(adjheading);  
       }
     }
  servoR.write(90);             // all stop  
  servoL.write(90);         
  delay( 200 );
  ReadCompass();		// get current heading see if there
// get closer  
  adjheading = 360 - headingDegrees;	// amount to turn in degrees
  Serial.println(adjheading);  
  while( adjheading > 2 ){
     servoR.write(10 + 90);     // wheels move speed       
     servoL.write(90 - 10);     // reverse direction of 2nd wheel so spins in place
     delay(85);	        // how long wheels turn  adjust for 5 degree per count
     if(adjheading < 2){
       adjheading = 0;
       }
     else{
       adjheading = adjheading - 2;
       Serial.println(adjheading);  
       }
     }
  servoR.write(90);             // all stop  
  servoL.write(90);         
  ReadCompass();		// get current heading see if there
}

void Square( int speed ){  
  int ir1=100;
  int ir2=100;
  int cnt=0;
  for (int x=0; x < 4; x++){		// each side of square
    while( (ir1<400) && (ir2<400) && (cnt < speed)){ 
      ir1 = analogRead(AnalogPins[1]);  // check i/r sensors front 1,2
      delay(150);			// length of move
      ir2 = analogRead(AnalogPins[2]);     
      delay(150);
      MrtFwd( 12 );			// move forward at speed
      cnt = cnt + 1;
      }
    servoR.write(90);          // all stop  
    servoL.write(90);         
    TurnRight( 13 );
    delay( 300 );	       // amount of turn could look at compass for this
    servoR.write(90);          // all stop  
    servoL.write(90);         
    }
}
    
