from repository.exceptions import InputException
from repository import error_codes


class AcceptableData:
    # input rules
    # signup
    input_singup_rules = {
        'role': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'real_or_legal': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'phone_number': {
            'nullable': False,
            'max_length': 11,
            'min_length': 11,
            'type': 'snum'
        },
        'password': {
            'nullable': False,
            'max_length': None,
            'min_length': 8,
            'type': 'str'
        },
        'email': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'email'
        },
        'user_info': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'json'
        },
        'company_info': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'answers': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'json'
        },
        'configurations': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'json'
        },
    }
    # login
    input_login_rules = {
        'user_name': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'password': {
            'nullable': False,
            'max_length': None,
            'min_length': 8,
            'type': 'str'
        },
    }
    # logout
    input_logout_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
    }
    # update
    input_phone_number_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'phone_number': {
            'nullable': False,
            'max_length': 11,
            'min_length': 11,
            'type': 'snum'
        },
    }
    input_password_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'password': {
            'nullable': False,
            'max_length': None,
            'min_length': 8,
            'type': 'str'
        },
    }
    input_email_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'email': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'email'
        },
    }
    input_user_info_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'user_info': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'json'
        },
    }
    input_company_info_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'company_info': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
    }
    input_configurations_update_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'configurations': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'json'
        },
    }
    # forget password
    input_account_recovery_by_send_sms_rules = {
        'phone_number': {
            'nullable': False,
            'max_length': 11,
            'min_length': 11,
            'type': 'snum'
        },
    }
    input_account_recovery_by_send_email_rules = {
        'email': {
            'nullable': True,
            'max_length': None,
            'min_length': None,
            'type': 'email'
        },
    }
    input_account_recovery_by_last_password_rules = {
        'user_name': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'last_password': {
            'nullable': False,
            'max_length': None,
            'min_length': 8,
            'type': 'str'
        },
    }
    input_account_recovery_by_answers_rules = {
        'user_name': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'answers': {
            'nullable': False,
            'max_length': None,
            'min_length': 8,
            'type': 'json'
        },
    }
    # delete account
    input_delete_account_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
    }
    # generate and send vcode
    input_generate_and_send_vcode_to_activate_phone_number_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
    }
    input_generate_and_email_vcode_to_activate_email_address_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
    }
    # confirm the received vcode
    input_confirm_the_received_vcode_to_activate_the_email_address_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'vcode': {
            'nullable': False,
            'max_length': 5,
            'min_length': 5,
            'type': 'snum'
        }
    }
    input_confirm_the_received_vcode_to_activate_the_phone_number_rules = {
        'token': {
            'nullable': False,
            'max_length': None,
            'min_length': None,
            'type': 'str'
        },
        'vcode': {
            'nullable': False,
            'max_length': 4,
            'min_length': 4,
            'type': 'snum'
        }
    }

    # output rules
    # all data
    output_return_user_all_data = {
        'token': {
            'nullable': False,
            'type': 'str'
        },
        'role': {
            'nullable': False,
            'type': 'str'
        },
        'real_or_legal': {
            'nullable': False,
            'type': 'str'
        },
        'phone_number': {
            'nullable': False,
            'type': 'snum'
        },
        'email': {
            'nullable': True,
            'type': 'email'
        },
        'user_info': {
            'nullable': True,
            'type': 'json'
        },
        'company_info': {
            'nullable': True,
            'type': 'str'
        },
        'configurations': {
            'nullable': True,
            'type': 'json'
        },
    }

    @staticmethod
    def _is_the_length_correct(data, max_length, min_length) -> bool:
        if max_length is not None and len(data) > max_length:
            return False
        if min_length is not None and len(data) < min_length:
            return False
        return True

    @staticmethod
    def _is_the_type_correct(data, type) -> bool:
        # todo create check input type function
        return True

    def input(self, data: dict, rules: dict) -> dict:
        cd = dict()
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                raise InputException(message=error_codes.INPUT_IS_NULL_MESSAGE,
                                     error_code=error_codes.INPUT_IS_NULL_CODE)
            if key in data:
                d = data[key]
                if not self._is_the_length_correct(d, rules[key]['max_length'], rules[key]['min_length']):
                    raise InputException(message=error_codes.INPUT_LENGTH_IS_INCORRECT_MESSAGE,
                                         error_code=error_codes.INPUT_LENGTH_IS_INCORRECT_CODE)
                if not self._is_the_type_correct(d, rules[key]['type']):
                    raise InputException(message=error_codes.INPUT_TYPE_IS_INCORRECT_MESSAGE,
                                         error_code=error_codes.INPUT_TYPE_IS_INCORRECT_CODE)
                cd[key] = d
        return cd

    def output(self, status: str, message: str, code: str, data, rules) -> dict:
        ret = dict()
        ret['status'] = status
        ret['message'] = message
        ret['code'] = code
        info = dict()
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                raise InputException(message=error_codes.OUTPUT_IS_NULL_MESSAGE,
                                     error_code=error_codes.OUTPUT_IS_NULL_CODE)
            if key in data:
                info[key] = data[key]
        ret['information'] = info
        return ret
