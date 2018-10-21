from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    full_name = StringField('Full name', validators=[DataRequired()])
    email = EmailField('Email Adress', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    adress = StringField('Address', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    recaptcha = RecaptchaField()
