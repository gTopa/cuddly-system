from flask import Flask, session, render_template, redirect, url_for	
import urllib2, json
from utils.weatherUtils import getWeather

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for("weather"))

@app.route("/weather")
def weather():
    p=getWeather()
    return p["timezone"];

if __name__ == "__main__":
   app.debug = True
   app.run()
