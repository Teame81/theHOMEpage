# -*- coding: utf-8 -*-
from flask_wtf import  FlaskForm
from wtforms import SubmitField, RadioField, StringField

#Creating a form
class TimmieForm(FlaskForm):
    timmiehome = RadioField('Change?', choices=[('True','Hemma'),('False','Borta')])
    submit = SubmitField('Skicka')
