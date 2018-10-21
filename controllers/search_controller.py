from flask import redirect, url_for, render_template, request, session
from flask.views import MethodView
from models.article import Article


class Search(MethodView):

    def get(self):
        try:
            request.args['category']
            request.args['town']
        except KeyError:
            return redirect(url_for('index'))

        category = request.args['category']
        town = request.args['town']

        articles = Article.query.filter_by(category=category,
                                           town=town).all()
        if articles is None:
            return redirect(url_for('index'))

        return render_template('search.html',
                               title='Search | Aukcije Online',
                               articles=articles,
                               session=session.get('username'))


