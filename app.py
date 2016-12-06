from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)


@app.route("/")
def root():
    u = urllib2.urlopen("https://newsapi.org/v1/articles?sortBy=latest&apiKey=490f5af0da6541dab948ebe1b84110d5")
    response = u.read()
    data = json.loads( response )
    stri=""
    return data["status"];


if __name__ == "__main__":
   app.debug = True
   app.run()
