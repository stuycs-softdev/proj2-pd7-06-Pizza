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
