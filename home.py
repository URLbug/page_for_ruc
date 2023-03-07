from flask import render_template, Blueprint, request

from database import db, User

# bluprint
home = Blueprint('home', __name__, template_folder='html', static_folder='html')

# index(home page) 
@home.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        about_me = request.form.get('about_me')

        if first_name != '' and last_name != '' and email != '' and about_me != '':
            user = User(first_name, last_name, email, about_me)
            db.session.add(user)
            db.session.flush()
            db.session.commit()


    return render_template('index.html')