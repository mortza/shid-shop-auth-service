from repository.users import UserRepositoryBase
from .models import User, ValidationCode
from . import db


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
        cd = dict()
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                raise Exception('{} is empty!'.format(key))
            cd[key] = data[key]
        return data

class UserRepository(UserRepositoryBase):
    def __init__(self):
        self.register_roles = {
            'email': 'req',
            'phone_number': 'req',
            'password': 'req',
        }

    @staticmethod
    def _check_user_exist(**kwargs):
        from sqlalchemy import or_
        return db.session.query(User). \
            filter(or_(User.email == kwargs['email'],
                       User.phone_number == kwargs['phone_number'])). \
            first()

    @staticmethod
    def _make_phone_number_validation(user):
        from random import randint
        from datetime import datetime, timedelta

        v = ValidationCode()
        v.user_id = user.id
        v.validation_code = randint(1000, 9999)
        v.valid_until = datetime.now() + timedelta(minutes=10)
        db.session.add(v)
        db.session.commit()
        db.create_all()
        # send SMS
        # Your activation Code is: v.validation_code

    def validate_phone_number(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        pass

    def register(self, **kwargs):
        validation_result = Validator.validate(self.register_roles, kwargs)
        if validation_result is not None:
            # data is not complete
            return validation_result
        old_user = self._check_user_exist(**kwargs)
        if old_user is not None:
            raise Exception('Email or phone number is taken')
        user = User(kwargs)

        db.session.add(user)
        db.session.commit()
        db.create_all()
        # send SMS
        self._make_phone_number_validation(user)
        return user.to_dict

    def update_user_profile(self, **kwargs):
        user = self._check_user_exist(**kwargs)
        if user is None:
            raise Exception('user is not define!')


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
