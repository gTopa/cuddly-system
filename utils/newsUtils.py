import urllib2, json
sources = ['abc-news-au','ars-technica','associated-press','bbc-news','bbc-sport','bild','bloomberg','business-insider','business-insider-uk','buzzfeed','cnbc','cnn','daily-mail','der-tagesspiegel','die-zeit','engadget','entertainment-weekly','espn','espn-cric-info','financial-times','focus','football-italia','fortune','four-four-two','fox-sports','google-news','gruenderszene','hacker-news','handelsblatt','ign','independent','mashable','metro','mirror','mtv-news','mtv-news-uk','national-geographic','new-scientist','newsweek','new-york-magazine','nfl-news','polygon','recode','reddit-r-all','reuters','sky-news','sky-sports-news','spiegel-online','t3n','talksport','techcrunch','techradar','the-economist','the-guardian-au','the-guardian-uk','the-hindu','the-huffington-post','the-lad-bible','the-new-york-times','the-next-web','the-sport-bible','the-telegraph','the-times-of-india','the-verge','the-wall-street-journal','the-washington-post','time','usa-today','wired-de','wirtschafts-woche']
def samplenews(source):
    stringres = 'https://newsapi.org/v1/articles?source=' + source + '&sortBy=latest&apiKey=7f93124e015c4d33bbc2e336b0f2244d'
    response = urllib2.urlopen(stringres)
    data = json.load(response)
    dic = data[u'articles'][0]
    print dic
    return dic
print sources[1]
samplenews(sources[1])



