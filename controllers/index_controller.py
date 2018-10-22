from flask import render_template, session
from flask.views import MethodView
from models.article import Article
from forms.search_form import SearchForm


class Index(MethodView):

    def get(self):

        articles = Article.query.order_by(Article.id.desc()).limit(5).all()

        return render_template('index.html',
                               title='Home | Aukcije Online',
                               session=session.get('username'),
                               articles=articles,
                               search_form=SearchForm())
