import datetime
from flask import redirect, url_for, render_template, session, request, flash
from flask.views import MethodView
from models import db
from models.offer import Offer
from models.user import User
from models.article import Article


class Article_(MethodView):

    def get(self, article_id):

        article = Article.query.filter_by(id=article_id).first()

        if article is None:
            return redirect(url_for('index'))

        user = User.query.filter_by(id=article.user_id).first()
        article.views += 1
        db.session.commit()

        offers_by_article = Offer.query.filter_by(article_id=article.id).order_by(Offer.price.desc()).limit(3).all()
        top_users = []
        if offers_by_article is not None:
            for offer in offers_by_article:
                top_users.append(User.query.filter_by(id=offer.user_id).first())

        session_username = session.get('username')
        if user.username == session_username:
            session_username = None

        return render_template('article.html',
                               title='Article | Aukcije Online',
                               article=article,
                               user=user,
                               offers_by_article=offers_by_article,
                               top_users=top_users,
                               session=session_username)

    def post(self, article_id):

        article = Article.query.filter_by(id=article_id).first()

        try:
            expected_value = int(request.form['new_price'])
            if expected_value < article.minimal_price:
                raise ValueError
        except ValueError:
            flash("Price lower than expected")
            return redirect(url_for('article', article_id=article_id))
        except Exception:
            flash("Invalid price")
            return redirect(url_for('article', article_id=article_id))

        us = User.query.filter_by(username=session.get('username')).first()
        new_offer = Offer(article_id=article.id,
                          user_id=us.id,
                          price=request.form['new_price'])
        db.session.add(new_offer)
        db.session.commit()
        return redirect(url_for('article', article_id=article_id))


