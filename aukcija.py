from flask import Flask
import config
from flask_admin import Admin
from models.user import User
from models.article import Article
from models.offer import Offer
from models import db  # db imported last because of problem with missing tables
from views.admin_controller import AdminModelView
from views.index_controller import Index
from views.login_controller import Login
from views.register_controller import Register
from views.logout_controller import Logout
from views.profile_controller import Profile
from views.create_article_controller import CreateArticle
from views.article_controller import ArticleC
from views.user_controller import UserC
from views.search_controller import Search

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)
admin = Admin(app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/profile', view_func=Profile.as_view('profile'))
app.add_url_rule('/user/<int:user_id>', view_func=UserC.as_view('user'))
app.add_url_rule('/create_article', view_func=CreateArticle.as_view('create_article'))
app.add_url_rule('/article/<int:article_id>', view_func=ArticleC.as_view('article'))
app.add_url_rule('/search', view_func=Search.as_view('search'))

admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Article, db.session))
admin.add_view(AdminModelView(Offer, db.session))

if __name__ == '__main__':
    app.run()
