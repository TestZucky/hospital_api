from passlib.hash import bcrypt_sha256
from ..db import db
from ..models.users import User
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthService:

    @staticmethod
    def authenticate(user_name, user_password):
        user = User.query.filter_by(user_name=user_name).first()
        print(user)
        print(type(user))

        if user and bcrypt_sha256.verify(user_password, user.user_password):
            return user
        else:
            return None
        
    @staticmethod
    def generate_tokens(user_id):
        return {
            'access_token': create_access_token(identity=str(user_id)),
            'refresh_token': create_refresh_token(identity=str(user_id)),
        }