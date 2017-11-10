
 LY=ps2x.Analog(PSS_LY);
     analogWrite(enB, LY);
     Serial.println(LY); 
     if (LY < 127)  {
         digitalWrite(in3, LOW);
         digitalWrite(in4, HIGH);
         Serial.println(LY); 
     } 
     else (LY == 127);  {
         LY = 0;
         digitalWrite(in3, HIGH);
         digitalWrite(in4, LOW);
         Serial.println(LY);
     }
      else (LY > 126);  {
         digitalWrite(in3, HIGH);
         digitalWrite(in4, LOW);
         Serial.println(LY);
     }
