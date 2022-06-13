from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_babelex import Babel
from flask_security import SQLAlchemyUserDatastore, Security

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:223355Kyui@localhost/rso'
app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STORAGE_SONG'] = 'D:/Projects/Site/app/static/songs'
app.config['SECRET_KEY'] = 'none'
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
app.config['SECURITY_PASSWORD_SALT'] = 'hidi2212n123j123'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'

babel = Babel(app)

db = SQLAlchemy(app)

from app.models import Songs, SongsView, Document, DocumentView, Album, AlbumView, Post, PostView, Contact, ContactView, User, Role, HomeView

admin = Admin(app, name='РСО', url='/', index_view=HomeView(name='Home'))
admin.add_view(SongsView(Songs, db.session(), name='Песни'))
admin.add_view(DocumentView(Document, db.session(), name='Документы'))
admin.add_view(AlbumView(Album, db.session(), name='Альбомы'))
admin.add_view(PostView(Post, db.session(), name='Посты'))
admin.add_view(ContactView(Contact, db.session(), name='Контакты'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(app, user_datastore)

from app import routes
