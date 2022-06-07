import os

from flask import redirect, render_template, url_for, request
from flask_login import login_user, login_required, logout_user

from app import app, db, Tovar, ALLOWED_EXTENSIONS, User


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def allowed_file(filename):
    # Функция проверки расширения файла
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # проверим, передается ли в запросе файл
        if 'file' not in request.files:
            print(1)
            return redirect('/tovari')
        file = request.files['file']
        # Если файл не выбран
        if file.filename == '':
            print(2)
            return redirect('/tovari')
        if file and allowed_file(file.filename):
            # сохраняем файл
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        else:
            return redirect('/tovari')
        title = request.form['title']
        cost = request.form['cost']
        info = request.form['info']
        photo_name = file.filename

        tovar = Tovar(title=title, cost=cost, info=info,  photo_name=photo_name)
        try:
            db.session.add(tovar)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    names = ('Egor', 'Max', 'Oleg')
    return render_template('about.html', n=names)

@app.route('/tovari')
def tovari():
    tov = db.session.query(Tovar).all()
    return render_template('tovari.html', tovari=tov)

@app.route('/tovari/<int:id>')
@login_required
def tovar(id):
    tov = db.session.query(Tovar).all()
    return render_template('tovar.html', tovari=tov, idd=id)

@app.route('/tovari/<int:id>/del')
def tovar_del(id):
    tov = db.session.query(Tovar).all()[id - 1]
    try:
        db.session.delete(tov)
        db.session.commit()
        return redirect('/tovari')
    except:
        return "Что-то пошло не так"

@app.route('/tovari/<int:id>/red', methods=['POST', 'GET'])
def tovar_red(id):
    tov = Tovar.query.get(id)
    if request.method == 'POST':
        # проверим, передается ли в запросе файл
        if 'file' not in request.files:
            print(1)
            return redirect('/tovari')
        file = request.files['file']
        # Если файл не выбран
        if file.filename == '':
            print(2)
            tov.title = request.form['title']
            tov.cost = request.form['cost']
            tov.info = request.form['info']
        else:
            if file and allowed_file(file.filename):
                # сохраняем файл
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            tov.title = request.form['title']
            tov.cost = request.form['cost']
            tov.info = request.form['info']
            tov.photo_name = file.filename

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"
    else:
        return render_template('update.html', tovar=tov)


@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    login = request.form.get('login')
    password = request.form.get('password')
    if login and password:
        user = User.query.filter_by(login=login, password=password).first()
        print(user)
        if user:
            login_user(user)
            return redirect('/admin')
        else:
            return redirect('/log_in')
    else: 
        return render_template('login.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect('/')
