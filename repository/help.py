# ------------------------------------------------------------------------------------------------
format = {
    'request URL': '',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'key': {
                'Value properties': ''
            }
        }
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'key': {
                    'Value properties': ''
                }
            }
        }
    },
    "message": "",
    "status": ""
}
# ------------------------------------------------------------------------------------------------
register = {
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
    },
    "message": "",
    "status": ""
}
# ------------------------------------------------------------------------------------------------
login = {
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
# ------------------------------------------------------------------------------------------------
logout = {
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
# ------------------------------------------------------------------------------------------------
update_password = {
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
# ------------------------------------------------------------------------------------------------
update_phone_number = {
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
# ------------------------------------------------------------------------------------------------
update_email = {
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
# ------------------------------------------------------------------------------------------------
update_user_information = {
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
# ------------------------------------------------------------------------------------------------
update_company_information = {
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
# ------------------------------------------------------------------------------------------------
update_configurations = {
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
# ------------------------------------------------------------------------------------------------
recovery_by_send_sms = {
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
# ------------------------------------------------------------------------------------------------
recovery_by_send_email = {
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
# ------------------------------------------------------------------------------------------------
recovery_by_last_password = {
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
# ------------------------------------------------------------------------------------------------
recovery_by_answers = {
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
# ------------------------------------------------------------------------------------------------
delete_account = {
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
# ------------------------------------------------------------------------------------------------
send_vcode_ph = {
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
# ------------------------------------------------------------------------------------------------
send_vcode_ea = {
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
# ------------------------------------------------------------------------------------------------
confirm_code_ph = {
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
# ------------------------------------------------------------------------------------------------
confirm_code_ea = {
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
# ------------------------------------------------------------------------------------------------
add_address = {
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
