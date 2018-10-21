import os
from flask import redirect, url_for, render_template, session, request
from flask.views import MethodView
from werkzeug.utils import secure_filename
from forms.article_form import ArticleForm
from models import db
from models.user import User
from models.article import Article


class CreateArticle(MethodView):

    def get(self):
        article_form = ArticleForm()

        if session.get('username') is None:
            return redirect(url_for('index'))

        return render_template('create_article.html',
                               title='Create Article | Aukcije Online',
                               article_form=article_form)

    def post(self):

        article_form = ArticleForm()

        if article_form.validate_on_submit():
            current_user = User.query.filter_by(username=session.get('username')).first()

            f = article_form.article_image.data
            name = current_user.username + "__" + f.filename
            name = secure_filename(name)

            if request.headers['Host'] == '127.0.0.1:5000':
                f.save(os.path.join("./static/article_images/", name))
            else:
                f.save(os.path.join(os.curdir, 'static', 'article_images', name))

            new_article = Article(name=article_form.name.data,
                                  category=article_form.category.data,
                                  town=article_form.town.data,
                                  minimal_price=article_form.minimal_price.data,
                                  article_image=name,
                                  time_left=article_form.time_left.data,
                                  description=article_form.description.data,
                                  user_id=current_user.id)

            db.session.add(new_article)
            db.session.commit()

        return redirect(url_for('create_article'))

