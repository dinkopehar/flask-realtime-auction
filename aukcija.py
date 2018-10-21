from flask import Flask, render_template
import config
from flask_admin import Admin
from models.user import User
from models.article import Article
from models.offer import Offer
from models import db  # db imported last because of problem with missing tables
from controllers.admin_controller import AdminModelView
from controllers.index_controller import Index
from controllers.login_controller import Login
from controllers.register_controller import Register
from controllers.logout_controller import Logout
from controllers.profile_controller import Profile
from controllers.create_article_controller import CreateArticle
from controllers.article_controller import Article_  # Namespace collision
from controllers.user_controller import User_  # Namespace collision
from controllers.search_controller import Search

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)
admin = Admin(app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/profile', view_func=Profile.as_view('profile'))
app.add_url_rule('/user/<int:user_id>', view_func=User_.as_view('user'))
app.add_url_rule('/create_article', view_func=CreateArticle.as_view('create_article'))
app.add_url_rule('/article/<int:article_id>', view_func=Article_.as_view('article'))
app.add_url_rule('/search', view_func=Search.as_view('search'))

admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Article, db.session))
admin.add_view(AdminModelView(Offer, db.session))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
