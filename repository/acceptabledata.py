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
            }, }
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
                'type': 'str'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
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
        'output': {}
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
                'type': 'str'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
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
        'output': {}
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
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
        'output': {}
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
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
        'output': {}
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
        'output': {}
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
                'type': 'str'
            },
            'configurations': {
                'nullable': True,
                'type': 'json'
            },
        }
    }
    recovery_by_answers_rules = {
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
        rules = rules['input']
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                err_message = "from acceptabledata.AcceptableData.input:" \
                              " Input {} is not set.".format(key)
                raise Exception(err_message)
            if key in data:
                d = data[key]
                if not self._is_the_length_correct(d, rules[key]['max_length'], rules[key]['min_length']):
                    err_message = "from acceptabledata.AcceptableData.input:" \
                                  " {} input length is not set correctly.".format(key)
                    raise Exception(err_message)
                if not self._is_the_type_correct(d, rules[key]['type']):
                    err_message = "from acceptabledata.AcceptableData.input:" \
                                  " Input data type {} is not set correctly.".format(key)
                    raise Exception(err_message)
                cd[key] = d
        return cd

    def output(self, arguments: dict, rules: dict) -> dict:
        ret = dict()
        if 'status' in arguments:
            ret['status'] = arguments['status']
        else:
            err_message = "from acceptabledata.AcceptableData.output:" \
                          "'status' is not in arguments."
            raise Exception(err_message)

        if 'message' in arguments:
            ret['message'] = arguments['message']
        else:
            err_message = "from acceptabledata.AcceptableData.output:" \
                          "'message' is not in arguments."
            raise Exception(err_message)
        if 'code' in arguments:
            ret['code'] = arguments['code']
        else:
            err_message = "from acceptabledata.AcceptableData.output:" \
                          "'code' is not in arguments."
            raise Exception(err_message)
        if 'data' in arguments:
            data = arguments['data']
        else:
            err_message = "from acceptabledata.AcceptableData.output:" \
                          "'data' is not in arguments."
            raise Exception(err_message)

        rules = rules['output']
        info = dict()
        for key in rules.keys():
            if key not in data and not rules[key]['nullable']:
                err_message = "from acceptabledata.AcceptableData.output:" \
                              " Output {} is not set.".format(key)
                raise Exception(err_message)
            if key in data:
                info[key] = data[key]
        ret['information'] = info
        return ret
