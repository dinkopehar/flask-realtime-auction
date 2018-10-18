import os

class Config:

    SECRET_KEY = os.urandom(32).hex()
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aukcija.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    try:
        RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
        RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
    except KeyError:
        RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PRIVATE_KEY = ''


