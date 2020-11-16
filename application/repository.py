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
    # @staticmethod
    # def validate(roles, data):
    #     """
    #     check input data against roles
    #     :param roles:
    #     :param data:
    #     :return:
    #     """
    #     err_dict = {}
    #     for key in roles.keys():
    #         if key not in data and roles[key] == 'req':
    #             err_dict[key] = 'required field is missing'
    #     return err_dict if len(err_dict) > 0 else None

    @staticmethod
    def clean_data(roles, data):
        cd = dict()
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                raise Exception('{} is empty!'.format(key))
            if key in data:
                cd[key] = data[key]
        return data


class UserRepository(UserRepositoryBase):
    def __init__(self):
        self.register_roles = {
            'phone_number': 'req',
            'email': 'req',
            'password': 'req',
            # 'phone_number_is_validated': 'opt',
            # 'email_is_validated': 'opt',
            # 'join_date': 'opt',
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

    @staticmethod
    def _check_user_exist(**kwargs):
        from sqlalchemy import or_
        return db.session.query(User). \
            filter(or_(User.email == kwargs['email'],
                       User.phone_number == kwargs['phone_number'])). \
            first()

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

        old_user = self._check_user_exist(**clean_data)
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

    def update_user_profile(self, **kwargs):
        clean_data = Validator.clean_data(self.register_roles, kwargs)
        user = self._check_user_exist(clean_data)
        if user is None:
            raise Exception('user is not define!')

        if clean_data['email'] is not None and \
                clean_data['email'] != user.email:
            user.email = clean_data['email']
            user.email_is_validated = False
        if clean_data['first_name'] is not None:
            user.first_name = clean_data['first_name']
        if clean_data['last_name'] is not None:
            user.last_name = clean_data['last_name']
        if clean_data['avatar_url'] is not None:
            user.avatar_url = clean_data['avatar_url']
        if clean_data['personal_account_number'] is not None:
            user.personal_account_number = clean_data['personal_account_number']
        if clean_data['card_number'] is not None:
            user.card_number = clean_data['card_number']
        if clean_data['national_card'] is not None:
            user.national_card = clean_data['national_card']
        db.session.commit()

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
