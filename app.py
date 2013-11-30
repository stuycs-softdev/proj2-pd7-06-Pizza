from flask import Flask, render_template
from flask import redirect, url_for, request
import movie_fetcher
from data import Movie

app = Flask(__name__)

# just some basic testing; this can be removed

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/m', methods=['POST'])
@app.route('/m/<title>', methods=['GET'])
def msearch(title=''):
    if request.method == 'POST':
        title = request.form['title']
        legality = request.form['legality']
    if request.method == 'GET':
        title=title
        legality = 'legal'
    itunes = movie_fetcher.itunes_lookup(title)
    omdb = movie_fetcher.omdb_lookup(title)
    try:
        m=Movie(title)
        youtube_id=m.yt['ident']
        poster=m.posters['original']
        reclist=m.recs.unloaded
        return render_template('movie.html', itunes=itunes, omdb=omdb, legality=legality, youtube_id=youtube_id, poster=poster,reclist=reclist)
    except:
        return render_template('movie.html',itunes=itunes,omdb=omdb,legality=legality)

if __name__ == "__main__":
    app.debug = True
    app.run()
