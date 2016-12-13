#include <Adafruit_NeoPixel.h>
#define PIN 3 //neo pin number
#define NUM_LEDS 16 //number of pixels in strip
int voltPin = 2; // 5V output
int MRLval = 0;
int Animation=1;


Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(voltPin, OUTPUT);
  digitalWrite(voltPin, HIGH);
  analogReference(DEFAULT);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  Serial.begin(9600);  
  Serial.println("--- Start DEBUG ---");
}



void loop() {
  MRLval = Serial.parseInt();
  Serial.println(MRLval);
  switch (MRLval) {
    case 1:
    Animation=1;
    break;
    case 2:
    Animation=2;
    break;
    case 3:
    Animation=3;
    break;
    case 9:
    Animation=0;
    break;
  }

  switch (Animation) {
  case 1: 
  CylonBounce(0xff, 0, 0, 2, 100, 50);
  break;
  case 2: 
  Fire(55,120,15);
  break;
  case 3: 
  Strobe(0xff, 0xff, 0xff, 10, 50, 1000);
  break;
  case 0: 
  strip.show();
  break;
  }
  
  //
}


void Strobe(byte red, byte green, byte blue, int StrobeCount, int FlashDelay, int EndPause){

  for(int j = 0; j < StrobeCount; j++) {

    setAll(red,green,blue);

    showStrip();

    delay(FlashDelay);

    setAll(0,0,0);

    showStrip();

    delay(FlashDelay);

  }

 

 delay(EndPause);
}


void CylonBounce(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay){


  for(int i = 0; i < NUM_LEDS-EyeSize-2; i++) {

    setAll(0,0,0);

    setPixel(i, red/10, green/10, blue/10);

    for(int j = 1; j <= EyeSize; j++) {

      setPixel(i+j, red, green, blue); 

    }

    setPixel(i+EyeSize+1, red/10, green/10, blue/10);

    showStrip();

    delay(SpeedDelay);

  }


  delay(ReturnDelay);


  for(int i = NUM_LEDS-EyeSize-2; i > 0; i--) {

    setAll(0,0,0);

    setPixel(i, red/10, green/10, blue/10);

    for(int j = 1; j <= EyeSize; j++) {

      setPixel(i+j, red, green, blue); 

    }

    setPixel(i+EyeSize+1, red/10, green/10, blue/10);

    showStrip();

    delay(SpeedDelay);

  }

  

  delay(ReturnDelay);
}




void Fire(int Cooling, int Sparking, int SpeedDelay) {

  static byte heat[NUM_LEDS];

  int cooldown;

  

  // Step 1.  Cool down every cell a little

  for( int i = 0; i < NUM_LEDS; i++) {

    cooldown = random(0, ((Cooling * 10) / NUM_LEDS) + 2);

    

    if(cooldown>heat[i]) {

      heat[i]=0;

    } else {

      heat[i]=heat[i]-cooldown;

    }

  }

  

  // Step 2.  Heat from each cell drifts 'up' and diffuses a little

  for( int k= NUM_LEDS - 1; k >= 2; k--) {

    heat[k] = (heat[k - 1] + heat[k - 2] + heat[k - 2]) / 3;

  }

    

  // Step 3.  Randomly ignite new 'sparks' near the bottom

  if( random(255) < Sparking ) {

    int y = random(7);

    heat[y] = heat[y] + random(160,255);

    //heat[y] = random(160,255);

  }


  // Step 4.  Convert heat to LED colors

  for( int j = 0; j < NUM_LEDS; j++) {

    setPixelHeatColor(j, heat[j] );

  }


  showStrip();

  delay(SpeedDelay);
}

void setPixelHeatColor (int Pixel, byte temperature) {

  // Scale 'heat' down from 0-255 to 0-191

  byte t192 = round((temperature/255.0)*191);

 

  // calculate ramp up from

  byte heatramp = t192 & 0x3F; // 0..63

  heatramp <<= 2; // scale up to 0..252

 

  // figure out which third of the spectrum we're in:

  if( t192 > 0x80) {                     // hottest

    setPixel(Pixel, 255, 255, heatramp);

  } else if( t192 > 0x40 ) {             // middle

    setPixel(Pixel, 255, heatramp, 0);

  } else {                               // coolest

    setPixel(Pixel, heatramp, 0, 0);

  }
}



void showStrip() {

 #ifdef ADAFRUIT_NEOPIXEL_H 

   // NeoPixel

   strip.show();

 #endif

 #ifndef ADAFRUIT_NEOPIXEL_H

   // FastLED

   FastLED.show();

 #endif
}

void setPixel(int Pixel, byte red, byte green, byte blue) {

 #ifdef ADAFRUIT_NEOPIXEL_H 

   // NeoPixel
   strip.setBrightness(20);
   strip.setPixelColor(Pixel, strip.Color(red, green, blue));

 #endif

 #ifndef ADAFRUIT_NEOPIXEL_H 

   // FastLED

   leds[Pixel].r = red;

   leds[Pixel].g = green;

   leds[Pixel].b = blue;

 #endif
}

void setAll(byte red, byte green, byte blue) {

  for(int i = 0; i < NUM_LEDS; i++ ) {

    setPixel(i, red, green, blue); 

  }

  showStrip();
}
