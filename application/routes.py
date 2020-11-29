from flask import request, make_response
from application import app, redis_client, db
from application.exceptions import UserException, TokenException, ArgsException
from application.repositories import UserRepository
from repository import error_codes
import json
from application.models import Token, User


def token_is_exist(func):
    def in_redis_or_in_db():
        auth_token = ''
        if 'Authorization' in request.headers:
            auth_token = request.headers['Authorization']
            auth_token = auth_token.split(' ')
            auth_token = auth_token[1]
        else:
            raise ArgsException(message=error_codes.KEY_IS_EMPTY_MESSAGE,
                                error_code=error_codes.KEY_IS_EMPTY_CODE)
        if redis_client.get(auth_token):
            return func()
        else:
            auth_token = db.session.query(Token).filter(Token.token == auth_token).first()
            if auth_token is not None:
                user = db.session.query(User).filter(User.id == auth_token.user_id).first()
                redis_client.set(auth_token.token, json.dumps(user.to_dict))
                return func()
            else:
                raise TokenException(message=error_codes.TOKEN_NOT_EXIST_ON_DATABASE_MESSAGE,
                                     error_code=error_codes.TOKEN_NOT_EXIST_ON_DATABASE_CODE)

    return in_redis_or_in_db


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
        'answers': 'opt',
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
        token, user_info = repo.login(**request.args)
        redis_client.set(token, json.dumps(user_info))
        ret = dict()
        ret['login_token'] = token
        ret['user_info'] = user_info
        ret['status'] = 'ok'
        ret['code'] = error_codes.OK_STATUS
        ret['message'] = ''
        return make_response((ret, 200))
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


@app.route('/logout', methods=['POST'], endpoint='logout')
@token_is_exist
def logout():
    try:
        repo = UserRepository()
        token = repo.logout(**request.args)
        ret = redis_client.delete(token)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'Logout completed successfully.'
                              }, 200))
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


@app.route('/user/update', methods=['POST'], endpoint='update')
@token_is_exist
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
        user_info = repo.update(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': 1,
                                  'message': 'Update completed successfully.',
                                  'user_info': user_info
                              }, 200))
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


@app.route('/forget', methods=['POST'])
def page_recovery():
    """
    request.args -> {
            'user_name'(phone_number or email) : 'opt'
            'send_code_to_phone_number'(False_or_True_or_None): 'opt',
            'send_code_to_email'(False_or_True_or_None): 'opt',
            'login_by_last_password(entered last password)': 'opt',
            'login_by_answered_to_questions({ans_to_q_1 : value,(and for all questions)})': 'opt',
        }
    :return:
    """
    try:
        repo = UserRepository()
        res = repo.page_recovery(**request.args)
        if 'temporary_password' in res:
            tp = res['temporary_password']
            return make_response(({
                                      'status': 'ok',
                                      'code': 1,
                                      'message': 'send code.',
                                      'information': tp
                                  }, 200))
        if 'token' in res:
            tkn = res['token']
            uinfo = res['user_info']
            redis_client.set(tkn, json.dumps(uinfo))
            print('*****************************&&&&&&&&&&')
            return make_response(({
                                      'status': 'ok',
                                      'code': 1,
                                      'message': 'login',
                                      'information': res
                                  }, 200))

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


@app.route('/delete-account', methods=['POST'], endpoint='delete')
@token_is_exist
def delete():
    try:
        repo = UserRepository()
        tokens = repo.delete(**request.args)
        for token in tokens:
            redis_client.delete(token.token)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'delete account successfully.'
                              }, 200))
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


@app.route('/register/verification-code-for-phone',
           methods=['POST'],
           endpoint='send_vcode_ph')
@token_is_exist
def send_vcode_ph():
    try:
        repo = UserRepository()
        vcode = repo.create_verify_code(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'send vcode for phone number.',
                                  'informations': vcode
                              }, 200))
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


@app.route('/register/verification-code-for-email',
           methods=['POST'],
           endpoint='send_vcode_e')
@token_is_exist
def send_vcode_e():
    try:
        repo = UserRepository()
        vcode = repo.create_verify_code(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'send vcode for email.',
                                  'informations': vcode
                              }, 200))
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


@app.route('/register/verify-phone-verification-code',
           methods=['POST'],
           endpoint='confirm_code_ph')
@token_is_exist
def confirm_code_ph():
    try:
        repo = UserRepository()
        res = repo.check_code_ph(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'phone number vcode is {}.'.format(str(res)),
                              }, 200))
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


@app.route('/register/verify-email-verification-code',
           methods=['POST'],
           endpoint='confirm_code_e')
@token_is_exist
def confirm_code_e():
    try:
        repo = UserRepository()
        res = repo.check_code_e(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'email vcode is {}.'.format(str(res)),
                              }, 200))
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


@app.route('/user/add-address',
           methods=['POST'],
           endpoint='add_address')
@token_is_exist
def add_address():
    try:
        repo = UserRepository()
        res = repo.add_address(**request.args)
        return make_response(({
                                  'status': 'ok',
                                  'code': error_codes.OK_STATUS,
                                  'message': 'Address added.',
                              }, 200))
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
