import secrets

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

import models
from db import db
from resources.dog import blp as DogBlueprint
from resources.user import blp as UserBlueprint
from resources.vaccine import blp as VaccineBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Dogs REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))
    JWTManager(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(DogBlueprint)
    api.register_blueprint(VaccineBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
