from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)


@app.route("/")
def root():
    u = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCdgELgiDjIoaZJDPocHK-Ijyh-eilLD0A")
    response = u.read()
    data = json.loads( response )
    stri=""
    return str(data["results"][0]["geometry"]["location"]["lng"])+"<br>"+str(data["results"][0]["geometry"]["location"]["lat"]);


if __name__ == "__main__":
   app.debug = True
   app.run()
