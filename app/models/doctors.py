from ..db import db

class Doctor(db.Model):

    __tablename__ = 'doctor_information'

    doctor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_name = db.Column(db.String(100), nullable=False)
    doctor_email = db.Column(db.String(150), unique=True, nullable=False)
    doctor_password = db.Column(db.String(255), nullable=False)
    doctor_active = db.Column(db.Boolean, nullable=False, default=True)
    user_role = db.Column(db.String(10), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey('store_information.store_id'), nullable=False)
    store = db.relationship('Store', back_populates='doctors')