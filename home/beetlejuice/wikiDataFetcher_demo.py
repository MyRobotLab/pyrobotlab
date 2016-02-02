# To know the IDs of property, visit : https://www.wikidata.org/wiki/Wikidata:List_of_properties/en


wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")

query = "Eiffel Tower"
wdf.setWebSite("enwiki") 

# Display the label
wdf.setLanguage("en")
print "Label from query : " + wdf.getLabel(query)

# Set language to english
wdf.setLanguage("en")

# Display the description 
print "Description EN : " + wdf.getDescription(query)

# Change language to French and display again the description
wdf.setLanguage("fr")
print "Description FR : " + wdf.getDescription(query)

# Display the identification number of the document
print "Identification number of the Eiffel Tower is : " + wdf.getId(query)

# Display the description from document identification number ( South pole )
wdf.setLanguage("en")
print "Label from ID Q933 is : " + wdf.getLabelById("Q933")

# Display the description from document identification number ( South pole )
wdf.setLanguage("en")
print "Description from ID Q933 : " + wdf.getDescriptionById("Q933")

# Display Date or time  (day, month, year, hour, minute, second, after, before
# This one don't work for the Eiffel Tower so : Not Found !
ID = "P569"
print "BirthDate : " + wdf.getTime(query,ID,"day") +"/" + wdf.getTime(query,ID,"month") + "/" + wdf.getTime(query,ID,"year")

# Display Date or time  (day, month, year, hour, minute, second, after, before
ID = "P571"
print "Built in : " + wdf.getTime(query,ID,"year")

# Display a property ( high of the eiffel tower )2048
print "high : " + wdf.getQuantity(query,"P2048")

# Display the official website url
print "Url : " + wdf.getUrl(query,"P856")
