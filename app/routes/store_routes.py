from flask import Blueprint, jsonify, request
from ..models.stores import Store
from ..models.users import User
from ..middlewares.role_required import role_required
from flask_jwt_extended import get_jwt_identity
from ..schemas.store_schema import StoreSchema
from ..db import db
from sqlalchemy import func
from ..roles import ALL_USERS, ADMIN


store_bp = Blueprint('store_bp', __name__)
store_schema = StoreSchema(many=True)
single_store_schema = StoreSchema()

@store_bp.route('/', methods=['GET'])
@role_required(role=ALL_USERS)
def get_all_hospital():
    stores = Store.query.all()
    return jsonify(data=store_schema.dump(stores)), 200

@store_bp.route('/by_city/', methods=['GET'])
@role_required(role=ALL_USERS)
def get_hospitals_by_city():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify(response = 'no such user exist'), 404
    
    stores = Store.query.filter_by(store_city=user.user_city).all()

    return jsonify(response = store_schema.dump(stores)), 200


@store_bp.route('/by_state/', methods=['GET'])
@role_required(role=ALL_USERS)
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

@store_bp.route('/by_id/', methods=['GET'])
@role_required(role=ALL_USERS)
def show_hospitals_by_id():

    hospital_id = request.args.get('hospital_id', 1, type=int)

    hospital_details = Store.query.filter_by(store_id = hospital_id)

    if hospital_id == None:
        return jsonify(response = {}), 404
    

    return jsonify(hospital = store_schema.dump(hospital_details)), 200

@store_bp.route('/add_store/', methods=['POST'])
@role_required(role=ADMIN)
def add_store():

    request_body = request.get_json()

    try:
        validated_data = single_store_schema.load(request_body)
    except Exception as e:
        return jsonify(repsonse = f'error as {e}'), 400
    
    existing_store = Store.query.filter_by(
        store_name = validated_data['store_name'],
        store_landmark = validated_data['store_landmark'],
        store_city = validated_data['store_city'],
        store_state = validated_data['store_state'],
        store_owner = validated_data['store_owner'],
    )

    if existing_store:
        return jsonify(response = 'store already existing...'), 409
    
    new_store = Store(**validated_data)

    try:
        db.session.add(new_store)
        db.session.commit()
        return jsonify(response = 'store added successfully...'), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(response = f'error as {e}'), 500
    
@store_bp.route('/search_store/', methods=['POST'])
@role_required(role=ALL_USERS)
def search_store():

    request_body = request.get_json()

    if 'store_name' not in request_body:
        return jsonify(response = 'there must be store name'), 404
    
    store_details = Store.query.filter(func.lower(Store.store_name).ilike(f"%{request_body['store_name'].lower()}%")).all()

    print(f'store details - {store_details}')

    if not store_details:
        return jsonify(response = 'no such store present'), 400
    
    return jsonify(response = store_schema.dump(store_details)), 200


