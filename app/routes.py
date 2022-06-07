from flask import render_template, url_for
import os

from app import app, db, Songs, Document

file_path = os.path.abspath(os.path.dirname(__name__))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/first_slet')
def first_slet():
    return render_template('first_slet.html')

@app.route('/documents')
def documents():
    docs = db.session.query(Document).all()
    spis = {}
    for i in docs:
        size = os.path.getsize(f'{file_path}/app/static/storage/files/{i.title}.pdf') / 1000
        if size >= 1000:
            size /= 1000
            size_str = f'{str(size)[:4]} МБ'
            print(size_str)
        else:
            size_str = f'{str(size)[:4]} КБ'
        spis[i.title] = size_str
    return render_template('documents.html', docs = docs, size=spis)

@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/music')
def music():
    songs = db.session.query(Songs).all()
    return render_template('music.html', songs = songs)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')