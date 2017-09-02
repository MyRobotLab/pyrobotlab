OpenWeatherMap=Runtime.createAndStart("OpenWeatherMap", "OpenWeatherMap")
OpenWeatherMap.setApiKey("YOUR_KEY") #https://home.openweathermap.org/
OpenWeatherMap.setUnits("metric") # or imperial
OpenWeatherMap.setLang("fr") # en / de ...

# fetch raw data:
r=[]
r=OpenWeatherMap.fetchRaw("YOUR CITY")
print r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]
# 0:description
# 1:temp
# 2:location
# 3:id // https://github.com/MyRobotLab/inmoov/blob/master/InMoov/chatbot/bots/en/aiml/_inmoovChatbot.aiml#L298
# 4:pressure
# 5:humidity
# 6:temp_min
# 7:temp_max
# 8:speed
# 9:deg

# fetch complete sentence data:
print OpenWeatherMap.fetchWeather("YOUR CITY")
