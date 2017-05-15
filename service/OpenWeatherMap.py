OpenWeatherMap=Runtime.createAndStart("OpenWeatherMap", "OpenWeatherMap")
OpenWeatherMap.setApiKey("YOUR_KEY") #https://home.openweathermap.org/
OpenWeatherMap.setUnits("metric") # or imperial
OpenWeatherMap.setLang("fr") # en / de ...

# fetch raw data:
r=[]
r=OpenWeatherMap.fetchRaw("YOUR CITY")
print r[0],r[1],r[2]

# fetch complete sentence data:
print OpenWeatherMap.fetchWeather("YOUR CITY")
