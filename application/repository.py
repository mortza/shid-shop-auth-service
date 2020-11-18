from repository.users import UserRepositoryBase
from .models import User, ValidationCode
from . import db
from repository import error_codes


class UserRepositoryException(Exception):
    def __init__(self, **kwargs):
        super(UserRepositoryException, self).__init__()
        self.message = kwargs['message'] if 'message' in kwargs else ''
        self.error_code = kwargs['error_code'] if 'error_code' in kwargs else -1


class Validator:
    @staticmethod
    def clean_data(roles, data) -> dict:
        cd = dict()
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                raise UserRepositoryException(message='{}::{}'.format(key, error_codes.USER_ALREADY_NOT_EXIST_CODE),
                                              error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
            if key in data:
                cd[key] = data[key]
        return data


class UserRepository(UserRepositoryBase):
    def __init__(self):
        self.register_roles = {
            'phone_number': 'req',
            'email': 'req',
            'password': 'req',
            'first_name': 'opt',
            'last_name': 'opt',
            'avatar_url': 'opt',
            'personal_account_number': 'opt',
            'card_number': 'opt',
            'national_card': 'opt',
            'last_password': 'opt',
            'q1': 'opt',
            'q2': 'opt',
            'q3': 'opt',
            'q4': 'opt',
            'q5': 'opt',
            'configurations': 'opt',
        }
        self.update_roles = {
            'phone_number': 'req',
            'first_name': 'opt',
            'last_name': 'opt',
            'avatar_url': 'opt',
            'personal_account_number': 'opt',
            'card_number': 'opt',
            'national_card': 'opt',
        }
        self.login_roles = {
            'phone_number': 'req',
            'email': 'opt',
            'password': 'req',
        }

    @staticmethod
    def _check_user_exist(kwargs, by='both') -> User:
        from sqlalchemy import or_
        if by == 'both':
            return db.session.query(User). \
                filter(or_(User.email == kwargs['email'],
                           User.phone_number == kwargs['phone_number'])). \
                first()
        if by == 'phone_number':
            return db.session.query(User). \
                filter(User.phone_number == kwargs['phone_number']).first()
        if by == 'email':
            return db.session.query(User). \
                filter(User.phone_number == kwargs['email']).first()

    # @staticmethod
    # def _make_phone_number_validation(user):
    #     from random import randint
    #     from datetime import datetime, timedelta
    #
    #     v = ValidationCode()
    #     v.user_id = user.id
    #     v.validation_code = randint(1000, 9999)
    #     v.valid_until = datetime.now() + timedelta(minutes=10)
    #     db.session.add(v)
    #     db.session.commit()
    #     db.create_all()
    #     # send SMS
    #     # Your activation Code is: v.validation_code
    #
    # @staticmethod
    # def _make_email_validation(user):
    #     from random import randint
    #     from datetime import datetime, timedelta
    #
    #     v = ValidationCode()
    #     v.user_id = user.id
    #     v.validation_code = randint(1000, 9999)
    #     v.valid_until = datetime.now() + timedelta(minutes=10)
    #     db.session.add(v)
    #     db.session.commit()
    #     db.create_all()
    #     # send SMS
    #     # Your activation Code is: v.validation_code
    #
    # def validate_phone_number(self, **kwargs):
    #     """
    #
    #     :param kwargs:
    #     :return:
    #     """
    #     pass

    def register(self, **kwargs):
        clean_data = Validator.clean_data(self.register_roles, kwargs)

        old_user = self._check_user_exist(clean_data)
        if old_user is not None:
            raise UserRepositoryException(message=error_codes.USER_ALREADY_EXIST_MESSAGE,
                                          error_code=error_codes.USER_ALREADY_EXIST_CODE)
        user = User(clean_data)
        db.session.add(user)
        db.session.commit()
        db.create_all()
        # send SMS
        # self._make_phone_number_validation(user)
        return user.to_dict

    @staticmethod
    def _update_user_profile(data: dict, user: User) -> dict:
        if data['first_name'] is not None:
            user.first_name = data['first_name']
        if data['last_name'] is not None:
            user.last_name = data['last_name']
        if data['avatar_url'] is not None:
            user.avatar_url = data['avatar_url']
        if data['personal_account_number'] is not None:
            user.personal_account_number = data['personal_account_number']
        if data['card_number'] is not None:
            user.card_number = data['card_number']
        if data['national_card'] is not None:
            user.national_card = data['national_card']
        db.session.commit()
        return user.to_dict

    @staticmethod
    def _update_user_password(data: dict, user: User) -> dict:
        pass

    @staticmethod
    def _update_user_email(data: dict, user: User) -> dict:
        pass

    def update(self, **kwargs):
        clean_data = Validator.clean_data(self.update_roles, kwargs)
        user = self._check_user_exist(clean_data)
        if user is None:
            raise UserRepositoryException(message=error_codes.USER_ALREADY_NOT_EXIST_CODE,
                                          error_code=error_codes.USER_ALREADY_NOT_EXIST_MESSAGE)
        if user.login_is_validate is False:
            raise UserRepositoryException(message=error_codes.USER_IS_NOT_LOGIN_CODE,
                                          error_code=error_codes.USER_IS_NOT_LOGIN_MESSAGE)

        return self._update_user_profile(clean_data, user)

    @staticmethod
    def _checked_for_login(data: dict, user: User) -> bool:
        from werkzeug.security import check_password_hash
        if check_password_hash(user.password, data['password']):
            user.login_is_validate = True
            db.session.commit()
            return True
        return False

    def login(self, **kwargs):
        clean_data = Validator.clean_data(self.register_roles, kwargs)
        user = self._check_user_exist(clean_data)
        if user is None:
            raise UserRepositoryException(message=error_codes.USER_ALREADY_NOT_EXIST_CODE,
                                          error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
        return self._checked_for_login(clean_data, user)
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
