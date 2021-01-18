from . import db
import datetime
import json


# class Address(db.Model):
#     def __init__(self, attributes=None):
#         if attributes is not None:
#             for key, value in attributes.items():
#                 setattr(self, key, value)
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     address = db.Column(db.JSON, default='{}')
#
#     @property
#     def to_dict(self):
#         return {
#             "address": json.loads(self.address)
#         }
#
#     def __str__(self):
#         return "ID: {},\n" \
#                "User ID: {},\n" \
#                "Address: {},\n". \
#             format(self.id,
#                    self.user_id,
#                    self.address
#                    )


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
        setattr(self, 'validity_date', datetime.now() + timedelta(days=1))

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

    configurations = db.Column(db.JSON, default='{}')

    # addresses = db.relationship('Address', backref='user', cascade="all, delete", lazy=True)
    tokens = db.relationship('Token', backref='user', cascade="all, delete", lazy=True)
    v_codes = db.relationship('VCode', backref='user', cascade="all, delete", lazy=True)

    username = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    national_id = db.Column(db.String(64), unique=True)
    gender = db.Column(db.String(64))
    birthday = db.Column(db.String(16))

    company_name = db.Column(db.String(64), unique=True)
    economic_code = db.Column(db.String(32), unique=True)
    national_id_company_owner = db.Column(db.String(32), unique=True)
    registration_id = db.Column(db.String(32), unique=True)

    question_answring_1 = db.Column(db.JSON)
    question_answring_2 = db.Column(db.JSON)
    question_answring_3 = db.Column(db.JSON)
    question_answring_4 = db.Column(db.JSON)
    question_answring_5 = db.Column(db.JSON)

    sms_num = db.Column(db.Integer(), default=0)
    sms_num_deth_time = db.Column(db.DateTime)

    @property
    def set_sms_num(self):
        import datetime
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        self.sms_num = self.sms_num + 1
        self.sms_num_deth_time = now + delta

    @property
    def check_send_sms(self):
        import datetime
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        if self.sms_num_deth_time < now:
            self.sms_num = 0
            self.sms_num_deth_time = now + delta
            return True
        if self.sms_num <= 2:
            return True
        return False

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
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'national_id': self.national_id,
            'gender': self.gender,
            'birthday': self.birthday,
            'company_name': self.company_name,
            'economic_code': self.economic_code,
            'national_id_company_owner': self.national_id_company_owner,
            'registration_id': self.registration_id,
        }

    # @property
    # def address_list(self):
    #     addresses = dict()
    #     for address in self.addresses:
    #         addresses['{}'.format(address.id)] = address.address
    #     return addresses

    @property
    def session_list(self):
        sessions = dict()
        for session in self.tokens:
            sessions['{}'.format(session.token)] = session.information
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
               "Configurations: {},\n" \
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
                   self.configurations,
                   # self.addresses,
                   self.tokens,
                   self.v_codes,
                   )
