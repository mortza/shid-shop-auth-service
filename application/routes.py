from flask import request, render_template, make_response, redirect, url_for
from datetime import datetime as dt
from application import app
from .repository import UserRepository, UserRepositoryException


@app.route('/register', methods=['POST'])
def register():
    try:
        repo = UserRepository()
        ret = repo.register(**request.args)
        return make_response(ret)
    except UserRepositoryException as ex:
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
    pass


@app.route('/delete-user-account', methods=['POST'])
def delete_user_account():
    pass


@app.route('/login', methods=['POST'])
def login():
    pass


@app.route('/logout', methods=['POST'])
def logout():
    pass
