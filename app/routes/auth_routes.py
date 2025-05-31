from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService
from ..models.users import User
from ..models.block_list import TokenBlocklist
from ..schemas.user_schema import UserSchema
from passlib.hash import bcrypt_sha256
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from ..db import db

auth_bp = Blueprint('auth_bp', __name__)

user_schema = UserSchema()

@auth_bp.route('/login/', methods=['POST'])
def login():

    json_data = request.get_json()

    if 'user_name' not in json_data or 'user_password' not in json_data:
        return jsonify({'message': 'missing user_name and user_passwrod'}), 400
    
    user = AuthService.authenticate(json_data['user_name'], json_data['user_password'])

    if not user:
        return jsonify(message = 'Invalid credentials'), 401
    
    tokens = AuthService.generate_tokens(user_id=user.user_id)

    return jsonify(tokens), 200

@auth_bp.route('/logout/', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()

    return jsonify(response = 'log out successfully...'), 200



@auth_bp.route('/signup/', methods=['POST'])
def sign_up():
    json_data = request.get_json()

    if not json_data:
        return jsonify(message = 'No input data provided'), 400
    
    try:
        user_schema.validate(json_data)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': e.messages}), 422
    
    hash_pass = bcrypt_sha256.hash(json_data['user_password'])

    json_data['user_password'] = hash_pass

    new_user = User(**json_data)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(message = 'user created'), 201


@auth_bp.route('/refresh/', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=str(user_id))

    return jsonify(access_token = new_access_token), 200