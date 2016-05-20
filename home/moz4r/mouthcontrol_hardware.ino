
// HARDWARE MOUTHCONTROL
//
// dedicated arduino
// Read voltage value from speaker and move jaw
// First POC version, need to be calibrated and fixed :
// If you want test it please read Analog values when you have NO SOUND and enter MIN , min is the value when robot speak
// I use AREF 1 volt and sound come from unamplified jack, from PC
//
// To do : 
// Webkit : shutdown microphone when speak

#include <Servo.h> 
#define servoPin 2



#define HPpin        0    // analog speaker input



Servo myservo;                 

int     MIN = 100; 
int     SecondDetection = 1; // 
int     val = 0;     // variable to store the read value
int     i = 0;
int     pos = 75;    // variable to store the servo position 
int     BoucheStatus = 0;
int     ActionBouche = 0;
int     Repos = 0;
int     CompteurRepos = 0;
String  dbg;


void setup() 
{ 
  
        
  analogReference(INTERNAL);
   
  Serial.begin(9600);  
  Serial.println("--- Start DEBUG ---");
  myservo.attach(servoPin);
  myservo.write(50);
  delay(1000);
  //myservo.detach();
  
} 
 
void loop()  
{ 

     
    val = analogRead(HPpin);
//Serial.println(val);
//Serial.print('\n');
    if (val > MIN ) // if values detected : speaker voltage
  
     {
      
     i++;
     
     }
     else  

     {
      BoucheStatus = 1; // closed mouth
     }
  
     if (i>=SecondDetection)
      {
       i=0;
        BoucheStatus = 0;
        //Serial.println(val);
  
      }

      if (BoucheStatus == 0 && ActionBouche == 0)

      {
      //Serial.println(val);
      ActionBouche = 1;
      //myservo.attach(9);
      delay(10);
      
     
      myservo.write(100);
      
      CompteurRepos=0;
      delay(100);
      
      }
      if (BoucheStatus == 1 && ActionBouche == 1)
      {
        
        if (Repos==0)
        {
        myservo.attach(servoPin);
        delay(10);
        }
        
       
       myservo.write(90);
       Repos = 0;
       CompteurRepos = 0;
       ActionBouche =0;
       delay(100);
       //digitalWrite(servoPin, LOW);
      }

      if (CompteurRepos == 30 && Repos == 0)
      {
       myservo.write(45); 
      }


      if (CompteurRepos == 100 && Repos == 0)
      {
       myservo.write(45); 
       delay(100);      
       myservo.detach(); 
       Repos=1;
      }
 dbg="a" + String(CompteurRepos) + "a" + String(ActionBouche) + "b" + String(BoucheStatus);
 Serial.println(dbg);
CompteurRepos+=1;    
delay(1);
    
   
}
