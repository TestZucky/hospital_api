from flask import Blueprint, jsonify, request
from ..models.doctors import Doctor
from ..schemas.doctor_schema import DoctorSchema
from ..db import db
from passlib.hash import bcrypt_sha256
from flask_jwt_extended import create_access_token, create_refresh_token

doc_bp = Blueprint('doctor_bp', __name__)
doctor_schema = DoctorSchema()

@doc_bp.route('/signup/', methods=['POST'])
def signup():

    body = request.get_json()

    try:
        validated_body = doctor_schema.load(body)
    except Exception as e:
        return jsonify(response = f'error as {e}'), 404
    
    if Doctor.query.filter_by(doctor_email=validated_body['doctor_email']).first():
        return jsonify(response='Email already registered'), 409
    
    validated_body['doctor_password'] = bcrypt_sha256.hash(validated_body['doctor_password'])

    new_doctor_obj = Doctor(**validated_body)

    db.session.add(new_doctor_obj)
    db.session.commit()

    return jsonify(repsonse = 'signup successfull'), 200

@doc_bp.route('/login/', methods=['POST'])
def login():

    body = request.get_json()

    if 'doctor_email' not in body and 'doctor_password' not in body:
        return jsonify(response = 'missing email and password')
    
    doctor = Doctor.query.filter_by(doctor_email=body['doctor_email']).first()

    if not doctor:
        return jsonify(response = 'invalid email id')
    
    if not bcrypt_sha256.verify(body['doctor_password'], doctor.doctor_password):
        return jsonify(response='Invalid password'), 401

    access_token = (create_access_token(identity=str(doctor.doctor_id)))
    refresh_token = create_refresh_token(identity=str(doctor.doctor_id))

    return jsonify(
        response='Login successful',
        access_token=access_token,
        refresh_token=refresh_token
    ), 200


