from pymongo import MongoClient

_cache = MongoClient().db.cache

def check_cache(title):
    res = _cache.find_one({'title':title})
    if (res is None or _isexpired(res['mod_date'])):
        return False
    return True

def cache(d):
    

def _isexpired(date):
    pass
