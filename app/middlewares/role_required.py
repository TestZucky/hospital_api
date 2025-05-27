from functools import wraps
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import jsonify
from ..models.users import User

def role_required(role: list):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if not user or user.user_role not in role:
                return jsonify(message="Unauthorized access"), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
