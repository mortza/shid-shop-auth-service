from application import application, redis_client, adata, limiter, RATE_LIMIT, mail
from application.repositories import UserRepository
from repository.ok import *
from application.decorator import cleanData, is_login
from flask_mail import Mail, Message
import os


@application.route('/register', methods=['POST'])
@limiter.limit(RATE_LIMIT)
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
                    'max_length': 16,
                    'type': 'string'
                },
                'real_or_legal': {
                    'nullable': False,
                    'max_length': 16,
                    'type': 'string'
                },
                'phone_number': {
                    'nullable': False,
                    'max_length': 11,
                    'min_length': 11,
                    'type': 'numerical string'
                },
                'password': {
                    'nullable': False,
                    'max_length': 128,
                    'min_length': 8,
                    'type': 'string'
                },
                'email': {
                    'nullable': True,
                    'max_length': 128,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'string'
                },
                'answers': {
                    'nullable': True,
                    'type': 'json'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                },
            },
        },
        'Response': {
            "information": {
                'output': {
                    'uuid': {
                        'nullable': True,
                        'type': 'string'
                    },
                    'role': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'real_or_legal': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'phone_number': {
                        'nullable': False,
                        'type': 'numerical string'
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
            }
        },
    }
    """
    repo = UserRepository()
    t = repo.register(clean_data)

    ret = {
        'data': t,
        'code': SIGNUP_CODE,
        'message': SIGNUP_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/login', methods=['POST'])
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'password': {
                    'nullable': False,
                    'type': 'string'
                },
                'device_information': {
                    'nullable': False,
                    'type': 'json'
                },
            },
        },
        'Response': {
            "information": {
                'output': {
                    'auth_token': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'role': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'real_or_legal': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'phone_number': {
                        'nullable': False,
                        'type': 'numerical string'
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
                        'type': 'string'
                    },
                    'configurations': {
                        'nullable': True,
                        'type': 'json'
                    },
                }
            }
        }
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'password': {
                    'nullable': False,
                    'max_length': 128,
                    'min_length': 8,
                    'type': 'string'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'auth_token': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'role': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'real_or_legal': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'phone_number': {
                        'nullable': False,
                        'type': 'numerical string'
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
                        'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'phone_number': {
                    'nullable': False,
                    'max_length': 11,
                    'min_length': 11,
                    'type': 'numerical string'
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
    res, tkns = repo.update(clean_data, 'update_phone_number')
    res['auth_token'] = clean_data['auth_token']
    for tkn in tkns:
        redis_client.set(tkn.token, tkn.information)
    ret = {
        'data': res,
        'code': UPDATE_PHONE_NUMBER_CODE,
        'message': UPDATE_PHONE_NUMBER_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/user/update/email', methods=['POST'], endpoint='update_email')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'email': {
                    'nullable': False,
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
    res, tkns = repo.update(clean_data, 'update_email')
    res['auth_token'] = clean_data['auth_token']
    for tkn in tkns:
        redis_client.set(tkn.token, tkn.information)
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_EMAIL_ADDRESS_CODE
    ret['message'] = UPDATE_EMAIL_ADDRESS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/user-information', methods=['POST'], endpoint='update_user_information')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'user_information': {
                    'nullable': False,
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

    res, tkns = repo.update(clean_data, 'update_user_information')
    res['auth_token'] = clean_data['auth_token']
    for tkn in tkns:
        redis_client.set(tkn.token, tkn.information)
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_USER_INFORMATION_CODE
    ret['message'] = UPDATE_USER_INFORMATION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/company-information', methods=['POST'], endpoint='update_company_information')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'company_information': {
                    'nullable': False,
                    'type': 'string'
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
    res, tkns = repo.update(clean_data, 'update_company_information')
    res['auth_token'] = clean_data['auth_token']
    for tkn in tkns:
        redis_client.set(tkn.token, tkn.information)
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_COMPANY_INFORMATION_CODE
    ret['message'] = UPDATE_COMPANY_INFORMATION_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/update/configurations', methods=['POST'], endpoint='update_configurations')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'configurations': {
                    'nullable': False,
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
    res, tkns = repo.update(clean_data, 'update_configurations')
    res['auth_token'] = clean_data['auth_token']
    for tkn in tkns:
        redis_client.set(tkn.token, tkn.information)
    ret = dict()
    ret['data'] = res
    ret['code'] = UPDATE_CONFIGURATIONS_CODE
    ret['message'] = UPDATE_CONFIGURATIONS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/send-sms', methods=['POST'], endpoint='recovery_by_send_sms')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'numerical string'
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
@limiter.limit(RATE_LIMIT)
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
    # todo send email
    # msg = Message(
    #     'Temporary Password: {}'.format(res['temporary_password']),
    #     sender=os.getenv('MAIL_SENDER'),
    #     recipients=['{}'.format(res['user_name'])]
    # )
    # msg.body = os.getenv('MESSAGE_BODY')
    # mail.send(msg)

    ret = dict()
    ret['data'] = dict()
    ret['code'] = RECOVERY_BY_SEND_EMAIL_CODE
    ret['message'] = RECOVERY_BY_SEND_EMAIL_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/last-password', methods=['POST'], endpoint='recovery_by_last_password')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'last_password': {
                    'nullable': False,
                    'type': 'string'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'auth_token': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'role': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'real_or_legal': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'phone_number': {
                        'nullable': False,
                        'type': 'numerical string'
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
                        'type': 'string'
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
        }
    )
    redis_client.set(rkey, rval)
    ret['code'] = RECOVERY_BY_LAST_PASSWORD_CODE
    ret['message'] = RECOVERY_BY_LAST_PASSWORD_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/recovery-by/send-rand-question', methods=['POST'], endpoint='send_rand_question')
@limiter.limit(RATE_LIMIT)
@cleanData(adata.rand_question_rules)
def send_rand_question(clean_data: dict) -> dict:
    repo = UserRepository()
    rnd_question = repo.rand_question(clean_data)
    ret = {
        'data': rnd_question,
        'code': RANDOM_QUESTION_SEND_CODE,
        'message': RANDOM_QUESTION_SEND_MESSAGE,
        'status': OK_STATUS
    }
    return ret


@application.route('/recovery-by/answers', methods=['POST'], endpoint='recovery_by_answers')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'answers': {
                    'nullable': False,
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
                        'type': 'string'
                    },
                    'role': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'real_or_legal': {
                        'nullable': False,
                        'type': 'string'
                    },
                    'phone_number': {
                        'nullable': False,
                        'type': 'numerical string'
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
                        'type': 'string'
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
        }
    )
    redis_client.set(rkey, rval)
    ret['code'] = RECOVERY_BY_ANSWERS_CODE
    ret['message'] = RECOVERY_BY_ANSWERS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/user/delete-account', methods=['POST'], endpoint='delete_account')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'vcode_expiration_date': {
                        'nullable': False,
                        'type': 'string'
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
    # print(res['vcode_for_phone'])
    ret = dict()
    ret['vcode_expiration_date'] = res['vcode_expiration_date']
    ret['data'] = ret
    ret['code'] = SEND_VCODE_FOR_PHONE_NUMBER_CODE
    ret['message'] = SEND_VCODE_FOR_PHONE_NUMBER_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-email', methods=['POST'], endpoint='send_vcode_ea')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'vcode_expiration_date': {
                        'nullable': False,
                        'type': 'string'
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
    # todo send email
    # msg = Message(
    #     'Verification code: {}'.format(res['vcode_for_email']),
    #     sender=os.getenv('MAIL_SENDER'),
    #     recipients=['{}'.format(res['email_address'])]
    # )
    # msg.body = os.getenv('MESSAGE_BODY')
    # mail.send(msg)

    ret = dict()
    ret['vcode_expiration_date'] = res['vcode_expiration_date']
    ret['data'] = ret
    ret['code'] = SEND_VCODE_FOR_EMAIL_ADDRESS_CODE
    ret['message'] = SEND_VCODE_FOR_EMAIL_ADDRESS_MESSAGE
    ret['status'] = OK_STATUS
    return ret


@application.route('/register/vcode/send-sms/confirm', methods=['POST'], endpoint='confirm_code_ph')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'vcode': {
                    'nullable': False,
                    'max_length': 5,
                    'min_length': 5,
                    'type': 'numerical string'
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'code_review_status': {
                        'nullable': False,
                        'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'vcode': {
                    'nullable': False,
                    'max_length': 4,
                    'min_length': 4,
                    'type': 'numerical string'
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'code_review_status': {
                        'nullable': False,
                        'type': 'string'
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


@application.route('/user/active-sessions', methods=['POST'], endpoint='active_session')
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                }
            },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'active_sessions': {
                        'nullable': False,
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
                },
                'session': {
                    'nullable': False,
                    'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
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
@limiter.limit(RATE_LIMIT)
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
                    'type': 'string'
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


@application.route('/user/get-users', methods=['POST'], endpoint='users')
@limiter.limit(RATE_LIMIT)
@is_login(adata.get_users_rules)
def get_users(clean_data: dict) -> dict:
    """
    {
        'request URL': '/user/get-users',
        'methods': 'POST',
        'Query Params': {
            'input': {
                'page': {
                        'nullable': False,
                        'type': 'string'
                    }
                },
                'auth_token': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
        },
        'Response': {
            "code": '',
            "information": {
                'output': {
                    'users': {
                        'nullable': False,
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
    res = repo.get_users(clean_data)
    ret = {
        'data': res,
        'code': GET_USERS_CODE,
        'message': GET_USER_MESSAGE,
        'status': OK_STATUS
    }
    return ret
