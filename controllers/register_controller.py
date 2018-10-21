from flask import Blueprint, redirect, url_for, render_template, session, g
from flask.views import MethodView
from werkzeug.security import generate_password_hash
from forms.registration_form import RegisterForm
from models import db
from models.user import User


class Register(MethodView):

    def get(self):

        if session.get('username'):
            return redirect(url_for('index'))

        registration_form = RegisterForm()
        return render_template('register.html',
                               title='Register | Aukcije Online',
                               registration_form=registration_form,
                               session=session.get('username'))

    def post(self):

        registration_form = RegisterForm()

        if registration_form.validate_on_submit():

            new_user = User(full_name=registration_form.full_name.data,
                            username=registration_form.username.data,
                            email=registration_form.email.data,
                            adress=registration_form.adress.data,
                            password=generate_password_hash(registration_form.password.data))

            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('index'))

