from flask import request, render_template, make_response, redirect, url_for
from datetime import datetime as dt
from application import app
from .repository import UserRepository, UserException


@app.route('/register', methods=['POST'])
def register():
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


@app.route('/register/validate-phone', methods=['POST'])
def validate_phone_number():
    pass


@app.route('/update-user-profile', methods=['POST'])
def update_user_profile():
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


@app.route('/update-password-profile', methods=['POST'])
def update_user_password():
    pass


@app.route('/update-email-profile', methods=['POST'])
def update_user_email():
    pass


@app.route('/delete-user-account', methods=['POST'])
def delete_user_account():
    pass


@app.route('/login', methods=['POST'])
def login():
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
    pass
