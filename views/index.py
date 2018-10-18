from flask import Blueprint

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return 'Home'

