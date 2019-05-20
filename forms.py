from flask_wtf import  FlaskForm
from wtforms import SubmitField, RadioField, StringField

class TimmieForm(FlaskForm):
    timmiehome = RadioField('Ändra?', choices=[('True','Hemma'),('False','Borta')])
    submit = SubmitField('Skicka')
