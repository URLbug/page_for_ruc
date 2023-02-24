from flask import render_template, Blueprint

home = Blueprint('home', __name__, template_folder='html', static_folder='html')

@home.route('/', methods=['POST', 'GET'])
def index():
    
    return render_template('index.html')