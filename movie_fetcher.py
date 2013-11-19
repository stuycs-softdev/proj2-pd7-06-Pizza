import json
from urllib import urlencode
import urllib2
import api_config as config
# title, 

def extract_terms(jsonr, terms):
    ret = {k:jsonr[terms[k]] for k in terms}
    return ret

# iTunes

def itunes_lookup(term):
    try:
        itj = itunes_json(term)['results'][0]
        return extract_terms(itj, config.itunes_terms)
    except:
        return None

def itunes_json(term):
    url = 'https://itunes.apple.com/search?'
    url += urlencode({'term':term, 'media':'movie'})
    js = json.load(urllib2.urlopen(url))
    return js

# OMDB

def omdb_lookup(title):
    return extract_terms(omdb_json(title), config.omdb_terms)

def omdb_json(title):
    url = 'http://www.omdbapi.com/?'
    url += urlencode({'t':title, 'r':'json', 'plot':'full', 'tomatoes':'true'})
    js = json.load(urllib2.urlopen(url))
    js['Actors'] = [a.strip() for a in js['Actors'].split(',')]
    return js

# etc.

def printd(d):
    print '%s'%d['title']
    print '[ $%.2f ]'%d['price']
    print '\n\t%s'%d['desc']

#print [k for k in itunes_json(raw_input('Lookup in iTunes: '))['results'][0]]
if __name__ == '__main__':
    print '-'*80
    try:
        itj = itunes_json(raw_input('Lookup in iTunes: '))['results'][0]
        printd(extract_terms(itj, config.itunes_terms))
    except:
        print 'Lookup failed.'
