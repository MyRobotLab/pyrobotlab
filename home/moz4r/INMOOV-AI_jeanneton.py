# -*- coding: utf-8 -*- 


#this is broken now need fix on myai.cloud
def Jeanneton(data):
	#print "http://192.168.1.166:4242/?question="+urllib2.quote(data).replace(" ", "%20")
	try:
		a = Parse("http://127.0.0.1:4242/?question="+urllib2.quote(data).replace(" ", "%20")).replace("Jea:", "")
	except: 
		a = "0"
	print a
	#print BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20")
	if a[0]=="0":
		talk("CONNECTION PROBLEM")
	elif a[0:299]=="":
		#return(a[0:299])
		talk("CONNECTION PROBLEM")
	else:
		talk(a[0:299])