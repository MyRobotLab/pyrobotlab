#include <Adafruit_NeoPixel.h>
#define PIN 3
#define NUM_LEDS 16
int voltPin = 2;
// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = 5V volt pin


Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(voltPin, OUTPUT);
   digitalWrite(voltPin, HIGH);
  strip.begin();

  strip.show(); // Initialize all pixels to 'off'
}



void loop() {

  Fire(55,120,15);
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
