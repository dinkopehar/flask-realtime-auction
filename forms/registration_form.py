from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    full_name = StringField('full_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    adress = StringField('adress', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('submit')
