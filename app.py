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
        legality = 'legal'
    try:
        try:
            m=Movie(title)
            itunes = m.itunes
            omdb = m.omdb
            poster=m.img
            youtube_id=m.yt['ident']
            return render_template('movie.html', legality=legality, poster=poster,m=m,youtube_id=youtube_id)
        except:
            itunes = movie_fetcher.itunes_lookup(title)
            omdb = movie_fetcher.omdb_lookup(title)
            return render_template('movie_no_m.html',itunes=itunes,omdb=omdb,legality=legality)
    except:
        return render_template('notfound.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=7006)
