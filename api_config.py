# defines a standard set of keys for all api requests to return

# {'movie_fetcher key' : 'api returned key'}

itunes_terms = {
    'title':'trackName',
    'price':'trackPrice',
    'desc':'longDescription',
    'trailer':'previewUrl',
    'img':'artworkUrl100'
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
tk_terms = {
    'title':'Name',
    'short_desc':'wTeaser',
    'read_more_url':'wUrl',
    'youtube_title':'yTitle',
    'youtube_url':'yUrl',
    'youtube_id':'yID'
}
