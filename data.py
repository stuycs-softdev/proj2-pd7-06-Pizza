import movie_fetcher as mf
class Movie():
    # props: should load all properties but recommendations
    # recs: should load recommendations
    def __init__(self, title, props=True, recs=False):
        self.title = title
        self.yt = None # dict with yt IDs
        self.wiki_url = None # wikipedia URL
        self.recs = None # Movie objects of recs
        self.rec_content_loaded = False # True once rec contents (not just titles) is loaded
        self.content_loaded = False # True once non-rec content is loaded
        self.desc = None # description
        self.img = None # poster, or assosciated image
        self.cast = None # list of cast
        self.itunes_price = None # price on iTunes
        self.itunes_currency = None # currency of itunes_price
        self.genre = None # genre
        self.explicit = None # True on explicit
        if props:
            self.load_info()
        if recs:
            self.load_recs()

    def load_recs(self):
        recs_with_content = []
        tk = mf.tastekid_lookup(self.title, True, True)
        for r in tk['suggestions']:
            recs_with_content.append(Movie(r))
        self.recs = recs_with_content
        self.rec_content_loaded = True

    def load_info(self):
        omdb = mf.omdb_lookup(self.title)
        tk = mf.tastekid_lookup(self.title)
        itunes = mf.itunes_lookup(self.title)
        if omdb is not None:
            self.desc = omdb['desc']
            self.img = omdb['img']
            self.cast = omdb['cast']
            self.title = omdb['title']
        if tk is not None:
            self.yt = {
                'ident':tk['info']['youtube_id'],
                'url':tk['info']['youtube_url'],
                'title':tk['info']['youtube_title']
            }
            self.wiki_url = tk['info']['read_more_url']
            if self.desc is None or self.desc == 'N/A':
                self.desc = itunes['desc']
            if self.title is None:
                self.title = tk['title']
            #        self.recs = tk['suggestions']
        if itunes is not None:
            self.itunes_price = itunes['price']
            self.itunes_currency = itunes['currency']
            self.genre = itunes['genre']
            self.explicit = itunes['explicit'] == 'explicit'
            if self.desc is None or self.desc == 'N/A':
                self.desc = itunes['desc']
            if self.title is None:
                self.title = itunes['title']
        self.content_loaded = True
