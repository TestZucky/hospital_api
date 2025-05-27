from ..db import db

class Store(db.Model):

    __tablename__ = 'store_information'

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_name = db.Column(db.String(100), nullable=False)
    store_landmark = db.Column(db.String(50), nullable=False)
    store_city = db.Column(db.String(50), nullable=False)
    store_state = db.Column(db.String(50), nullable=False)
    store_owner = db.Column(db.String(100), nullable=False)
    store_zip_code = db.Column(db.String(6), nullable=False)
    store_active = db.Column(db.Boolean, nullable=False)
