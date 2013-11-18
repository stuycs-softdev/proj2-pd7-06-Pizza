#!/usr/bin/python

import json
import urllib
import urllib2
import sys

usage = """
Usage: python OMDB.py 'movie title'
e.g python OMDB.py Titanic
"""

if len(sys.argv)!=2:
    print (usage)
    sys.exit(0)

title = sys.argv[1]

movie = urllib2.urlopen("http://www.omdbapi.com/?t="+title)

data = json.load(movie)

print data["Title"]
print data["Year"]
print data["Plot"]
