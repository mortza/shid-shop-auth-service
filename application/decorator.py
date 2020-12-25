from functools import wraps
from flask import request, make_response, jsonify
from application import redis_client, db, adata
from application.models import Token


def cleanData(rule):
    def decorator(func):
        @wraps(func)
        def decorated_function():
            try:
                i_c_data = adata.input(request.form, rule)
                res = func(i_c_data)
                o_c_data = adata.output(res, rule)
                return make_response(
                    jsonify(
                        {
                            'status': o_c_data['status'],
                            'code': o_c_data['code'],
                            'message': o_c_data['message'],
                            'information': o_c_data['information'],
                        }),
                    200,
                )
            except Exception as ex:
                return make_response(
                    jsonify(
                        {
                            'status': 'error',
                            'code': '-1',
                            'message': ex.args,
                            'information': '',
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
                    return make_response(
                        jsonify(
                            {
                                'status': o_c_data['status'],
                                'code': o_c_data['code'],
                                'message': o_c_data['message'],
                                'information': o_c_data['information'],
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
                        return make_response(
                            jsonify(
                                {
                                    'status': o_c_data['status'],
                                    'code': o_c_data['code'],
                                    'message': o_c_data['message'],
                                    'information': o_c_data['information'],
                                }),
                            200,
                        )
                    else:
                        raise Exception('Token is not define.')
            except Exception as ex:
                return make_response(
                    jsonify(
                        {
                            'status': 'error',
                            'code': '-1',
                            'message': ex.args,
                            'information': '',
                        }),
                    200)

        return decorated_function

    return decorator
