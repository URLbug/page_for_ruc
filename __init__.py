from flask import Flask


app = Flask(__name__, template_folder='html', static_folder='html')

app.config['SECRET_KEY'] = 'amber'