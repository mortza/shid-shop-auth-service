from .exceptions import UserException
from repository import error_codes


class UserValidator:
    @staticmethod
    def clean_data(roles, data) -> dict:
        cd = dict()
        cd['user_name'] = None
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                raise UserException(message='{}::{}'.format(key, error_codes.USER_NOT_EXIST_MESSAGE),
                                    error_code=error_codes.USER_NOT_EXIST_CODE)
            if key in data:
                cd[key] = data[key]
        if cd['user_name'] is None:
            if 'phone_number' in cd:
                cd['user_name'] = cd['phone_number']
            elif 'email' in cd:
                cd['user_name'] = cd['email']
        return cd
