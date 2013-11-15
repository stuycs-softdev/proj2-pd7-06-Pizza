import json
from urllib import urlencode
import urllib2

# title, 

itunes_terms = {
    'title':'trackName',
    'price':'trackPrice',
    'desc':'longDescription',
    'trailer':'previewUrl'
}

def extract_terms(jsonr, terms):
    ret = {}
    for key in terms:
        ret[key] = jsonr[terms[key]]
    return ret

def itunes_json(term):
    url = 'https://itunes.apple.com/search?'
    url += urlencode({'term':term, 'media':'movie'})
    return json.load(urllib2.urlopen(url))

#print [k for k in itunes_json(raw_input('Lookup in iTunes: '))['results'][0]]
if __name__ == '__main__':
    itj = itunes_json(raw_input('Lookup in iTunes: '))['results'][0]
    print extract_terms(itj, itunes_terms)
