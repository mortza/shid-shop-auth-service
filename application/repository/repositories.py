from repository.users import UserRepositoryBase
from application.models import User, ValidationCode
from application import db
from repository import error_codes

from .validators import UserValidator
from .exceptions import UserException


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

    @staticmethod
    def _current_user(kwargs) -> User:
        data = UserValidator.clean_data(UserRepository.register_roles, kwargs)
        user = UserRepository._check_user_exist(data)
        if user is None:
            raise UserException(message=error_codes.USER_ALREADY_NOT_EXIST_MESSAGE,
                                error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
        return [user, data]

    def register(self, **kwargs):
        clean_data = UserValidator.clean_data(self.register_roles, kwargs)

        old_user = self._check_user_exist(clean_data)
        if old_user is not None:
            raise UserException(message=error_codes.USER_ALREADY_EXIST_MESSAGE,
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
        [user, data] = self._current_user(kwargs)
        if user.login_is_validate is False:
            raise UserException(message=error_codes.USER_IS_NOT_LOGIN_CODE,
                                error_code=error_codes.USER_IS_NOT_LOGIN_MESSAGE)

        update_type = kwargs['update_type']

        if update_type == 'profile':
            return self._update_user_profile(data, user)
        if update_type == 'password':
            return self._update_user_password(data, User)
        if update_type == 'email':
            return self._update_user_email(data, user)

        raise UserException(message=error_codes.UPDATE_TYPE_IS_NOT_DEFINE_CODE,
                            error_code=error_codes.UPDATE_TYPE_IS_NOT_DEFINE_MESSAGE)

    def login(self, **kwargs):
        [user, data] = self._current_user(kwargs)
        from werkzeug.security import check_password_hash
        if check_password_hash(user.password, data['password']):
            user.login_is_validate = True
            db.session.commit()
            return True
        return False

    # def logout(self, **kwargs):
    #     [user, ] = self._current_user(kwargs)
    #     user.login_is_validate = False
    #     db.session.commit()
    #     return True
    #
    # def getUser(self, **kwargs):
    #     [user, ] = self._current_user(kwargs)
    #     if user.login_is_validate:
    #         return user.to_dict
    #     return {}
    #
    # def delete(self, **kwargs):
    #     [user, ] = self._current_user(kwargs)
    #     if user.login_is_validate:
    #         db.session.delete(user)
    #         db.session.commit()
    #     raise UserException(message=error_codes.USER_IS_NOT_LOGIN_MESSAGE,
    #                         error_code=error_codes.USER_IS_NOT_LOGIN_CODE)