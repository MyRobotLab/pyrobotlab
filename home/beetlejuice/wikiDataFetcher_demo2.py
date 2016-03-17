wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")

query = "eiffel tower"
wdf.setWebSite("enwiki") 
print "Url : " + wdf.getData(query,"P856")
# Display a property ( high of the eiffel tower )2048
print "high : " + wdf.getData(query,"P2048")

# Display a monolingual value
print "Birthname of Adam Sandler : " + wdf.getData("Adam Sandler","P1477")

# Display Date or time  (day, month, year, hour, minute, second, after, before
query = "adam sandler"
ID = "P569"
print "BirthDate : " + wdf.getTime(query,ID,"day") +"/" + wdf.getTime(query,ID,"month") + "/" + wdf.getTime(query,ID,"year")

# Display Date by default
query = "pentagon"
ID = "P571"
print "Built in : " + wdf.getData(query,ID)
