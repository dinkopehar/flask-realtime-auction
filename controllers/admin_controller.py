from flask import session
from flask_admin.contrib.sqla import ModelView


class AdminModelView(ModelView):

    def is_accessible(self):
        return session.get('username') == 'admin'

