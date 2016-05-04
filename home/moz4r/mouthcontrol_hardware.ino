// HARDWARE MOUTHCONTROL
//
// dedicated arduino
// Read voltage value from speaker and move jaw
// First POC version, need to be calibrated and fixed :
// If you want test it please read Analog values when you have NO SOUND and enter MIN and MAX
// I think you need AREF
//
// To do : 
// automatic values detection when sound level change
// Webkit : shutdown microphone when speak

#include <Servo.h> 



#define servoPin     9     // jaw
#define HPpin        5     // analog speaker input



Servo myservo;                 

int     MIN = 665; 
int     MAX = 680; 
int     SecondDetection = 1; // 
int     val = 0;     // variable to store the read value
int     i = 0;
int     pos = 75;    // variable to store the servo position 
int     BoucheStatus = 0;
int     ActionBouche = 0;


void setup() 
{ 
  
        
  analogReference(EXTERNAL);
  pinMode(servoPin, OUTPUT);      
  Serial.begin(9600);  
  Serial.println("--- Start DEBUG ---");
  myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object 
  myservo.write(75);
} 
 
void loop()  
{ 

     
    val = analogRead(HPpin);

    if (val < MIN || val > MAX ) // if values detected : speaker voltage
  
     {
      BoucheStatus = 1; // closed mouth

     }
     else  

     {
       i++;
     }
  
     if (i>=SecondDetection)
      {
       i=0;
        BoucheStatus = 0;
        Serial.println(val);
  
      }

      if (BoucheStatus == 0 && ActionBouche == 0)

      {
      myservo.write(90);
      ActionBouche = 1;
      delay(50);
      myservo.write(75);
      delay(50);
      }
      if (BoucheStatus == 1 && ActionBouche == 1)
      {
       myservo.write(75);
       ActionBouche =0;
       delay(50);
      }

    
delay(1);
    
   
}
