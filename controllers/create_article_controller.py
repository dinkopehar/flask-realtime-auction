import datetime
import os
import tinify
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
        end_day = datetime.datetime.strptime(article_form.end_day.data, '%d-%m-%Y')

        if article_form.validate_on_submit():
            current_user = User.query.filter_by(username=session.get('username')).first()

            f = article_form.article_image.data
            name = current_user.username + "__" + f.filename
            name = secure_filename(name)

            tinify.key = os.environ['TINIFY']

            if request.headers['Host'] == '127.0.0.1:5000':
                tinify.from_file(f).to_file(os.path.join("./static/article_images/",
                                                         name))
            else:
                tinify.from_file(f).to_file(os.path.join(os.curdir,
                                                         'static',
                                                         'article_images',
                                                         name))

            new_article = Article(name=article_form.name.data,
                                  category=article_form.category.data,
                                  town=article_form.town.data,
                                  minimal_price=article_form.minimal_price.data,
                                  article_image=name,
                                  end_day=end_day,
                                  end_time=article_form.end_time.data,
                                  description=article_form.description.data,
                                  user_id=current_user.id)

            db.session.add(new_article)
            db.session.commit()

            return redirect(url_for('article',
                                    article_id=Article.query.order_by(Article.id.desc()).first().id))
        else:
            return redirect(url_for('create_article'))



