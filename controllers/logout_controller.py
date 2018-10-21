from flask import redirect, url_for, session
from flask.views import MethodView


class Logout(MethodView):

    def get(self):
        session.pop('username', None)
        return redirect(url_for('index'))
