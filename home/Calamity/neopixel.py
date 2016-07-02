from time import sleep
red=140;
blue=0;
green=0;
while 1:
  lp=1;
  for l in range(0,100):
  	for x in range (1,neopixel.numPixel+1):
  		if(x==lp): 
  			if (l<25):
  				neopixel.setPixel(x,150,0,0)
  			elif (l<50):
  				neopixel.setPixel(x,0,150,0)
  			elif (l<75):
  				neopixel.setPixel(x,0,0,150)
  			else:
  				neopixel.setPixel(x,150,150,150)
  		else: 
  			neopixel.setPixel(x,0,0,0)
  		neopixel.sendPixelMatrix()
  	lp=lp+1
  	if (lp>neopixel.numPixel+1):
  		lp=1	
  	sleep(0.001)
  for l in range (0,1000):
  	if l==0:
  		blue=0
  		green=0
  	if l==250:
  		blue=140
  	if l==500:
  		green=140
  	if l==750:
  		blue=0
	for x in range (1, neopixel.numPixel+1):
		neopixel.setPixel(x,red,green,blue);
	neopixel.sendPixelMatrix()
	red=red-5;
	if red<0:
		red=140
	sleep(0.03)
