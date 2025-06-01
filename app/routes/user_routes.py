from flask import Blueprint, jsonify
from ..schemas.user_schema import UserSchema
from ..middlewares.role_required import role_required 
from ..models.users import User
from ..roles import ADMIN

users_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema(many=True)

@users_bp.route('/', methods=['GET'])
@role_required(role=ADMIN)
def fetch_users():
    users = User.query.all()
    print(users)
    return jsonify(data=user_schema.dump(users)), 200