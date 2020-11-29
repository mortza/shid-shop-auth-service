from . import db
import datetime


class Address(db.Model):
    def __init__(self, attributes=None):
        # ! set all input attr
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    district = db.Column(db.String(16))
    city = db.Column(db.String(16))
    state = db.Column(db.String(16))
    long = db.Column(db.Float)
    lat = db.Column(db.Float)
    address_text = db.Column(db.String(1024))
    post_code = db.Column(db.String(16))
    detail = db.JSON()

    @property
    def to_dict(self):
        return {
            'district', self.district,
            'city', self.city,
            'state', self.state,
            'long', self.long,
            'lat', self.lat,
            'address-text', self.address_text,
            'post-code', self.post_code,
            # 'detail', self.detail,
        }

    # @property
    # def __str__(self):
    #     return "ID: {},\n" \
    #            "User ID: {},\n" \
    #            "District: {},\n" \
    #            "City: {},\n" \
    #            "State: {},\n" \
    #            "Long: {},\n" \
    #            "Lat: {},\n" \
    #            "Address Text: {},\n" \
    #            "Post Code: {},\n" \
    #            "Detail: {},\n". \
    #         format(self.id,
    #                self.user_id,
    #                self.district,
    #                self.city,
    #                self.state,
    #                self.long,
    #                self.lat,
    #                self.address_text,
    #                self.post_code,
    #                self.detail
    #                )


class Token(db.Model):
    def __init__(self, user_id: int, device_info: dict):
        # ! set _user_id
        self.user_id = user_id
        # ! create and hashing and set _token ->
        import string
        import random
        s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
        from datetime import datetime
        now = datetime.now().time()
        t = '{}{}{}'.format(user_id, now, s)
        import hashlib
        self.token = hashlib.sha512(bytes(t, encoding='utf-8')).hexdigest()
        # ! <- create and hashing and set _token
        # ! set _user_information
        self.device_information = device_info

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(512), nullable=False, default='')
    device_information = db.JSON()

    @property
    def to_dict(self):
        return {
            'token': self.token,
            # 'device-information': self.device_information,
        }

    # @property
    # def __str__(self):
    #     return "ID:{},\n" \
    #            "User ID:{},\n" \
    #            "Token:{},\n" \
    #            "Device Information.". \
    #         format(self.id,
    #                self.user_id,
    #                self.token,
    #                self.device_information
    #                )


class VCode(db.Model):
    def __init__(self, user_id):
        self.user_id = user_id

        from random import randint
        from datetime import datetime, timedelta

        self.v_code_ph = randint(1000, 9999)
        self.v_code_e = randint(10000, 99999)
        self.validity_date = datetime.now() + timedelta(minutes=10)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    v_code_ph = db.Column(db.String(4))
    v_code_e = db.Column(db.String(6))
    validity_date = db.Column(db.DateTime)

    @property
    def to_dict(self):
        return {
            'verify-code-for-phone-number': self.v_code_ph,
            'verify-code-for-email': self.v_code_e,
            'validity-date': self.validity_date,
        }

    # @property
    # def __str__(self):
    #     return "ID:{},\n" \
    #            "User ID:{},\n" \
    #            "Phone Number Verify Code {} is valid until date {}.\n" \
    #            "Email Verify Code {} is valid until date {}.". \
    #         format(self.id,
    #                self.user_id,
    #                self.v_code_ph, self.validity_date,
    #                self.v_code_e, self.validity_date
    #                )


class User(db.Model):
    # ! set all input attr
    def __init__(self, attributes=None):
        if attributes is not None:
            for key, value in attributes.items():
                setattr(self, key, value)
        self._join_date = datetime.datetime.utcnow()
        self.last_password_hash = self.password

    # required
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(16), nullable=False, default='')
    real_or_legal = db.Column(db.String(16), nullable=False, default='')
    phone_number = db.Column(db.String(16), unique=True, nullable=False, default='09123456789')
    phone_number_is_validated = db.Column(db.Boolean, default=False, nullable=False)
    _password = db.Column(db.String(256), nullable=False, default='')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        from werkzeug.security import generate_password_hash
        self._password = generate_password_hash(value)

    _join_date = db.Column(db.DateTime)

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
        return self._answer

    @answer.setter
    def answer(self, value):
        from werkzeug.security import generate_password_hash
        self._answer = generate_password_hash(value)

    configurations = db.JSON()
    addresses = db.relationship('Address', backref='user', cascade="all, delete", lazy=True)
    tokens = db.relationship('Token', backref='user', cascade="all, delete", lazy=True)
    v_codes = db.relationship('VCode', backref='user', cascade="all, delete", lazy=True)

    @property
    def to_dict(self):
        return {
            'role': self.role,
            'real-or-legal': self.real_or_legal,
            'phone-number': self.phone_number,
            'phone-number-is-validated': self.phone_number_is_validated,
            'join-date': str(self._join_date),
            'email': self.email,
            'email-is-validated': self.email_is_validated,
            'company-name': self.company_name,
            # 'company-information': self.company_information,
            'first-name': self.first_name,
            'last-name': self.last_name,
            'avatar-url': self.avatar_url,
            'personal-account-number': self.personal_account_number,
            'card-number': self.card_number,
            'national-card': self.national_card,
            # 'configurations': self.configurations
        }

    # @property
    # def __str__(self):
    #     return "ID:{},\n" \
    #            "Role: {},\n" \
    #            "Real Or Legal: {},\n" \
    #            "Phone Number:{}-> is validated:{},\n" \
    #            "Password: {},\n" \
    #            "Join Date:{},\n" \
    #            "Email Address:{}->is validated:{},\n" \
    #            "Company Name:{},\n" \
    #            "Company information: {},\n" \
    #            "Name:{} {},\n" \
    #            "Avatar URL:{},\n" \
    #            "Personal Account Number:{},\n" \
    #            "Card Number:{},\n" \
    #            "National Card:{},\n" \
    #            "Last Password: {},\n" \
    #            "Answers: {},\n" \
    #            "Configurations: {},\n" \
    #            "Addresses: {},\n" \
    #            "Tokens: {},\n" \
    #            "VCodes: {},\n". \
    #         format(self.id,
    #                self.role,
    #                self.real_or_legal,
    #                self.phone_number, self.phone_number_is_validated,
    #                self.password,
    #                self._join_date,
    #                self.email, self.email_is_validated,
    #                self.company_name,
    #                self.company_information,
    #                self.first_name, self.last_name,
    #                self.avatar_url,
    #                self.personal_account_number,
    #                self.card_number,
    #                self.national_card,
    #                self.last_password_hash,
    #                self.answer,
    #                self.configurations,
    #                self.addresses,
    #                self.tokens,
    #                self.v_codes
    #                )
