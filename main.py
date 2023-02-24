from __init__ import app

from home import home


# db.create_all()

app.register_blueprint(home)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)