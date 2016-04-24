#include <Servo.h>

/*
for azul mobile platform running on mega board
which has:
parallax pings
i/r sensors
servo motor drivers
eacon sensor
compass HMC5883L
april 20,2016
 */

#include <Wire.h>
#include <SPI.h>
#include <HMC5883L.h>
HMC5883L compass;
#include <Servo.h>
Servo servoR; // create servo object to control a servo
Servo servoL; // create servo object to control a servo
#include <SoftwareSerial.h>
SoftwareSerial LedSerial(12, 13); // RX2=12 and TX2=13   RX3=63 and TX3=64  RX1=45 and TX1=46


String serdata = "";
// I/R sensors data  turns out this data is not very good
int distcen = 0;
int distright = 0;
int distleft = 0;
// ping sensors left and right  info very good
int DistPingRight = 0;
int DistPingLeft = 0;
// input routine
String cmd;
String sBuffer = "";
String sResp = "?";
// motors are controlled like servo
int OldSpeed = 90;   // storage of last speed for stopping
int speed = 90;
int wheeloffsetR = 0;   // try to adjust for different speed motors
int wheeloffsetL = 0;
		
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
  LedSerial.begin(2400);            // separate board that controls lights
  LedSerial.print( "!DC16");     // all leds off board address
  LedSerial.print( B00 );     // statusLo controls OUT1..OUT8, statusHi controls OUT9..OUT16  1 bit = On, 0 bit = Off
  LedSerial.println( "X");     // end of string
  Serial.begin (57600);             // setup Serial port at 57,600 baud
  Serial.println(" platform Ver. 4-20-2016");
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
        delay(1);
        break;
      case 'P':
        ReadPing();        
        delay(1);
        break;
      case 'C':
        ReadCompass();        
        delay(1);
        break;
      case 'F':         // go forward
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          Serial.println("wrong spd");
        }
        MrtFwd( speed );        
        break;
      case 'B':         // go backward
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          Serial.println("wrong spd");
        }
        MrtRev( speed );        
        break;
      case 'R':         // turn right
        ProcessRestCmd (sBuffer.substring (1));
        if (speed > 55){
          Serial.println("wrong spd");
        }
        TurnRight( speed );        
        break;
      case 'L':         // turn left
        ProcessRestCmd (sBuffer.substring (1));
       if (speed > 55){
          Serial.println("wrong spd");
        }
        TurnLeft( speed );        
        break;
      case 'M':         // move forward looking at sensors
        ProcessRestCmd (sBuffer.substring (1));
       if (speed > 55){
          Serial.println("wrong spd");
        }
        MoveFwd( speed );        
        break;
      case 'S':
        MrtStop();        
        break;
     case '?':
        Serial.println("Help  ver. 04-20-2016");
        Serial.println("P ping distance readings ");
        Serial.println("A analog readings ");
        Serial.println("C compass not working ");
        Serial.println("F forward motors 0 to 50 ");
        Serial.println("B reverse motors 0 to 50 ");
        Serial.println("R turn right 0 to 50");
        Serial.println("L turn left 0 to 50");
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
 for (int x=0; x < AnalogPinCount; x++){
   reading = analogRead(AnalogPins[x]);        // get raw number
   Serial.print("A"); 
   Serial.print(x);
   Serial.print("=");
   Serial.print(reading);         // show raw number
   Serial.print(",");
//   Serial.print("cnt, ");
//   voltage = reading * 5.0;
//   voltage /= 1024.0; 
//   voltage = 0.00488 * reading;        // 5 / 1024 = .00488
//   Serial.print(voltage);         // show voltage calculated
//   Serial.print("v, ");
 }
 Serial.println();
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
  float headingDegrees = heading * 180/M_PI; 
//  Output(headingDegrees);
  Serial.println(headingDegrees);
  delay(500);     //jhs 5sec
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
        delay(50);
//        Serial.println(speed);   // make sure working right
      }
      servoR.write(90);           // all stop for sure    
      servoL.write(90);             
}

void MrtFwd( int speed ){ 
     OldSpeed = speed + 90;           //storing for stopping             
     servoR.write(90 + speed + wheeloffsetR);   // try to adjust for different speed motors
     servoL.write(90 + speed + wheeloffsetL);          
}

void MrtRev( int speed ){   
     OldSpeed = 90 - speed;         
     servoR.write(90 - speed + wheeloffsetR);               
     servoL.write(90 - speed + wheeloffsetL);     
     int ir0=100;
     while( ir0<400 ){ 
        ir0 = analogRead(AnalogPins[0]);        // check i/r sensor back
        delay(50);
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

void MoveFwd( int speed ){ 
     OldSpeed = speed + 90;           //storing for stopping             
     servoR.write(90 + speed + wheeloffsetR);        
     servoL.write(90 + speed + wheeloffsetL);    
     int ir1=100;
     int ir2=100;
      while( (ir1<400) && (ir2<400) ){ 
        ir1 = analogRead(AnalogPins[1]);        // check i/r sensors front 1,2
        delay(30);
        ir2 = analogRead(AnalogPins[2]);     
        delay(30);
     }
//      ReadAnalog();        // just checking to see if working
      MrtStop();  
}

