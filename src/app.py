import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db


# Import de las tablas
from models.favorite import Favorite
from models.people import People
from models.planet import Planet
from models.user import User

from dotenv import load_dotenv

from routes.favorites import api as api_favorites
from routes.peoples import api as api_peoples
from routes.planets import api as api_planets
from routes.users import api as api_users


load_dotenv()


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


db.init_app(app)
Migrate(app, db)
CORS(app)


app.register_blueprint(api_favorites, url_prefix="/api")
app.register_blueprint(api_peoples, url_prefix="/api")
app.register_blueprint(api_planets, url_prefix="/api")
app.register_blueprint(api_users, url_prefix="/api")


if __name__ == '__main__':
    app.run()