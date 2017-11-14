LY=ps2x.Analog(PSS_LY);
    Serial.println(LY); 
    if (LY < 127) {
        spd = map(LY, 126, 0, 0, 257);
        analogWrite(enB, spd);
        digitalWrite(in3, LOW);
        digitalWrite(in4, HIGH);
        Serial.println(spd); 
     } 
     if (LY > 127) {
         spd = map(LY, 127, 257, 0, 257);
         analogWrite(enB, spd);
         digitalWrite(in3, HIGH);
         digitalWrite(in4, LOW);
         Serial.println(spd);
     } 
     if (LY == 127) {
         spd = 0;
         analogWrite(enB, spd);
         digitalWrite(in3, LOW);
         digitalWrite(in4, LOW);
         Serial.println(spd);
     }
