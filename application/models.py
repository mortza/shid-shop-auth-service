"""
    Data models.
"""
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(11), unique=True)
    phone_number_is_validated = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))

    first_name = db.Column(db.String(50), default='')
    last_name = db.Column(db.String(50), default='')

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number,
            'phone_is_valid': self.phone_number_is_validated,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)


class ValidationCode(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, default=0)
    validation_code = db.Column(db.String(10), default='')
    valid_until = db.Column(db.DateTime, nullable=True)

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'validation_code': self.validation_code,
            'valid_until': self.valid_until,
        }
