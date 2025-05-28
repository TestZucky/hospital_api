from flask import Blueprint, jsonify, request
from ..models.stores import Store
from ..models.users import User
from ..middlewares.role_required import role_required
from flask_jwt_extended import get_jwt_identity
from ..schemas.store_schema import StoreSchema
from ..db import db


store_bp = Blueprint('store_bp', __name__)
store_schema = StoreSchema(many=True)

@store_bp.route('/', methods=['GET'])
@role_required(role=['admin','user'])
def get_all_hospital():
    stores = Store.query.all()
    return jsonify(data=store_schema.dump(stores)), 200

@store_bp.route('/by_city/', methods=['GET'])
@role_required(role=['admin', 'user'])
def get_hospitals_by_city():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify(response = 'no such user exist'), 404
    
    stores = Store.query.filter_by(store_city=user.user_city).all()

    return jsonify(response = store_schema.dump(stores)), 200


@store_bp.route('/by_state/', methods=['GET'])
@role_required(role=['admin', 'user'])
def get_hospitals_by_state():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify(response = 'no such user exist'), 404
    
    page = request.args.get('page', 1, type=int)
    per_page = 2

    paginated_stores = Store.query.filter_by(store_state = user.user_state).paginate(page=page, per_page=per_page, error_out=False)

    stores = paginated_stores.items
    
    # stores = Store.query.filter_by(store_state=user.user_state).all()

    return jsonify(response = store_schema.dump(stores)), 200
