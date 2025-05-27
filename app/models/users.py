from ..db import db

class User(db.Model):
    __tablename__ = 'user_information'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(1000), nullable=False)
    user_city = db.Column(db.String(50), nullable=False)
    user_state = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(10), nullable=False)
