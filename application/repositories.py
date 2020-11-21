from repository.users import UserRepositoryBase
from application.models import User, Token
from application import db, redis_client
from repository import error_codes

from application.validators import UserValidator
from application.exceptions import UserException


class UserRepository(UserRepositoryBase):
    def __init__(self):
        # ! define roles. data extraction for registering
        self.register_roles = {
            'phone_number': 'req',
            'password': 'req',
            'email': 'opt',
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
        # ! define roles. data extraction for updating
        self.update_roles = {
            'user_name': 'req',
            'phone_number': 'opt',
            'email': 'opt',
            'password': 'opt',
            'first_name': 'opt',
            'last_name': 'opt',
            'avatar_url': 'opt',
            'personal_account_number': 'opt',
            'card_number': 'opt',
            'national_card': 'opt',
            'configurations': 'opt',
        }
        # ! define roles. data extraction for login
        self.login_roles = {
            'user_name': 'req',
            'password': 'req',
        }
        # ! define roles. data extraction for logout
        self.logout_roles = {
            'user_name': 'req',
        }

    @staticmethod
    def _check_user_exist(user_name: str) -> User:
        from sqlalchemy import or_
        return db.session.query(User). \
            filter(or_(User.email == user_name,
                       User.phone_number == user_name)). \
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
        # ! extract data ->
        data = UserValidator.clean_data(self.register_roles, kwargs)
        # ! check for user not exist ->
        old_user = self._check_user_exist(data['user_name'])
        if old_user is not None:
            raise UserException(message=error_codes.USER_ALREADY_EXIST_MESSAGE,
                                error_code=error_codes.USER_ALREADY_EXIST_CODE)
        # ! <- check for user not exist
        # ! define and create new User
        user = User(data)
        # ! update db ->
        db.session.add(user)
        db.session.commit()
        db.create_all()
        # ! <- update db
        # send SMS
        # self._make_phone_number_validation(user)
        return user.to_dict

    def update(self, **kwargs):
        # ! extract data and user ->
        data = UserValidator.clean_data(self.update_roles, kwargs)
        user = UserRepository._check_user_exist(data['user_name'])
        # ! <- extract data and user
        # ! check for user exist
        if user is None:
            raise UserException(message=error_codes.USER_NOT_EXIST_MESSAGE,
                                error_code=error_codes.USER_NOT_EXIST_CODE)
        # ! update user ->
        if 'phone_number' in data:
            user.phone_number_is_validated = False
            user.phone_number = data['phone_number']
        if 'email' in data:
            user.email_is_validated = False
            user.email = data['email']
        if 'password' in data:
            user.last_password_hash = user.password
            user.password = data['password']
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'avatar_url' in data:
            user.avatar_url = data['avatar_url']
        if 'personal_account_number' in data:
            user.personal_account_number = data['personal_account_number']
        if 'card_number' in data:
            user.card_number = data['card_number']
        if 'national_card' in data:
            user.national_card = data['national_card']
        # ! <- update user
        # ! update db
        db.session.commit()

        # ! disconnect all device for update redis
        tokens = db.session.query(Token).filter(Token.user_id == user.id).all()
        db.session.query(Token).filter(Token.user_id == user.id).delete()
        db.session.commit()
        return tokens

    def login(self, **kwargs):
        # ! extract data and user ->
        data = UserValidator.clean_data(self.login_roles, kwargs)
        user = UserRepository._check_user_exist(data['user_name'])
        # ! <- extract data and user
        # ! check for user exist
        if user is None:
            raise UserException(message=error_codes.USER_NOT_EXIST_MESSAGE,
                                error_code=error_codes.USER_NOT_EXIST_CODE)
        # ! check input password with user.password(hashed) ->
        from werkzeug.security import check_password_hash
        if not check_password_hash(user.password, data['password']):
            raise UserException(message=error_codes.WRONG_PASSWORD_ENTERED_MESSAGE,
                                error_code=error_codes.WRONG_PASSWORD_ENTERED_CODE)
        # todo add device info
        tkn = Token(user_id=user.id, device_info=user.to_dict)
        db.session.add(tkn)
        db.session.commit()
        return tkn.token, user.to_dict
        # ! <- check input password with user.password(hashed)

    def logout(self, **kwargs):
        token = kwargs['token']
        db.session.query(Token).filter(Token.token == token).delete()
        db.session.commit()
        return token
# def logout(self, **kwargs):
#     # ! extract data and user ->
#     data = UserValidator.clean_data(self.login_roles, kwargs)
#     user = UserRepository._check_user_exist(data['user_name'])
#     # ! <- extract data and user
#     # ! check for user exist
#     if user is None:
#         raise UserException(message=error_codes.USER_ALREADY_NOT_EXIST_MESSAGE,
#                             error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
#     # ! reset login_is_validate for logout
#     user.login_is_validate = False
#     # ! update db
#     db.session.commit()
#     return True
#
# def getUser(self, **kwargs):
#     # ! extract data and user ->
#     data = UserValidator.clean_data(self.login_roles, kwargs)
#     user = UserRepository._check_user_exist(data['user_name'])
#     # ! <- extract data and user
#     # ! check for user exist
#     if user is None:
#         raise UserException(message=error_codes.USER_ALREADY_NOT_EXIST_MESSAGE,
#                             error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
#     # ! check user is login
#     if user.login_is_validate:
#         return user.to_dict
#     return {}

# def delete(self, **kwargs):
#     [user, ] = self._current_user(kwargs)
#     if user.login_is_validate:
#         db.session.delete(user)
#         db.session.commit()
#     raise UserException(message=error_codes.USER_IS_NOT_LOGIN_MESSAGE,
#                         error_code=error_codes.USER_IS_NOT_LOGIN_CODE)
