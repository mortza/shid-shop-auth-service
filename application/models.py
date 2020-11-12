"""Data models."""
from werkzeug.routing import ValidationError

from . import db

from repository.users import UserRepositoryBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(11), unique=True)
    phone_number_is_validated = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    first_name = db.Column(db.String(50), default='')

    @property
    def phone_is_valid(self):
        return self.phone_number_is_validated

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "phone_is_valid": self.phone_is_valid,
            "first_name": self.first_name,
            "password": self.password,
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


class Validator:
    @staticmethod
    def validate(roles, data):
        """
        check input data against roles
        :param roles:
        :param data:
        :return:
        """
        err_dict = {}
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                err_dict[key] = 'required field is missing'
        return err_dict if len(err_dict) > 0 else None

    @staticmethod
    def clean_data(roles, data):
        pass


class UserRepository(UserRepositoryBase):
    def __init__(self):
        self.register_roles = {
            'email': 'req',
            'phone_number': 'req',
            'password': 'req',
        }

    def register(self, **kwargs):
        validation_result = Validator.validate(self.register_roles, kwargs)
        if validation_result is not None:
            # data is not complete
            return validation_result

        user = User()
        user.phone_number = kwargs['phone_number']
        user.email = kwargs['email']
        user.password = generate_password_hash(kwargs['password'])

        db.session.add(user)
        db.session.commit()
        db.create_all()
        return user.to_dict

    # def get_user(self, password, email=None, phone_number=None) -> dict:
    #     qb = {}
    #
    #     if phone_number is None and email is None:
    #         return {}
    #     if email is None:
    #         qb['phone_number'] = phone_number
    #     else:
    #         qb['email'] = email
    #     user = db.session.query(User).filter_by(**qb).first()
    #     return user.to_dict if user is not None else {}

    def update_user(self, **kwargs):
        pass

    def delete_user(self, **kwargs):
        pass
