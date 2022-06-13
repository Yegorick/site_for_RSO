from flask import render_template, url_for
import os, zipfile

from app import app, db, Songs, Document, Album, Post, Contact

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
        size = os.path.getsize(f'{file_path}/app/static/storage/files/{i.title}.pdf') / 1024
        if size >= 1000:
            size /= 1024
            size_str = f'{size:.1f} МБ'
            print(size_str)
        else:
            size_str = f'{size:.1f} КБ'
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
    albums = db.session.query(Album).all()
    return render_template('gallery.html', albums=albums)

@app.route('/gallery/<int:id>')
def photos(id):
    album = Album.query.get(id)
    if zipfile.is_zipfile(f'app/static/storage/albums/{album.title}/{album.title}.zip'):
        zip_info = zipfile.ZipFile(f'app/static/storage/albums/{album.title}/{album.title}.zip', 'r')
        zip_info.extractall(f'app/static/storage/albums/{album.title}')
        zip_info.close()
        os.remove(f'app/static/storage/albums/{album.title}/{album.title}.zip')

    photos = os.listdir(f'app/static/storage/albums/{album.title}')
    print(photos)
    print(album.title)
    photos.remove(f'{album.title}.jpg')
    return render_template('photos.html', photos=photos, id=id, album=album)

@app.route('/music')
def music():
    songs = db.session.query(Songs).all()
    return render_template('music.html', songs = songs)

@app.route('/contacts')
def contacts():
    contacts = db.session.query(Contact).all()
    return render_template('contacts.html', contacts=contacts)