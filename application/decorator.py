from functools import wraps
from flask import request, make_response, jsonify
from application import redis_client, db, adata
from application.models import Token

from repository.ok import *


def cleanData(rule):
    def decorator(func):
        @wraps(func)
        def decorated_function():
            try:
                i_c_data = adata.input(request.form, rule)
                res = func(i_c_data)
                o_c_data = adata.output(res, rule)
                data = {}
                if 'information' in o_c_data:
                    if 'auth_token' in o_c_data['information']:
                        data['token'] = o_c_data['information']['auth_token']
                        del o_c_data['information']['auth_token']
                    if len(o_c_data['information']) > 0:
                        data['user'] = o_c_data['information']
                return make_response(
                    jsonify(
                        {

                            'succsess': True,
                            'message': o_c_data['message'],
                            'data': data,
                        }),
                    200,
                )
            except Exception as ex:
                return make_response(
                    jsonify(
                        {

                            'succsess': False,
                            'message': ex.args,
                            'data': '',
                        }),
                    200)

        return decorated_function

    return decorator


def is_login(rule):
    def decorator(func):
        @wraps(func)
        def decorated_function():
            try:
                i_c_data = adata.input(request.form, rule)
                auth_token = i_c_data['auth_token']
                redis_value = redis_client.get(auth_token)
                if redis_value:
                    import json
                    auth_token_info_extract = json.loads(redis_value)
                    i_c_data['user_id'] = auth_token_info_extract['user_id']
                    i_c_data['auth_token_info_extract'] = auth_token_info_extract
                    res = func(i_c_data)
                    o_c_data = adata.output(res, rule)
                    data = {}
                    if 'information' in o_c_data:
                        if 'auth_token' in o_c_data['information']:
                            data['token'] = o_c_data['information']['auth_token']
                            del o_c_data['information']['auth_token']
                        if len(o_c_data['information']) > 0:
                            data['user'] = o_c_data['information']
                        if 'users' in o_c_data['information']:
                            del data['user']
                            data = o_c_data['information']['users']
                    return make_response(
                        jsonify(
                            {

                                'succsess': True,
                                'message': o_c_data['message'],
                                'data': data,
                            }),
                        200,
                    )
                else:
                    auth_token = db.session.query(Token).filter(Token.token == auth_token).first()
                    if auth_token is not None:
                        redis_client.set(auth_token.token, auth_token.information)
                        import json
                        auth_token_info_extract = json.loads(auth_token.information)
                        i_c_data['user_id'] = auth_token_info_extract['user_id']
                        i_c_data['auth_token_info_extract'] = auth_token_info_extract
                        res = func(i_c_data)
                        o_c_data = adata.output(res, rule)
                        data = {}
                        if 'information' in o_c_data:
                            if 'auth_token' in o_c_data['information']:
                                data['token'] = o_c_data['information']['auth_token']
                                del o_c_data['information']['auth_token']
                            if len(o_c_data['information']) > 0:
                                data['user'] = o_c_data['information']
                        return make_response(
                            jsonify(
                                {

                                    'succsess': True,
                                    'message': o_c_data['message'],
                                    'data': data,
                                }),
                            200,
                        )
                    else:
                        raise Exception(TOKEN_NOT_DEFINE_MESSAGE)
            except Exception as ex:
                return make_response(
                    jsonify(
                        {

                            'succsess': False,
                            'message': ex.args,
                            'data': '',
                        }),
                    200)

        return decorated_function

    return decorator
