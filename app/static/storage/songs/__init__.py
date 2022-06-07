import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_login.mixins import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tovari.db'
# папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'C:/Users/Familu/Projects/FL/app/static/img'
# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'anykey'

db = SQLAlchemy(app)

class Tovar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    info = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.datetime.now())
    photo_name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        infoo = str([self.title, self.cost, self.info, self.date,  self.photo_name])
        return infoo

class AnyView(BaseView):
    @expose('/')
    def any_page(self):
        return self.render('admin/index.html')

admin = Admin(app, name='Наш Магазин')
admin.add_view(ModelView(Tovar, db.session, name='Товары'))
admin.add_view(AnyView(name='Новая Страница'))

login_manager = LoginManager(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


admin.add_view(ModelView(User, db.session, name='Пользователи'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app import routes
