# movie_fetcher.py
# SERVICE_lookup(term) returns search results from SERVICE in a dict with keys as defined by api_config.py
# SERVICE_json(term) returns search results from SERVICE in its json defined format

import json
from urllib import urlencode
import urllib2
import api_config as config
import keys
import cache

# utils, etc.

# parses json returned dicts to movie_fetcher returned dicts, with key to key mapping as defined in terms {'newKey':'oldKey'}
# usually used with api_config returned terms dicts
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

# TasteKid

def tastekid_lookup(title):
    if cache.in_cache(title):
        return retrieve_cached(title)
    tkjson = tastekid_json(title)['Similar']
    item = extract_terms(tkjson['Info'][0], config.tk_terms)
    results = [extract_terms(tk, config.tk_terms) for tk in tkjson['Results']]
    suggestions = [r['title'] for r in results]
    tk = {'title':title, 'info':item, 'suggestions':suggestions}
    cache.cache(tk)
    for r in results:
        cache.cache(r)
    return tk

def tastekid_json(title):
    url = 'http://www.tastekid.com/ask/ws?'
    url += urlencode({'q':title+'//movies', 'verbose':'1', 'format':'JSON',
                      'f':keys.tk_f, 'k':keys.tk_k
                  })
    print "tk url:", url
    js = json.load(urllib2.urlopen(url))
    return js
    
# testing

def printd(d):
    print '%s'%d['title']
    print '[ $%.2f ]'%d['price']
    print '\n\t%s'%d['desc']

if __name__ == '__main__':
    print '-'*80
    try:
        itj = itunes_json(raw_input('Lookup in iTunes: '))['results'][0]
        printd(extract_terms(itj, config.itunes_terms))
    except:
        print 'Lookup failed.'
