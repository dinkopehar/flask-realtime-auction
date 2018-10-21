from . import db
from .user import User


class Offer(db.Model):

    __tablename__ = 'Offer'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('Article.id'), nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Offer {}>'.format(id)
