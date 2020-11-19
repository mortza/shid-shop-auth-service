"""
    Data models.
"""
from . import db
import datetime


class Token(db.Model):
    def __init__(self, user_id: int, user_info: dict):
        # ! set _user_id
        self._user_id = user_id
        # ! create and hashing and set _token ->
        from datetime import datetime
        now = datetime.now().time()
        t = '{}{}'.format(user_id, now)
        from werkzeug.security import generate_password_hash
        self._token = generate_password_hash(t)
        # ! <- create and hashing and set _token
        # ! set _user_information
        self._user_information = user_info

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    _token = db.Column(db.String(512), nullable=False, default='')
    _device_information = db.JSON()

    @property
    def user_id(self):
        return self.user_id

    @property
    def token(self):
        return self._token

    @property
    def device_information(self):
        return self._device_information


class User(db.Model):
    # required
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(16), unique=True, nullable=False, default='0912-345-6789')
    phone_number_is_validated = db.Column(db.Boolean, default=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False, default='example@example.example')
    email_is_validated = db.Column(db.Boolean, default=False, nullable=False)
    _password = db.Column(db.String(256), nullable=False, default='')
    join_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    login_is_validate = db.Column(db.Boolean, default=False, nullable=False)
    # optional
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    avatar_url = db.Column(db.String(256))
    personal_account_number = db.Column(db.String(64))
    card_number = db.Column(db.String(32))
    national_card = db.Column(db.String(32))
    # extra
    last_password_hash = db.Column(db.String(127))
    q1 = db.Column(db.String(127))
    q2 = db.Column(db.String(127))
    q3 = db.Column(db.String(127))
    q4 = db.Column(db.String(127))
    q5 = db.Column(db.String(127))
    configurations = db.JSON()

    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)

    def __str__(self):
        return "ID:{},\n" \
               "Phone Number:{}-> is validated:{},\n" \
               "Email Address:{}->is validated:{},\n" \
               "Join Date:{},\n" \
               "Name:{} {},\n" \
               "Avatar:{},\n" \
               "Personal Account Number:{},\n" \
               "Card Number:{},\n" \
               "National Card:{}\n". \
            format(self.id,
                   self.phone_number, self.phone_number_is_validated,
                   self.email, self.email_is_validated,
                   str(self.join_date),
                   self.first_name, self.last_name,
                   self.avatar_url,
                   self.personal_account_number,
                   self.card_number,
                   self.national_card
                   )

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        from werkzeug.security import generate_password_hash
        self._password = generate_password_hash(value)

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number,
            'phone_is_valid': self.phone_number_is_validated,
            'email': self.email,
            'email_is_validated': self.email_is_validated,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }


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
