from . import db
import datetime
import json
import uuid


class Address(db.Model):
    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String(512), unique=False, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    address = db.Column(db.JSON, default='{}')

    @property
    def to_dict(self):
        return {
            "address": json.loads(self.address)
        }

    def __str__(self):
        return "ID: {},\n" \
               "User ID: {},\n" \
               "Address: {},\n". \
            format(self.id,
                   self.user_id,
                   self.address
                   )


class Token(db.Model):
    def __init__(self, user_id: int, info: dict):
        setattr(self, 'user_id', user_id)
        setattr(self, 'information', info)

        import string
        import random

        s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))

        from datetime import datetime

        now = datetime.now().time()
        t = '{}{}{}'.format(user_id, now, s)

        import hashlib

        setattr(self, 'token', hashlib.sha512(bytes(t, encoding='utf-8')).hexdigest())

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String(512), unique=False, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(512), nullable=False)
    information = db.Column(db.JSON)

    @property
    def to_dict(self):
        return {
            "token": self.token,
            "device-information": json.loads(self.device_information),
        }

    def __str__(self):
        return "ID:{},\n" \
               "User ID:{},\n" \
               "Token:{},\n" \
               "Device Information.". \
            format(self.id,
                   self.user_id,
                   self.token,
                   self.device_information
                   )


class VCode(db.Model):
    def __init__(self, user_id):
        setattr(self, 'user_id', user_id)

        from random import randint
        from datetime import datetime, timedelta

        setattr(self, 'v_code_ph', randint(1000, 9999))
        setattr(self, 'v_code_e', randint(10000, 99999))
        setattr(self, 'validity_date', datetime.now() + timedelta(minutes=10))

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String(512), unique=False, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    v_code_ph = db.Column(db.String(4))
    v_code_e = db.Column(db.String(6))
    validity_date = db.Column(db.DateTime)

    @property
    def to_dict(self):
        return {
            "verify_code_for_phone_number": self.v_code_ph,
            "verify_code_for_email": self.v_code_e,
            "validity_date": self.validity_date,
        }

    def __str__(self):
        return "ID:{},\n" \
               "User ID:{},\n" \
               "Phone Number Verify Code {} is valid until date {}.\n" \
               "Email Verify Code {} is valid until date {}.". \
            format(self.id,
                   self.user_id,
                   self.v_code_ph, self.validity_date,
                   self.v_code_e, self.validity_date
                   )


class User(db.Model):
    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)
        from uuid import uuid4
        setattr(self, 'uid', str(uuid4()))
        setattr(self, '_join_date', datetime.datetime.utcnow())
        self.last_password_hash = self.password

    # required
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    guid = db.Column(db.String(512), unique=False, default=uuid.uuid4)
    uid = db.Column(db.String(50), unique=True)
    role = db.Column(db.String(16), nullable=False)
    real_or_legal = db.Column(db.String(16), nullable=False)
    phone_number = db.Column(db.String(16), unique=True)
    phone_number_is_validated = db.Column(db.Boolean, default=False)
    _password = db.Column(db.String(256), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        from werkzeug.security import generate_password_hash
        self._password = generate_password_hash(value)

    _join_date = db.Column(db.DateTime)

    # optional
    email = db.Column(db.String(128), unique=True)
    email_is_validated = db.Column(db.Boolean, default=False)
    user_information = db.Column(db.JSON, default='{}')
    company_information = db.Column(db.JSON, default='{}')
    # extra
    last_password_hash = db.Column(db.String(127))
    _answers = db.Column(db.String(1024))

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        from werkzeug.security import generate_password_hash
        self._answers = generate_password_hash(value)

    configurations = db.Column(db.JSON, default='{}')

    addresses = db.relationship('Address', backref='user', cascade="all, delete", lazy=True)
    tokens = db.relationship('Token', backref='user', cascade="all, delete", lazy=True)
    v_codes = db.relationship('VCode', backref='user', cascade="all, delete", lazy=True)

    @property
    def to_dict(self):
        return {
            'uuid': self.uid,
            'role': self.role,
            'real_or_legal': self.real_or_legal,
            'phone_number': self.phone_number,
            'phone_number_is_validated': self.phone_number_is_validated,
            'join_date': str(self._join_date),
            'email': self.email,
            'email_is_validated': self.email_is_validated,
            'user_information': json.loads(self.user_information),
            'company_information': json.loads(self.company_information),
            'configurations': json.loads(self.configurations),
        }

    @property
    def address_list(self):
        addresses = dict()
        for address in self.addresses:
            addresses['address id = {}'.format(address.id)] = address.address
        return addresses

    @property
    def session_list(self):
        sessions = dict()
        for session in self.tokens:
            sessions['token = {}'.format(session.token)] = session.device_information
        return sessions

    def __str__(self):
        return "ID:{},\n" \
               "Role: {},\n" \
               "Real Or Legal: {},\n" \
               "Phone Number:{}-> is validated:{},\n" \
               "Password: {},\n" \
               "Join Date:{},\n" \
               "Email Address:{}->is validated:{},\n" \
               "User Information:{},\n" \
               "Company information: {},\n" \
               "Last Password: {},\n" \
               "Answers: {},\n" \
               "Configurations: {},\n" \
               "Addresses: {},\n" \
               "Tokens: {},\n" \
               "VCodes: {},\n". \
            format(self.id,
                   self.role,
                   self.real_or_legal,
                   self.phone_number, self.phone_number_is_validated,
                   self.password,
                   self._join_date,
                   self.email, self.email_is_validated,
                   self.user_information,
                   self.company_information,
                   self.last_password_hash,
                   self.answers,
                   self.configurations,
                   self.addresses,
                   self.tokens,
                   self.v_codes
                   )
