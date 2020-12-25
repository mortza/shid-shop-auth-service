from application import application, redis_client, adata
from application.repositories import UserRepository
from repository.ok import *
from application.decorator import cleanData, is_login


@application.route('/register', methods=['POST'])
@cleanData(adata.signup_rules)
def register(clean_data: dict) -> dict:
    """
    {
        'request URL': '/register',
        'methods': 'POST',
        'Query Params': {
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
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    repo.register(clean_data)
    ret = {
        'data': {},
        'code': SIGNUP_CODE,
        'message': SIGNUP_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/login', methods=['POST'])
@cleanData(adata.login_rules)
def login(clean_data: dict) -> dict:
    """
    {
        'request URL': '/login',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
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
                        'type': 'str'
                    },
                    'configurations': {
                        'nullable': True,
                        'type': 'json'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    rkey, rval, ret = repo.login(clean_data)
    redis_client.set(rkey, rval)
    ret['code'] = LOGIN_CODE
    ret['message'] = LOGIN_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/logout', methods=['POST'], endpoint='logout')
@is_login(adata.logout_rules)
def logout(clean_data: dict) -> dict:
    """
    {
        'request URL': '/logout',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    tkn = repo.logout(clean_data)
    redis_client.delete(tkn)
    ret = {
        'data': {},
        'code': LOGOUT_CODE,
        'message': LOGOUT_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/user/update/password', methods=['POST'], endpoint='update_password')
@is_login(adata.password_update_rules)
def update_password(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/password',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
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
                        'type': 'str'
                    },
                    'configurations': {
                        'nullable': True,
                        'type': 'json'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    tkns, user_name = repo.update(clean_data, 'update_password')
    for tkn in tkns:
        redis_client.delete(tkn.token)
    rkey, rval, ret = repo.login(
        {
            'user_name': user_name,
            'password': clean_data['password'],
            'device_information': clean_data['auth_token_info_extract']['device_information']
        }
    )
    redis_client.set(rkey, rval)
    ret['code'] = UPDATE_PASSWORD_CODE
    ret['message'] = UPDATE_PASSWORD_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/phone-number', methods=['POST'], endpoint='update_phone_number')
@is_login(adata.phone_number_update_rules)
def update_phone_number(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/phone-number',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.update(clean_data, 'update_phone_number')
    # todo
    res['auth_token'] = ''
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_PHONE_NUMBER_CODE
    ret['message'] = UPDATE_PHONE_NUMBER_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/email', methods=['POST'], endpoint='update_email')
@is_login(adata.email_update_rules)
def update_email(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/email',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.update(clean_data, 'update_email')
    # todo
    res['auth_token'] = ''
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_EMAIL_ADDRESS_CODE
    ret['message'] = UPDATE_EMAIL_ADDRESS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/user-information', methods=['POST'], endpoint='update_user_information')
@is_login(adata.user_info_update_rules)
def update_user_information(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/user-information',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
                'user_information': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'json'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.update(clean_data, 'update_user_information')
    # todo
    res['auth_token'] = ''
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_USER_INFORMATION_CODE
    ret['message'] = UPDATE_USER_INFORMATION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/company-information', methods=['POST'], endpoint='update_company_information')
@is_login(adata.company_info_update_rules)
def update_company_information(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/company-information',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
                'company_information': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.update(clean_data, 'update_company_information')
    # todo
    res['auth_token'] = ''
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_COMPANY_INFORMATION_CODE
    ret['message'] = UPDATE_COMPANY_INFORMATION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/configurations', methods=['POST'], endpoint='update_configurations')
@is_login(adata.configurations_update_rules)
def update_configurations(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/update/configurations',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.update(clean_data, 'update_configurations')
    # todo
    res['auth_token'] = ''
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_CONFIGURATIONS_CODE
    ret['message'] = UPDATE_CONFIGURATIONS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/send-sms', methods=['POST'], endpoint='recovery_by_send_sms')
@cleanData(adata.recovery_by_sms_rules)
def recovery_by_send_sms(clean_data: dict) -> dict:
    """
    {
        'request URL': '/recovery-by/send-sms',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'phone_number': {
                    'nullable': False,
                    'max_length': 11,
                    'min_length': 11,
                    'type': 'snum'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.page_recovery(clean_data, 'recovery_by_send_sms')
    print(res)
    # todo send sms. phone number : res['user_name'] and sms text : res['temporary_password']
    ret = dict()
    ret['data'] = dict()
    ret['code'] = RECOVERY_BY_SEND_SMS_CODE
    ret['message'] = RECOVERY_BY_SEND_SMS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/send-email', methods=['POST'], endpoint='recovery_by_send_email')
@cleanData(adata.recovery_by_email_rules)
def recovery_by_send_email(clean_data: dict) -> dict:
    """
    {
        'request URL': '/recovery-by/send-email',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'email': {
                    'nullable': True,
                    'max_length': None,
                    'min_length': None,
                    'type': 'email'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.page_recovery(clean_data, 'recovery_by_send_email')
    print(res)
    # todo send email. email address : res['user_name'] and email text : res['temporary_password']
    ret = dict()
    ret['data'] = dict()
    ret['code'] = RECOVERY_BY_SEND_EMAIL_CODE
    ret['message'] = RECOVERY_BY_SEND_EMAIL_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/last-password', methods=['POST'], endpoint='recovery_by_last_password')
@cleanData(adata.recovery_by_last_password_rules)
def recovery_by_last_password(clean_data: dict) -> dict:
    """
    {
        'request URL': '/recovery-by/last-password',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
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
                        'type': 'str'
                    },
                    'configurations': {
                        'nullable': True,
                        'type': 'json'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    repo.page_recovery(clean_data, 'recovery_by_last_password')
    rkey, rval, ret = repo.login(
        {
            'user_name': clean_data['user_name'],
            'password': clean_data['last_password'],
            'device_information': clean_data['auth_token_info_extract']['device_information']
        }
    )
    redis_client.set(rkey, rval)
    ret['code'] = RECOVERY_BY_LAST_PASSWORD_CODE
    ret['message'] = RECOVERY_BY_LAST_PASSWORD_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/answers', methods=['POST'], endpoint='recovery_by_answers')
@cleanData(adata.recovery_by_answers_rules)
def recovery_by_answers(clean_data: dict) -> dict:
    """
    {
        'request URL': '/recovery-by/answers',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'user_name': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
                'answers': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'json'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
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
                        'type': 'str'
                    },
                    'configurations': {
                        'nullable': True,
                        'type': 'json'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.page_recovery(clean_data, 'recovery_by_answers')
    rkey, rval, ret = repo.login(
        {
            'user_name': res['user_name'],
            'password': res['temporary_password'],
            'device_information': clean_data['auth_token_info_extract']['device_information']
        }
    )
    redis_client.set(rkey, rval)
    ret['code'] = RECOVERY_BY_ANSWERS_CODE
    ret['message'] = RECOVERY_BY_ANSWERS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/delete-account', methods=['POST'], endpoint='delete_account')
@is_login(adata.delete_account_rules)
def delete_account(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/delete-account',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    tkns = repo.delete(clean_data)
    for tkn in tkns:
        redis_client.delete(tkn.token)
    ret = dict()
    ret['data'] = dict()
    ret['code'] = DELETE_ACCOUNT_CODE
    ret['message'] = DELETE_ACCOUNT_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-sms', methods=['POST'], endpoint='send_vcode_ph')
@is_login(adata.send_vcode_phone_number_rules)
def send_vcode_ph(clean_data: dict) -> dict:
    """
    {
        'request URL': '/register/vcode/send-sms',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'vcode_expiration_date': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'str'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.create_verify_code(clean_data, 'for_phone')
    # todo send sms: phone number : ret['phone_number'] and sms text : ret['vcode_for_phone']
    print(res['vcode_for_phone'])
    ret = dict()
    ret['vcode_expiration_date'] = res['vcode_expiration_date']
    ret['data'] = ret
    ret['code'] = SEND_VCODE_FOR_PHONE_NUMBER_CODE
    ret['message'] = SEND_VCODE_FOR_PHONE_NUMBER_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-email', methods=['POST'], endpoint='send_vcode_ea')
@is_login(adata.email_vcode_email_address_rules)
def send_vcode_ea(clean_data: dict) -> dict:
    """
    {
        'request URL': '/register/vcode/send-email',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'vcode_expiration_date': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'str'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.create_verify_code(clean_data, 'for_email')
    # todo send email: email address : ret['email_address'] and sms text : ret['vcode_for_email']
    print(res['vcode_for_email'])
    ret = dict()
    ret['vcode_expiration_date'] = res['vcode_expiration_date']
    ret['data'] = ret
    ret['code'] = SEND_VCODE_FOR_EMAIL_ADDRESS_CODE
    ret['message'] = SEND_VCODE_FOR_EMAIL_ADDRESS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-sms/confirm', methods=['POST'], endpoint='confirm_code_ph')
@is_login(adata.confirm_vcode_phone_number_rules)
def confirm_code_ph(clean_data: dict) -> dict:
    """
    {
        'request URL': '/register/vcode/send-sms/confirm',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'code_review_status': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'str'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.check_code(clean_data, 'for_phone')
    ret = dict()
    if res:
        ret['code_review_status'] = 'The code is acceptable.'
    else:
        ret['code_review_status'] = 'The code is unacceptable.'
    ret['data'] = ret
    ret['code'] = CONFIRM_VCODE_FOR_PHONE_NUMBER_CODE
    ret['message'] = CONFIRM_VCODE_FOR_PHONE_NUMBER_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-email/confirm', methods=['POST'], endpoint='confirm_code_ea')
@is_login(adata.confirm_vcode_email_address_rules)
def confirm_code_ea(clean_data: dict) -> dict:
    """
    {
        'request URL': '/register/vcode/send-email/confirm',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'code_review_status': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'str'
                    },
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.check_code(clean_data, 'for_email')
    ret = dict()
    if res:
        ret['code_review_status'] = 'The code is acceptable.'
    else:
        ret['code_review_status'] = 'The code is unacceptable.'
    ret['data'] = ret
    ret['code'] = CONFIRM_VCODE_FOR_EMAIL_ADDRESS_CODE
    ret['message'] = CONFIRM_VCODE_FOR_EMAIL_ADDRESS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/add-address', methods=['POST'], endpoint='add_address')
@is_login(adata.add_address_rules)
def add_address(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/add-address',
        'methods': 'POST',
        'Query Params': {
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
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    repo.add_address(clean_data)
    ret = {
        'data': {},
        'code': ADD_ADDRESS_CODE,
        'message': ADD_ADDRESS_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/user/get-addresses', methods=['POST'], endpoint='get_addresses')
@is_login(adata.get_addresses_rules)
def get_addresses(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/get-addresses',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'addresses': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'json'
                    }
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.get_addresses(clean_data)
    ret = {
        'data': res,
        'code': GET_ADDRESSES_CODE,
        'message': GET_ADDRESSES_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/user/active-sessions', methods=['POST'], endpoint='active_session')
@is_login(adata.get_sessions_rules)
def active_session(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/active-sessions',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'active_sessions': {
                        'nullable': False,
                        'max_length': None,
                        'min_length': None,
                        'type': 'json'
                    }
                }
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.active_session(clean_data)
    ret = dict()
    ret['data'] = res
    ret['code'] = GET_ACTIVE_SESSIONS_CODE
    ret['message'] = GET_ACTIVE_SESSIONS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/delete-session', methods=['POST'], endpoint='delete_session')
@is_login(adata.delete_sessions_rules)
def delete_session(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/delete-session',
        'methods': 'POST',
        'Query Params': {
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
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    repo.delete_session(clean_data)
    redis_client.delete(clean_data['session'])
    ret = dict()
    ret['data'] = {}
    ret['code'] = DEL_SESSION_CODE
    ret['message'] = DEL_SESSION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/delete-all-active-sessions', methods=['POST'], endpoint='delete_all_active_sessions')
@is_login(adata.delete_all_sessions_rules)
def delete_all_active_sessions(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/delete-all-active-sessions',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    repo = UserRepository()
    res = repo.delete_all_sessions(clean_data)
    for tkn in res:
        redis_client.delete(tkn.token)
    ret = dict()
    ret['data'] = {}
    ret['code'] = DEL_ALL_SESSION_CODE
    ret['message'] = DEL_ALL_SESSION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/is-login', methods=['POST'], endpoint='user_is_login')
@is_login(adata.user_is_login_rules)
def user_is_login(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/is-login',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {}
            }
        },
        "message": "",
        "status": ""
    }
    """
    ret = {
        'data': clean_data['auth_token_info_extract'],
        'code': USER_IS_LOGIN_CODE,
        'message': USER_IS_LOGIN_MESSAGE,
        'status': OK_STATUS
    }
    return ret
