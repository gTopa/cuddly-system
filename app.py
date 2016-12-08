from flask import Flask, session, render_template, redirect, url_for	
import urllib2, json
from utils.newsUtils import samplenews
from utils.weatherUtils import getWeather

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for("news"))

@app.route("/weather")
def weather():
    p=getWeather()
    return p["timezone"];

@app.route("/news")
def news():
    dic = samplenews(66,'latest')
    return render_template("index.html", newsactive="active", news=dic)

if __name__ == "__main__":
   app.debug = True
   app.run()
