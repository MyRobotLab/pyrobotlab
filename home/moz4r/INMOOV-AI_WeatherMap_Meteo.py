global cur_temperature
global low_temperature
global high_temperature
global todayforecast
cur_temperature=0
low_temperature=0
high_temperature=0
todayforecast=0

def Meteo(Town_Parameter):
	try:
		if Town_Parameter=="0":
			Town_Parameter=Town
		print "http://api.openweathermap.org/data/2.5/weather?q=" + Town_Parameter + "&units=" + units + "&APPID=" + WeatherMapMeteoApi
		response = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + Town_Parameter + "&units=" + units + "&APPID=" + WeatherMapMeteoApi) 
		weather = response.read()
		w = json.loads(weather)

		#CURRENT TEMPERATURE
		#print w['main']['temp'] #in kelvin
		print weather
		print w
		cur_temperature = round(float(w['main']['temp']),0)
		print ("Current Temp:")
		print (round(cur_temperature, 0))

		####################################################################
		#FORECAST
		response = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q="+Town_Parameter+"&units="+units+"&APPID="+WeatherMapMeteoApi) 
		weather = response.read()
		w = json.loads(weather)


		#TODAY'S LOW
		low_temperature = round(float(w['list'][0]['temp']['min']),0)
		print ("Daily Low: ")
		print (round(low_temperature, 0))

		#TODAY'S HIGH 
		high_temperature = round(float(w['list'][0]['temp']['max']),0)
		print ("Daily High: ")
		print (round(high_temperature, 0))

		#rain or clear today?
		todayforecast = w['list'][0]['weather'][0]['main']
		print ("The weather is: ")
		print (todayforecast)

		if todayforecast == 'Clear':
		   todayforecast=2
		if todayforecast == 'Rain':
		   todayforecast=3
		if todayforecast == 'Clouds':
		   todayforecast=1
		if todayforecast == 'Snow':
		   todayforecast=4
		
		print "SYSTEM METEO curtemperature " + str(cur_temperature).replace(".0", "") + " lowtemperature " + str(low_temperature).replace(".0", "") + " hightemperature " + str(high_temperature).replace(".0", "") + " Town " + str(Town_Parameter) + " COMMENTAIRE " + str(todayforecast)
		chatBot.getResponse("SYSTEM METEO curtemperature " + str(cur_temperature).replace(".0", "") + " lowtemperature " + str(low_temperature).replace(".0", "") + " hightemperature " + str(high_temperature).replace(".0", "") + " Town " + str(Town_Parameter) + " COMMENTAIRE " + str(todayforecast))
   

	except:
		chatBot.getResponse("SYSTEM METEO curtemperature 0 lowtemperature 0 hightemperature 0 Town 0 COMMENTAIRE 0")
		print sys.exc_info()[0]
		pass

