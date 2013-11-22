from pymongo import MongoClient
from datetime import datetime

_cache = MongoClient().db.cache

def check_cache(title):
    res = _cache.find_one({'title_lower':title.lower()})
    if (res is None or _isexpired(res['mod_date'])):
        return False
    return True

def retrieve_cached(title):
    return _cache.find_one({'title_lower':title.lower()})

def cache(d):
    d['title_lower'] = d['title'].lower()
    d['mod_date'] = datetime.now()
    _cache.update({'title':d['title']},
                  d, upsert=True
    )

def _isexpired(date):
    now = datetime.now()
    delta = now - date
    return delta.days > 3
