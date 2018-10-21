from flask import redirect, url_for, render_template, session
from flask.views import MethodView
from werkzeug.security import check_password_hash

from forms.login_form import LoginForm
from models.user import User


class Login(MethodView):

    def get(self):

        if session.get('username'):
            return redirect(url_for('index'))

        login_form = LoginForm()
        return render_template('login.html',
                               title='Login | Aukcije Online',
                               login_form=login_form,
                               session=session.get('username'))

    def post(self):

        login_form = LoginForm()

        if login_form.validate_on_submit():

            user = User.query.filter_by(username=login_form.username.data).first()

            if user is None:
                return redirect(url_for('login'))
            elif check_password_hash(user.password, login_form.password.data):
                session['username'] = user.username
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))
