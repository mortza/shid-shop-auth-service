from flask import request, render_template, make_response, redirect, url_for
from datetime import datetime as dt
from application import app
from .exceptions import UserException
from .repositories import UserRepository


@app.route('/register', methods=['POST'])
def register():
    """
    request.args -> {
        'phone_number': 'req',
        'email': 'req',
        'password': 'req',
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
    :return:
    """
    try:
        repo = UserRepository()
        ret = repo.register(**request.args)
        return make_response(ret)
    except UserException as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': ex.error_code,
                                  'message': ex.message
                              }, 500))
    except Exception as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': '-1',
                                  'message': str(ex)
                              }, 500))


@app.route('/login', methods=['POST'])
def login():
    """
    request.args -> {
            'user_name'('phone_number' or 'email') : 'opt'
            'phone_number': 'opt',
            }
    :return:
    """
    try:
        repo = UserRepository()
        ret = repo.login(**request.args)
        if ret:
            return make_response(({
                                      'status': 'user is login',
                                      'code': '0',
                                      'message': '0'
                                  }, 500))
        else:
            return make_response(({
                                      'status': 'user is not login',
                                      'code': '-1',
                                      'message': '-1'
                                  }, 500))
    except UserException as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': ex.error_code,
                                  'message': ex.message
                              }, 500))
    except Exception as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': '-1',
                                  'message': str(ex)
                              }, 500))


@app.route('/logout', methods=['POST'])
def logout():
    """
    request.args -> {
            'user_name'('phone_number' or 'email') : 'opt'
            }
    :return:
    """
    pass


@app.route('/user/update', methods=['POST'])
def update():
    """
    request.args -> {
            'user_name'('phone_number' or 'email') : 'opt'
            'new_phone_number': 'opt',
            'new_email': 'opt',
            'new_password': 'opt',
            'new_first_name': 'opt',
            'new_last_name': 'opt',
            'new_avatar_url': 'opt',
            'new_personal_account_number': 'opt',
            'new_card_number': 'opt',
            'new_national_card': 'opt',
            'new_configurations': 'opt',
        }
    :return:
    """
    try:
        repo = UserRepository()
        ret = repo.update(**request.args)
        return make_response(ret)
    except UserException as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': ex.error_code,
                                  'message': ex.message
                              }, 500))
    except Exception as ex:
        return make_response(({
                                  'status': 'error',
                                  'code': '-1',
                                  'message': str(ex)
                              }, 500))


@app.route('/user/delete', methods=['POST'])
def delete():
    """
    request.args -> {
            'user_name'('phone_number' or 'email') : 'opt'
            }
    :return:
    """
    pass


@app.route('/register/validate-phone', methods=['POST'])
def validate_phone_number():
    pass
