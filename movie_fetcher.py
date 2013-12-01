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
    ret = {k:jsonr[terms[k]] for k in terms if terms[k] in jsonr}
    return ret

# iTunes
def itunes_lookup(term, check_cache=True):
    if check_cache:
        ret = cache.retrieve_valid(term)
        if ret is not None:
            iterms = config.itunes_terms.keys()
            ret = {k:v for k,v in ret.items() if k in iterms}
            if ret.keys() == iterms:
                return ret
    itj = itunes_json(term)['results'][0]
    return extract_terms(itj, config.itunes_terms) if itj is not None else None

def itunes_json(term):
    url = 'https://itunes.apple.com/search?'
    url += urlencode({'term':term, 'media':'movie'})
    js = json.load(urllib2.urlopen(url))
    return js

# OMDB
def omdb_lookup(title, check_cache=True):
    if check_cache:
        ret = cache.retrieve_valid(title)
        if ret is not None:
            oterms = config.omdb_terms.keys()
            ret = {k:v for k,v in ret.items() if k in oterms}
            if ret.keys() == oterms:
                return ret
    js = omdb_json(title)
    return extract_terms(js, config.omdb_terms) if js is not None else None

def omdb_json(title):
    url = 'http://www.omdbapi.com/?'
    url += urlencode({'t':title, 'r':'json', 'plot':'full', 'tomatoes':'true'})
    js = json.load(urllib2.urlopen(url))
    if js['Response'] == 'False':
        return None
    js['Actors'] = [a.strip() for a in js['Actors'].split(',')]
    return js

# TasteKid
def tastekid_lookup(title, check_cache=True, load_rec_content=False, use_key=True):
    if check_cache and cache.in_cache(title):
        ret = cache.retrieve_valid(title)
        tkterms = config.tk_terms.keys()
        ret = {k:v for k,v in ret.items() if k in tkterms}
        if ((not load_rec_content) or ('suggestions' in ret)) and ret.keys() == tkterms:
            return ret
    tkjson = tastekid_json(title, use_key)
    if 'Error' in tkjson:
        print 'Yarr there be an error fetching tk; trying sneakily'
        try:
            tkjson = tastekid_json(title, False)['Similar']
        except:
            return None
    else:
        tkjson = tkjson['Similar']
    item = extract_terms(tkjson['Info'][0], config.tk_terms) #actual movie
    suggestions = [extract_terms(tk, config.tk_terms) for tk in tkjson['Results']]
    rec_titles = [r['title'] for r in suggestions]
    tk = {'title':item['title'], 'suggestions':rec_titles}
    cache.upsert_properties(item)
    cache.cache(tk)
    for r in suggestions:
        cache.upsert_properties(r)
    for k in config.tk_terms:
        tk[k] = item[k]
    return tk

def tastekid_json(title, use_key=True):
    url = 'http://www.tastekid.com/ask/ws?'
    params = {'q':title+'//movies', 'verbose':'1', 'format':'JSON',
                      'f':keys.tk_f, 'k':keys.tk_k}
    if not use_key:
        del params['f']
        del params['k']
        print params
    url += urlencode(params)
    js = json.load(urllib2.urlopen(url))
    return js
    
# Rotten Tomatoes

def rt_lookup(title, check_cache=True):
    if check_cache and cache.in_cache(title):
        ret = cache.retrieve_valid(title)
        tomaterms = config.rt_terms.keys()
        ret = {k:v for k,v in ret.items() if k in tomaterms}
        if ret.keys() == tomaterms:
            return ret
    rtj = rt_json(title)["movies"][0]
    return extract_terms(rtj, config.rt_terms)

def rt_json(title):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=vq8bhcvbrnmmwndpv9cw9twr&'
    url += urlencode({'q':title, 'page_limit':1})
    js = json.load(urllib2.urlopen(url))
    return js
