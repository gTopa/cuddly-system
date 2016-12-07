import urllib2, json
def getWeather():
    u = urllib2.urlopen("https://api.darksky.net/forecast/1de933934abc6c18e4627dc35a7c1549/8,70")
    response = u.read()
    data = json.loads( response )
    return data;