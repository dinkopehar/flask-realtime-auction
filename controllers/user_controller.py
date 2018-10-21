from flask import render_template, redirect, url_for
from flask.views import MethodView
from models.user import User
from models.article import Article


class User_(MethodView):

    def get(self, user_id):

        if user_id is None:
            return redirect(url_for('index'))

        user = User.query.filter_by(id=user_id).first()
        articles = Article.query.filter_by(user_id=user.id).all()

        return render_template('user.html',
                               title='User | Aukcije Online',
                               user=user,
                               articles=articles)

