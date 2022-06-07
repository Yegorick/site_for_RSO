from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:223355Kyui@localhost/rso'
app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STORAGE_SONG'] = 'D:/Projects/Site/app/static/songs'
app.config['SECRET_KEY'] = 'none'
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

babel = Babel(app)

db = SQLAlchemy(app)

from app.models import Songs, SongsView, Document,DocumentView

admin = Admin(app, name='РСО')
#admin.add_view(ModelView(Songs, db.session(), name='Песни'))
admin.add_view(SongsView(Songs, db.session(), name='Песни'))
admin.add_view(DocumentView(Document, db.session(), name='Документы'))

from app import routes
