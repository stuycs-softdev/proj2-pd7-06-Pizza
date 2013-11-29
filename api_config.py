# defines a standard set of keys for all api requests to return

# {'movie_fetcher key' : 'api returned key'}

itunes_terms = {
    'title':'trackName',
    'price':'trackPrice',
    'currency':'currency',
    'genre':'primaryGenreName',
    'explicit':'trackExplicitness',
    'desc':'longDescription',
    'trailer':'previewUrl',
    'img':'artworkUrl100',
    'purchase_url':'trackViewUrl'
}
omdb_terms = {
    'title':'Title',
    'desc':'Plot',
    'img':'Poster',
    'cast':'Actors'
}

rt_terms = {
    "title":"title",
    "rating":"mpaa_rating",
    "statement":"critics_consensus",
    "scores":"ratings",
    "posters":"posters"
}

# recommendations

#tastekid
# BEWARE this stuff is under tastekid_lookup('movie')['info']
tk_terms = {
    'title':'Name',
    'desc':'wTeaser',
    'read_more_url':'wUrl',
    'youtube_title':'yTitle',
    'youtube_url':'yUrl',
    'youtube_id':'yID'
}
