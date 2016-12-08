
import urllib2, json
from flask import Flask, render_template, json, Request
app = Flask(__name__)


@app.route("/")
def index():
	return 'hi'

@app.route('/two')
def pagethree():
    return 'hi'

#returns as dictionary data, i will parse and add more later
def samplenews():
    response = urllib2.urlopen('https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=7f93124e015c4d33bbc2e336b0f2244d')
    data = json.load(response)
    dic = data[u'articles']
    return data
