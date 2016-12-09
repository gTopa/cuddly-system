import urllib2, json

def getWeather(latitude, longitude):
	coordinates=latitude+','+longitude
	u = urllib2.urlopen("https://api.darksky.net/forecast/1de933934abc6c18e4627dc35a7c1549/"+coordinates)
	response = u.read()
	data = json.loads( response )
	return data;