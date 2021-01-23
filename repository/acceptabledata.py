from repository.ok import *


class AcceptableData:
    # input rules
    # signup
    signup_rules = {
        'input': {
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
                'min_length': 6,
                'type': 'email'
            },
            'user_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'question_answring_1': {
                'nullable': True,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
            'question_answring_2': {
                'nullable': True,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
            'question_answring_3': {
                'nullable': True,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
            'question_answring_4': {
                'nullable': True,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
            'question_answring_5': {
                'nullable': True,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'username': {
                'nullable': False,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
        },
        'output': {
            'uuid': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
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
            'email': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'email'
            },
            'user_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    # login
    login_rules = {
        'input': {
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
            'device_information': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    # logout
    logout_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {}
    }
    # update
    phone_number_update_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },

            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    password_update_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    email_update_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    user_info_update_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'user_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    company_info_update_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': 3,
                'type': 'snum'
            },
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    configurations_update_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    # forget password
    recovery_by_sms_rules = {
        'input': {
            'phone_number': {
                'nullable': False,
                'max_length': 11,
                'min_length': 11,
                'type': 'snum'
            },
        },
        'output': {}
    }
    recovery_by_email_rules = {
        'input': {
            'email': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'email'
            },
        },
        'output': {}
    }
    recovery_by_last_password_rules = {
        'input': {
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
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }

    rand_question_rules = {
        'input': {
            'user_name': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {
            'question': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    }

    recovery_by_answers_rules = {
        'input': {
            'user_name': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'question_answring': {
                'nullable': False,
                'max_length': None,
                'min_length': 1,
                'type': 'json'
            },
        },
        'output': {
            'auth_token': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }
    # delete account
    delete_account_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {}
    }
    # generate and send vcode
    send_vcode_phone_number_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {
            'vcode_expiration_date': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        }
    }
    email_vcode_email_address_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {
            'vcode_expiration_date': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        }
    }
    # confirm the received vcode
    confirm_vcode_email_address_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'code_review_status': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        }
    }
    confirm_vcode_phone_number_rules = {
        'input': {
            'auth_token': {
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
        },
        'output': {
            'code_review_status': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        }
    }

    # add address
    add_address_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'address': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            }
        },
        'output': {}
    }

    # get addresses
    get_addresses_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'page': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'int'
            },
        },
        'output': {
            'addresses': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    }

    # get sessions
    get_sessions_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {
            'sessions': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    }

    # get users
    get_users_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'page': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'int'
            },
        },
        'output': {
            'users': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    }

    # del session
    delete_sessions_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'session': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {},
    }

    # del all session
    delete_all_sessions_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {},
    }

    # user is login or not
    user_is_login_rules = {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {
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
            'user_information': {
                'nullable': True,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
            'uuid': {
                'nullable': True,
                'type': 'str'
            },
            'username': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'first_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'national_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'gender': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'birthday': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_name': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'economic_code': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'national_id_company_owner': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
            'registration_id': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'snum'
            },
        }
    }

    @staticmethod
    def _is_the_length_correct(data, max_length, min_length, typ=None) -> bool:
        if typ is 'json':
            import json
            data = json.loads(data)
            if max_length is not None and len(data) > max_length:
                return False
            if min_length is not None and len(data) < min_length:
                return False
            return True

        if max_length is not None and len(data) > max_length:
            return False
        if min_length is not None and len(data) < min_length:
            return False
        return True

    @staticmethod
    def _is_the_type_correct(data, type) -> bool:
        if type == 'str':
            return isinstance(data, str)
        if type == 'snum':
            for d in data:
                if d not in '1234567890':
                    return False
            return True
        if type == 'email':
            import re
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex, data):
                return True
            else:
                return False
        if type == 'json':
            import json
            return isinstance(json.loads(data), dict)
        else:
            raise Exception(TYPE_NAME_IS_NOT_DEFINE_MESSAGE)

    def input(self, data: dict, rules: dict) -> dict:
        cd = dict()
        rules = rules['input']
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                err_message = INPUT_NOT_SET_MESSAGE.format(key)
                raise Exception(err_message)
            if key in data:
                d = data[key]
                if not self._is_the_length_correct(d, rules[key]['max_length'], rules[key]['min_length'],
                                                   rules[key]['type']):
                    err_message = INPUT_LENGTH_NOT_SET_MESSAGE.format(key)
                    raise Exception(err_message)
                if not self._is_the_type_correct(d, rules[key]['type']):
                    err_message = INPUT_TYPE_NOT_SET_MESSAGE.format(key)
                    raise Exception(err_message)
                cd[key] = d
        return cd

    def output(self, arguments: dict, rules: dict) -> dict:
        ret = dict()
        if 'status' in arguments:
            ret['status'] = arguments['status']
        else:
            err_message = STATUS_NOT_SET_MESSAGE
            raise Exception(err_message)

        if 'message' in arguments:
            ret['message'] = arguments['message']
        else:
            err_message = MESSAGE_NOT_SET_MESSAGE

            raise Exception(err_message)
        if 'code' in arguments:
            ret['code'] = arguments['code']
        else:
            err_message = CODE_NOT_SET_MESSAGE
            raise Exception(err_message)
        if 'data' in arguments:
            data = arguments['data']
        else:
            err_message = DATA_NOT_SET_MESSAGE

            raise Exception(err_message)

        rules = rules['output']
        info = dict()
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                err_message = OUTPUT_NOT_SET_MESSAGE.format(key)
                raise Exception(err_message)
            if key in data:
                info[key] = data[key]
        ret['information'] = info
        return ret
