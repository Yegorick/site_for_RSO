from flask_sqlalchemy import Model
from app import app, db
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import form, AdminIndexView
from flask_security import UserMixin, RoleMixin, current_user

import os
from random import getrandbits
from datetime import datetime

file_path = os.path.abspath(os.path.dirname(__name__))

def name_gen_song(model, file_data):
    name = f'{model.title}.mp3'
    return name

def name_gen_doc(model, file_data):
    name = f'{model.title}.pdf'
    return name

def name_gen_img(model, file_data):
    name = f'{model.title}/{model.title}'
    return name

def name_gen_zip(model, file_data):
    name = f'{model.title}/{model.title}.zip'
    return name

def name_gen_post_img(model, file_data):
    name = f'{model.title}'
    return name

def name_gen_contact_img(model, file_data):
    name = f'{model.name}'
    return name

class Songs(db.Model):

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    squad = db.Column(db.String(100), nullable=False)



class SongsView(ModelView):
    
    column_labels = {
        'id':'№',
        'title':'Название',
        'author':'Автор',
        'squad':'Отряд'
    }
    
    def _list_thumbnail(view, context, model, name):
        if not model.song:
            return ''
        
        url = url_for('static', filename=os.path.join('storage/songs/', model.song))


    form_extra_fields = {"song": form.FileUploadField(
                                                        'Загрузите песню',
                                                        base_path = os.path.join(file_path, 'app\\static\\storage\\songs'),
                                                        namegen = name_gen_song
                                                        )}
        

    def create_form(self, obj=None):
        return super(SongsView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(SongsView, self).edit_form(obj)


class Document(db.Model):

    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)


class DocumentView(ModelView):
    
    column_labels = {
        'id':'№',
        'title':'Название'
    }

    def _list_thumbnail(view, context, model, name):
        if not model.document:
            return ''
        
        url = url_for('static', filename=os.path.join('storage/files/', model.document))


    form_extra_fields = {"song": form.FileUploadField(
                                                        'Загрузите файл',
                                                        base_path = os.path.join(file_path, 'app\\static\\storage\\files'),
                                                        namegen = name_gen_doc
                                                        )}
        

    def create_form(self, obj=None):
        return super(DocumentView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(DocumentView, self).edit_form(obj)


class Album(db.Model):
    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)


class AlbumView(ModelView):
    column_labels = {
        'id':'№',
        'title':'Название'
    }

    form_extra_fields = {"cover": form.ImageUploadField(
                                                        'Загрузите облжку',
                                                        base_path = os.path.join(file_path, 'app/static/storage/albums'),
                                                        url_relative_path = 'storage/albums',
                                                        namegen = name_gen_img
                                                        ),
                        "photos": form.FileUploadField(
                                                        'Загрузите архив с фотографиями',
                                                        base_path = os.path.join(file_path, 'app\\static\\storage\\albums'),
                                                        namegen = name_gen_zip
                                                        )}
                                        
    def create_form(self, obj=None):
        return super(AlbumView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(AlbumView, self).edit_form(obj)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False, default=datetime.now())


class PostView(ModelView):
    column_labels = {
        'id':'№',
        'title':'Название',
        'info':'Основная информация',
        'date':'Дата'
    }

    form_extra_fields = {"cover": form.ImageUploadField(
                                                        'Загрузите изображение',
                                                        base_path = os.path.join(file_path, 'app/static/storage/imgs'),
                                                        namegen = name_gen_post_img
                                                        )}
                                        
    def create_form(self, obj=None):
        return super(PostView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(PostView, self).edit_form(obj)


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

class ContactView(ModelView):
    column_labels = {
        'id':'№',
        'name':'ФИО',
        'role':'Роль',
        'email':'Контакты'
    }

    form_extra_fields = {"cover": form.ImageUploadField(
                                                        'Загрузите изображение',
                                                        base_path = os.path.join(file_path, 'app/static/storage/contact_photo'),
                                                        namegen = name_gen_contact_img
                                                        )}
                                        
    def create_form(self, obj=None):
        return super(ContactView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ContactView, self).edit_form(obj)


user_role = db.Table('user_role',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    )


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=user_role, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))


class HomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect( url_for('security.login', next=request.url ))
