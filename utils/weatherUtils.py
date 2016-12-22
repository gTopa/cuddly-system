import urllib2, json

def getWeather(latitude, longitude):
	coordinates=str(latitude)+','+str(longitude)
	u = urllib2.urlopen("https://api.darksky.net/forecast/1de933934abc6c18e4627dc35a7c1549/"+coordinates)
	response = u.read()
	data = json.loads( response )
	return data;

def adrToCoords(address):
    n=0
    print len(address)
    while(n<len(address)):
        if (address[n]==' '):
            address=address.replace(' ', '+')
        n+=1
    print address
    u = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyCdgELgiDjIoaZJDPocHK-Ijyh-eilLD0A")
    response = u.read()
    data = json.loads( response )
    if len(data['results'])>0:
        return data['results'][0]['geometry']['location']
    else:
        return "Error"