from flask import Flask, session, render_template, redirect, url_for, request
<<<<<<< HEAD
import urllib2, json, os
from utils.newsUtils import givenews
=======
import urllib2, json, requests, os, datetime
from utils.newsUtils import samplenews, sources
>>>>>>> 9d67a7bd2b2ae709e10c0b108d792496f7a04eb5
from utils.weatherUtils import getWeather, adrToCoords

app = Flask(__name__)
app.secret_key=os.urandom(32)


@app.route("/")
def root():
    return redirect(url_for("news"))

@app.route("/weather")
def weather():
    if "lat" in session:
        p=getWeather(session['lat'], session['lng'])
        for day in p["daily"]["data"]:
            day["time"]=datetime.datetime.fromtimestamp(int(day["time"])).strftime('%Y-%m-%d')
        curr=p["daily"]["data"].pop(0)
        print p["daily"]["data"]
        return render_template("weather.html", current=curr, weatherContent=p["daily"]["data"], weatheractive="active", navcolor= "#8e44ad")
                #return render_template('weather.html', adrForm="weatherContent=wc")
    else:
        return render_template("weatheraddress.html", weatheractive="active", navcolor= "#8e44ad")

@app.route("/submitAddress", methods=['POST'])
def submitAddress():
    if request.form['address']=='':
        return render_template("weatheraddress.html", error=
                               '''
                               <div class="row">
                               <div class="container-fluid">
                               <div class="col-sm-3">
                               </div>
                               <div class="col-sm-6">
                               <div class="alert alert-danger">
                               <center><strong>Error!</strong> Invalid Address!</center>
                               </div>
                               </div>
                               <div class="col-sm-3">
                               </div>
                               </div>
                               </div>
                               '''
                               , weatheractive="active", navcolor= "#8e44ad")
    adr=adrToCoords(request.form['address'])
    if adr=="Error":
        return render_template("weatheraddress.html", error=
                               '''
                               <div class="row">
                               <div class="container-fluid">
                               <div class="col-sm-3">
                               </div>
                               <div class="col-sm-6">
                               <div class="alert alert-danger">
                               <center><strong>Error!</strong> Invalid Address!</center>
                               </div>
                               </div>
                               <div class="col-sm-3">
                               </div>
                               </div>
                               </div>
                               '''
                               , weatheractive="active", navcolor= "#8e44ad")
    session['lat']=adr['lat']
    session['lng']=adr['lng']
    return redirect(url_for("weather"))

    categories = ['general', 'technology', 'sport', 'business', 'entertainment']

@app.route("/news")
def news():
<<<<<<< HEAD
    dic = givenews('abc-news-au');
    return render_template("index.html", newsactive="active", news=dic)
    return 'hi'
=======
    dic = samplenews(66,'latest')
    return render_template("index.html", newsactive="active", news=dic, navcolor="#16a085")
>>>>>>> 9d67a7bd2b2ae709e10c0b108d792496f7a04eb5

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
