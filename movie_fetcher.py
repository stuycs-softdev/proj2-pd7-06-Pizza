import json
from urllib import urlencode
import urllib2
import api_config as config
# title, 

def extract_terms(jsonr, terms):
    ret = {k:jsonr[terms[k]] for k in terms}
    return ret

def itunes_lookup(term):
    itj = itunes_json(term)['results'][0]
    return extract_terms(itj, config.itunes_terms)

def itunes_json(term):
    url = 'https://itunes.apple.com/search?'
    url += urlencode({'term':term, 'media':'movie'})
    return json.load(urllib2.urlopen(url))

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
