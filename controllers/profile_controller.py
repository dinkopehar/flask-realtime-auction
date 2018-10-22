import os
import tinify  # tinypng.com for compression
from flask import redirect, url_for, render_template, session, request
from flask.views import MethodView
from werkzeug.utils import secure_filename

from models import db
from models.user import User
from models.article import Article


class Profile(MethodView):

    def get(self):

        if session.get('username') is None:
            return redirect(url_for('index'))

        user = User.query.filter_by(username=session.get('username')).first()
        articles = Article.query.filter_by(user_id=user.id).all()

        return render_template('profile.html',
                               title='My Profile | Aukcije Online',
                               user=user,
                               articles=articles)

    def post(self):

        user = User.query.filter_by(username=session.get('username')).first()
        articles = Article.query.filter_by(user_id=user.id).all()

        file = request.files['fileToSave']
        name = user.username + "_" + file.filename
        name = secure_filename(name)

        tinify.key = os.environ['TINIFY']  # Compression of image

        if request.headers['Host'] == '127.0.0.1:5000':
            tinify.from_file(file).to_file(os.path.join("./static/profile_images/",
                                                        name))
        else:
            tinify.from_file(file).to_file(os.path.join(os.curdir,
                                                        'static',
                                                        'profile_images',
                                                        name))

        user.profile_image = name
        db.session.commit()

        return redirect(url_for('profile',
                                user=user,
                                articles=articles))
