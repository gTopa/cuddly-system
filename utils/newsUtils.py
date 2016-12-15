import urllib2, json

sources = ['','ars-technica','associated-press','bbc-news','bbc-sport','bild','bloomberg','business-insider','business-insider-uk','buzzfeed','cnbc','cnn','daily-mail','der-tagesspiegel','die-zeit','engadget','entertainment-weekly','espn','espn-cric-info','financial-times','focus','football-italia','fortune','four-four-two','fox-sports','google-news','gruenderszene','hacker-news','handelsblatt','ign','independent','mashable','metro','mirror','mtv-news','mtv-news-uk','national-geographic','new-scientist','newsweek','new-york-magazine','nfl-news','polygon','recode','reddit-r-all','reuters','sky-news','sky-sports-news','spiegel-online','t3n','talksport','techcrunch','techradar','the-economist','the-guardian-au','the-guardian-uk','the-hindu','the-huffington-post','the-lad-bible','the-new-york-times','the-next-web','the-sport-bible','the-telegraph','the-times-of-india','the-verge','the-wall-street-journal','the-washington-post','time','usa-today','wired-de','wirtschafts-woche']
def samplenews(source):
    stringres = 'https://newsapi.org/v1/articles?source=' + source + '&sortBy=latest&apiKey=7f93124e015c4d33bbc2e336b0f2244d'
    response = urllib2.urlopen(stringres)
    data = json.load(response)
    dic = data[u'articles'][0]
    print dic
    return dic
print sources[1]
samplenews(sources[1])
#samplenews(sources[10],categories[1])

nytimes = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=8c0edd871eaf406da66e34ceee3f2663&sort=newest'

'''


ABC News,
BBC News
general technology sport business entertainment



'''
def nytimes():
    stringres = nytimes = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=8c0edd871eaf406da66e34ceee3f2663&sort=newest'
    response = urllib2.urlopen(stringres)
    data = json.load(response)
    listdata = data[u'response'][u'docs']
    newlist = []
    
    for row in listdata:
        dic = {}
        dic['url'] = row[u'web_url']
        dic['title'] = row[u'headline'][u'main']
        dic['publishedAt'] = row[u'pub_date']
        dic['author'] = row[u'byline'][u'original']
        dic['description'] = row[u'lead_paragraph']
        if(len(row[u'multimedia']) > 0):
            dic['urlToImage'] = row[u'multimedia'][0][u'url']
        
        else:
            dic['urlToImage'] = 'none'
        newlist.append(dic)
    
    print newlist
    return newlist
        
    
    #newdic = {}

#nytimes()
def givenews(source):
    samplenews(source)
    #nytimes()
        
givenews(sources[1])

'''
def samplenews(site,order):
    stringres = 'https://newsapi.org/v1/articles?source=' + sources[site] + '&sortBy=' + order + '&apiKey=key'
    response = urllib2.urlopen(stringres)
    data = json.load(response)
    dic = data[u'articles']
    print dic
    return dic
print sources[66]
#can sort by latest, top, or popular 
samplenews(66,'latest')

#nytimes()
    print listdata[0][u'lead_paragraph'] #time

    newlist
    for row in listdata:
        dic = {}
        dic['url'] = row[u'web_url']
        dic['urlToImage'] = row[u'multimedia'][0][u'url']
        dic['title'] = row[u'headline'][u'main']
        dic['publishedAt'] = row[u'pub_date']
        dic['author'] = row[u'byline'][u'original']
        dic['description'] = row[u'byline'][u'original']
        
            
    newdic = {}



'''