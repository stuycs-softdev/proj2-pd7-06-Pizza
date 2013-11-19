from flask import Flask, render_template
from flask import redirect, url_for, request
import movie_fetcher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/m', methods=['POST'])
@app.route('/m/<title>')
def msearch(title=''):
    if request.method == 'POST':
        title = request.form['title']
    itunes = movie_fetcher.itunes_lookup(title)
    omdb = movie_fetcher.omdb_lookup(title)
    return render_template('movie.html', itunes=itunes, omdb=omdb)

if __name__ == "__main__":
    app.debug = True
    app.run()
