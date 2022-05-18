from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return render_template('documents.html')

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
    return render_template('music.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
