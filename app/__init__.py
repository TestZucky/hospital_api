import os
from flask import Flask
from .config import DevConfig, ProdConfig
from .db import db
from .models.block_list import TokenBlocklist
from .routes.store_routes import store_bp
from .routes.auth_routes import auth_bp
from .routes.user_routes import users_bp
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV')
    jwt = JWTManager(app)

    if env == 'dev':
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(ProdConfig)

    db.init_app(app)
    migrate = Migrate(app=app, db=db)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        token = TokenBlocklist.query.filter_by(jti=jti).first()
        return token is not None

    app.register_blueprint(store_bp, url_prefix='/stores')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')

    return app