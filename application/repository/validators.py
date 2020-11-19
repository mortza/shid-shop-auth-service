from application.repository import UserException
from repository import error_codes


class UserValidator:
    @staticmethod
    def clean_data(roles, data) -> dict:
        cd = dict()
        cd['user_name'] = None
        for key in roles.keys():
            if key not in data and roles[key] == 'req':
                raise UserException(message='{}::{}'.format(key, error_codes.USER_ALREADY_NOT_EXIST_MESSAGE),
                                    error_code=error_codes.USER_ALREADY_NOT_EXIST_CODE)
            if key in data:
                cd[key] = data[key]
        if cd['user_name'] is None:
            cd['user_name'] = cd['phone_number']
        return cd
