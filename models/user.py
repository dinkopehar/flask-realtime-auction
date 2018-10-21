from . import db


class User(db.Model):

    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    adress = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile_image = db.Column(db.String(256), nullable=True, default="animated-cat-13.jpg")
    articles = db.relationship('Article', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
