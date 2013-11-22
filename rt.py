#!/usr/bin/python

import json
import urllib
import urllib2
import sys

usage = """
Usage: python rt.py 'movie title'
e.g python rt.py Titanic
"""

if len(sys.argv)!=2:
    print (usage)
    sys.exit(0)

title = sys.argv[1]

movie = urllib2.urlopen("http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=vq8bhcvbrnmmwndpv9cw9twr&q="+title+"&page_limit=1")

data = json.load(movie)

print data["movies"][0]["ratings"]["critics_score"]
print data["movies"][0]["synopsis"]
print data["movies"][0]["posters"]["original"]
print data["movies"][0]["abridged_cast"][1]["name"]
print data["movies"][0]["abridged_cast"][1]["characters"]

#http://developer.rottentomatoes.com/docs
