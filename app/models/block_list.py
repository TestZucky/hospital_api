from datetime import datetime
from ..db import db

class TokenBlocklist(db.Model):
    __tablename__ = 'block_list'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
