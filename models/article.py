from . import db
from .user import User
import datetime


class Article(db.Model):

    __tablename__ = 'Article'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    town = db.Column(db.String(80), nullable=False)
    minimal_price = db.Column(db.Integer, nullable=False)
    article_image = db.Column(db.String(256), nullable=False)
    end_day = db.Column(db.Date, default=datetime.datetime.now())
    end_time = db.Column(db.Time, default=datetime.time())
    offers = db.relationship('Offer', backref='article', lazy=True)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __repr__(self):
        return '<Article {}>'.format(self.name)
