from flask import Flask
import config
from models import db

# from views.index import index_blueprint


app = Flask(__name__)
db.init_app(app)

app.config.from_object(config.Config)



#app.register_blueprint(index_blueprint)

if __name__ == '__main__':
    app.run()
