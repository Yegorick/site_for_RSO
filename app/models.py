from flask_sqlalchemy import Model
from app import app, db
from flask import url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import form

import os
from random import getrandbits

file_path = os.path.abspath(os.path.dirname(__name__))

def name_gen_song(model, file_data):
    name = f'{model.title}.mp3'
    return name

def name_gen_doc(model, file_data):
    name = f'{model.title}.pdf'
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
