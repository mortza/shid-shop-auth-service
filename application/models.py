"""
    Data models.
"""
from . import db
import datetime


class Address(db.Model):
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.foreign('user.id'), nullable=False)
    district = db.Column(db.String(16))
    city = db.Column(db.String(16))
    state = db.Column(db.String(16))
    long = db.Column(db.Float)
    lat = db.Column(db.Float)
    adres = db.Column(db.String(512))
    post_code = db.Column(db.String(16))
    detail = db.JSON()


class Token(db.Model):
    def __init__(self, user_id: int, device_info: dict):
        # ! set _user_id
        self.user_id = user_id
        # ! create and hashing and set _token ->
        from datetime import datetime
        now = datetime.now().time()
        t = '{}{}'.format(user_id, now)
        import hashlib
        self.token = hashlib.sha512(bytes(t, encoding='utf-8')).hexdigest()
        # ! <- create and hashing and set _token
        # ! set _user_information
        self.device_information = device_info

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(512), nullable=False, default='')
    device_information = db.JSON()


class User(db.Model):
    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)

    # required
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(1), nullable=False, default='s')  # s := seller , t := storekeeper or a := admin
    real_or_legal = db.Column(db.String(1), nullable=False, default='r')  # r := real or l := legal
    phone_number = db.Column(db.String(16), unique=True, nullable=False, default='0912-345-6789')
    phone_number_is_validated = db.Column(db.Boolean, default=False, nullable=False)
    _password = db.Column(db.String(256), nullable=False, default='')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        from werkzeug.security import generate_password_hash
        self._password = generate_password_hash(value)

    _join_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # optional
    email = db.Column(db.String(128), unique=True, default='example@example.example')
    email_is_validated = db.Column(db.Boolean, default=False, nullable=False)
    company_name = db.Column(db.String(64))
    company_information = db.JSON()
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    avatar_url = db.Column(db.String(256))
    personal_account_number = db.Column(db.String(64))
    card_number = db.Column(db.String(32))
    national_card = db.Column(db.String(32))
    # extra
    last_password_hash = db.Column(db.String(127))

    _answer = db.Column(db.String(1024))

    @property
    def answer(self):
        return self._password

    @answer.setter
    def answer(self, value):
        from werkzeug.security import generate_password_hash
        self._answer = generate_password_hash(value)

    configurations = db.JSON()

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
                   str(self._join_date),
                   self.first_name, self.last_name,
                   self.avatar_url,
                   self.personal_account_number,
                   self.card_number,
                   self.national_card
                   )

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
    def __init__(self, user_id):
        self.user_id = user_id
        from random import randint
        from datetime import datetime, timedelta
        self.validation_code = randint(1000, 9999)
        self.valid_until = datetime.now() + timedelta(minutes=10)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    validation_code = db.Column(db.String(10))
    valid_until = db.Column(db.DateTime)

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'validation_code': self.validation_code,
            'valid_until': self.valid_until,
        }
