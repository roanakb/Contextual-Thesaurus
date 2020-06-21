from flask import Flask, request, render_template

from get_synonyms import get_words, get_best_words

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    word = request.form['word']
    sent = request.form['sent']
    synsets = get_words(word)
    best_words = get_best_words(word, sent, synsets)
    return render_template('index.html', synsets=synsets, best_words=best_words, word=word, sentence=sent)
