from flask import Flask, session, render_template, redirect, url_for, request
import urllib2, json
#from utils.newsUtils import samplenews
from utils.weatherUtils import getWeather

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for("news"))

@app.route("/weather")
def weather():
    if "address" in session:
        p=getWeather('40.7128', '74.0059')
    else:
        p=getWeather('40.7128', '74.0059')
    wc=[p['timezone']]
    return render_template('weather.html', weatherContent=wc);

@app.route("/submitAddress", methods=['POST'])
def submitAddress():
    adr=request.form('address')
    Session.Add("address", adr)
    return redirect(url_for("weather"))

@app.route("/news")
def news():
    #dic = samplenews(66,'latest')
    #return render_template("index.html", newsactive="active", news=dic)
    return 'hi'

@app.route("/test1")
def hi():
    stri='<form action="/test2" method="POST">Address: <input type="text" name="address"><input type="submit" name="submit" value="submit"><br></form>'
    return stri
    
@app.route("/test2", methods=["POST"])
def testfunc():
    n=0
    address=request.form['address']
    print len(address)
    while(n<len(address)):
        if (address[n]==' '):
            address=address.replace(' ', '+')
        n+=1
    print address
    u = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyCdgELgiDjIoaZJDPocHK-Ijyh-eilLD0A")
    response = u.read()
    data = json.loads( response )
    return str(data['results'][0]['geometry']['location']['lat'])+'<br>'+str(data['results'][0]['geometry']['location']['lng']);
    
if __name__ == "__main__":
   app.debug = True
   app.run()
