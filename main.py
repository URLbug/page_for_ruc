from __init__ import app

from database import db

from home import home

import subprocess


# create database
db.create_all()

#register bluprint
app.register_blueprint(home)

if __name__ == '__main__':
    files = "amber_telegram.py"
    
    subprocess.Popen(args=["start", "python", files], shell=True, stdout=subprocess.PIPE)
    
    app.run('0.0.0.0', 9000, True)