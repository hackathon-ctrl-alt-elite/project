from flask import Flask
from os import path
import os


def create_app():
    app = Flask(__name__)
    print("Flask app is being initialized")  # Debugging line
    app.config['SECRET_KEY'] = 'this secret key will be longer then most to differentiate'

    print(f"SECRET_KEY in create_app: {app.config['SECRET_KEY']}")


    # register the blueprints (that are made from other files) allows us to be able to use these routes.
    from routes import routes as routes_blueprint 
    app.register_blueprint(routes_blueprint, url_prefix = '/')

    return app


