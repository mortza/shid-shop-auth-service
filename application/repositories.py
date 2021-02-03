from flask import make_response, jsonify

from repository.users import UserRepositoryBase
from application.models import User, Token, VCode
from application import db
import json

from repository.ok import *


class UserRepository(UserRepositoryBase):

    @staticmethod
    def _user_is_exist(user_name: str = None, phone_number: str = None, email: str = None) -> User:
        uemail: str
        uphone: str
        if user_name is None and \
                phone_number is None and \
                email is None:
            raise Exception(ENTER_USERNAME_MESSAGE)
        elif phone_number is not None and \
                email is None:
            uphone = phone_number
            uemail = phone_number
        elif email is not None and \
                phone_number is None:
            uphone = email
            uemail = email
        elif email is not None and \
                phone_number is not None:
            uemail = email
            uphone = phone_number
        else:
            uemail = user_name
            uphone = user_name

        from sqlalchemy import or_
        return db.session.query(User). \
            filter(or_(User.username == user_name,
                       User.username == phone_number,

                       User.phone_number == user_name,
                       User.phone_number == phone_number,
                       )
                   ).first()

    @staticmethod
    def _page_recovery_by_send_sms(user: User) -> dict:

        user.set_sms_num
        if not user.check_send_sms:
            raise Exception(LIMITED_SMS_RECOVERY_MESSAGE)

        import string
        import random
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=8))
        user.last_password_hash = user.password
        user.password = res
        db.session.commit()
        return {'user_name': user.phone_number, 'temporary_password': res}

    @staticmethod
    def _page_recovery_by_send_email(user: User) -> dict:
        import string
        import random
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=10))
        user.last_password_hash = user.password
        user.password = res
        db.session.commit()
        return {'user_name': user.email, 'temporary_password': res}

    @staticmethod
    def _page_recovery_by_last_password(user: User, last_password: str) -> dict:
        from werkzeug.security import check_password_hash
        if not check_password_hash(user.last_password_hash, last_password):
            raise Exception(PREVIOUS_PASSWORD_INCORRECT_MESSAGE)
        user.password = last_password
        db.session.commit()
        return {'user_name': user.phone_number, 'temporary_password': last_password}

    @staticmethod
    def _page_recovery_by_answered_to_questions(user: User, question_answring: json) -> dict:
        if question_answring == user.question_answring_1:
            pass
        elif question_answring == user.question_answring_2:
            pass
        elif question_answring == user.question_answring_3:
            pass
        elif question_answring == user.question_answring_4:
            pass
        elif question_answring == user.question_answring_5:
            pass
        else:
            raise Exception(ANSWER_WRONG_MESSAGE)

        import string
        import random
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=20))
        user.last_password_hash = user.password
        user.password = res
        db.session.commit()
        return {'user_name': user.phone_number, 'temporary_password': res}

    @staticmethod
    def _create_list() -> dict:
        pass

    def register(self, clean_data: dict):
        if 'email' not in clean_data:
            clean_data['email'] = None
        old_usr = self._user_is_exist(email=clean_data['email'], phone_number=clean_data['phone_number'])
        if old_usr is not None:
            raise Exception([USER_EXIST_WITH_UUID_MESSAGE, old_usr.uid])
        try:
            usr = User(clean_data)
            db.session.add(usr)
            db.session.commit()
            db.create_all()
            return usr.to_dict
        except Exception as ex:
            err_t = ex.args[0]
            err_t = err_t.split(":")
            err_t = err_t[1]
            err_t = [UNIQUE_CONSTRAINT_FAILED, err_t]
            raise Exception(err_t)

    def update(self, clean_data: dict, key: str):
        uid = clean_data['user_id']
        usr = db.session.query(User).filter(User.id == uid).first()
        if key == 'update_phone_number':
            usr.phone_number_is_validated = False
            usr.phone_number = clean_data['phone_number']
        elif key == 'update_email':
            usr.email_is_validated = False
            usr.email = clean_data['email']
        elif key == 'update_password':
            tkns = usr.tokens
            user_name = usr.phone_number
            usr.last_password_hash = usr.password
            usr.password = clean_data['password']
            db.session.query(Token).filter(Token.user_id == uid).delete()
            db.session.commit()
            return tkns, user_name
        elif key == 'update_user_information':
            if 'user_information' in clean_data:
                usr.user_information = clean_data['user_information']
            if 'first_name' in clean_data:
                usr.first_name = clean_data['first_name']
            if 'last_name' in clean_data:
                usr.last_name = clean_data['last_name']
            if 'national_id' in clean_data:
                usr.national_id = clean_data['national_id']
            if 'gender' in clean_data:
                usr.gender = clean_data['gender']
            if 'birthday' in clean_data:
                usr.birthday = clean_data['birthday']
        elif key == 'update_company_information':
            if 'company_information' in clean_data:
                usr.company_information = clean_data['company_information']
            if 'company_name' in clean_data:
                usr.company_name = clean_data['company_name']
            if 'economic_code' in clean_data:
                usr.economic_code = clean_data['economic_code']
            if 'national_id_company_owner' in clean_data:
                usr.national_id_company_owner = clean_data['national_id_company_owner']
            if 'registration_id' in clean_data:
                usr.registration_id = clean_data['registration_id']
        elif key == 'update_configurations':
            usr.configurations = clean_data['configurations']

        info = usr.to_dict
        info['user_id'] = usr.id
        tkns = db.session.query(Token).filter(Token.user_id == usr.id).all()
        for tkn in tkns:
            t_info = json.loads(tkn.information)
            device_info = t_info['device_information']
            info['device_information'] = device_info
            h_info = json.dumps(info)
            tkn.information = h_info
        db.session.commit()
        return usr.to_dict, tkns

    def login(self, clean_data: dict) -> [Token, dict]:
        usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
        if usr is None:
            raise Exception(USERNAME_NOT_REGISTER_MESSAGE)
        from werkzeug.security import check_password_hash
        if not check_password_hash(usr.password, clean_data['password']):
            raise Exception(PASSWORD_INCORRECT_MESSAGE)
        if 'device_information' not in clean_data:
            clean_data['device_information'] = '{}'
        info = usr.to_dict
        info['device_information'] = clean_data['device_information']
        info['user_id'] = usr.id
        info = json.dumps(info)
        tkn = Token(user_id=usr.id, info=info)
        db.session.add(tkn)
        db.session.commit()
        ret = usr.to_dict
        ret['auth_token'] = tkn.token
        ret['data'] = ret
        rkey = tkn.token
        rvalue = tkn.information
        return rkey, rvalue, ret

    def logout(self, clean_data: dict) -> Token:
        tkn = clean_data['auth_token']
        db.session.query(Token).filter(Token.token == tkn).delete()
        db.session.commit()
        return tkn

    def rand_question(self, clean_data: dict):
        usr = UserRepository._user_is_exist(phone_number=clean_data['user_name'])
        import random
        import json
        q_num = random.randint(1, 5)
        if q_num == 1:
            question = usr.question_answring_1
            question = json.loads(question)
            question = question.keys()
            question = list(question)
            question = question[0]
            return {'question': question}
        if q_num == 2:
            question = usr.question_answring_2
            question = json.loads(question)
            question = question.keys()
            question = list(question)
            question = question[0]
            return {'question': question}
        if q_num == 3:
            question = usr.question_answring_3
            question = json.loads(question)
            question = question.keys()
            question = list(question)
            question = question[0]
            return {'question': question}
        if q_num == 4:
            question = usr.question_answring_4
            question = json.loads(question)
            question = question.keys()
            question = list(question)
            question = question[0]
            return {'question': question}
        if q_num == 5:
            question = usr.question_answring_5
            question = json.loads(question)
            question = question.keys()
            question = list(question)
            question = question[0]
            return {'question': question}

    def page_recovery(self, clean_data: dict, key: str) -> dict:
        if key == 'recovery_by_send_sms':
            usr = UserRepository._user_is_exist(phone_number=clean_data['phone_number'])
            if usr is None:
                raise Exception(USER_NOT_DEFINE_MESSAGE)
            return self._page_recovery_by_send_sms(usr)
        if key == 'recovery_by_send_email':
            usr = UserRepository._user_is_exist(email=clean_data['email'])
            if usr is None:
                raise Exception(USER_NOT_DEFINE_MESSAGE)
            return self._page_recovery_by_send_email(usr)
        if key == 'recovery_by_last_password':
            usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
            if usr is None:
                raise Exception(USER_NOT_DEFINE_MESSAGE)
            return self._page_recovery_by_last_password(usr, clean_data['last_password'])
        if key == 'recovery_by_answers':
            usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
            if usr is None:
                raise Exception(USER_NOT_DEFINE_MESSAGE)
            return self._page_recovery_by_answered_to_questions(usr, clean_data['question_answring'])
        raise Exception(FROM_REPOSITORY_DOT_PAGE_DOT_RECOVERY_MESSAGE)

    def delete(self, clean_data: dict) -> Token:
        uid = clean_data['user_id']
        uid = int(uid)
        usr = db.session.query(User).filter(User.id == uid).first()
        tkns = usr.tokens
        db.session.delete(usr)
        db.session.commit()
        return tkns

    def create_verify_code(self, clean_data: dict, key: str) -> dict:
        if key == 'for_phone':
            uid = clean_data['user_id']
            uid = int(uid)
            usr = db.session.query(User).filter(User.id == int(uid)).first()
            vcodes = db.session.query(VCode).filter(VCode.user_id == usr.id).all()
            import datetime
            now = datetime.datetime.now()
            for vc in vcodes:
                if vc.validity_date < now:
                    db.session.query(VCode).filter(VCode.id == vc.id).delete()
            db.session.commit()
            if len(vcodes) >= 2:
                raise Exception(LIMITED_SMS_MESSAGE)
            v_code = VCode(uid)
            db.session.add(v_code)
            db.session.commit()
            ret = dict()

            phone_number = usr.phone_number
            vcode_for_phone = v_code.v_code_ph
            vcode_expiration_date = v_code.validity_date
            ret = {
                'phone_number': phone_number,
                'vcode_for_phone': vcode_for_phone,
                'vcode_expiration_date': vcode_expiration_date
            }
            return ret
        elif key == 'for_email':
            uid = clean_data['user_id']
            uid = int(uid)
            usr = db.session.query(User).filter(User.id == int(uid)).first()
            v_code = VCode(uid)
            db.session.add(v_code)
            db.session.commit()
            ret = dict()

            email_address = usr.email
            vcode_for_email = v_code.v_code_e
            vcode_expiration_date = v_code.validity_date
            ret = {
                'email_address': email_address,
                'vcode_for_email': vcode_for_email,
                'vcode_expiration_date': vcode_expiration_date
            }
            return ret

    def check_code(self, clean_data: dict, key: str) -> bool:
        uid = clean_data['user_id']
        uid = int(uid)
        v_code = clean_data['vcode']
        usr = db.session.query(User).filter(User.id == uid).first()
        import datetime
        d = datetime.datetime.now()
        if key == 'for_phone':
            for vc in usr.v_codes:
                if vc.v_code_ph == v_code and d < vc.validity_date:
                    usr.phone_number_is_validated = True
                    db.session.query(VCode).filter(VCode.id == vc.id).delete()
                    db.session.commit()
                    return True
        elif key == 'for_email':
            for vc in usr.v_codes:
                if vc.v_code_e == v_code and d < vc.validity_date:
                    usr.email_is_validated = True
                    db.session.query(VCode).filter(VCode.id == vc.id).delete()
                    db.session.commit()
                    return True
        return False

    def get_users(self, clean_data: dict) -> dict:
        usr_id = clean_data['user_id']
        usr = db.session.query(User).filter(User.id == usr_id).first()
        u_role = usr.role
        u_role = u_role.lower()
        if u_role.find('superuser') == 0:
            raise Exception(SUPERUSER_ACCESS_MESSAGE)
        ret = dict()
        page = int(clean_data['page']) if 'page' in clean_data else 1
        ret['users'] = self._jsonify_pagination(
            db.session.query(User).paginate(page))
        return ret

    def active_session(self, clean_data: dict) -> dict:
        uid = clean_data['user_id']
        usr = db.session.query(User).filter(User.id == uid).first()
        ret = dict()
        ret['sessions'] = usr.session_list
        return ret

    def _jsonify_pagination(self, data):
        ret = {
            'has_next': data.has_next,
            'next_num': data.next_num,
            'page': data.page,
            'pages': data.pages,
            'per_page': data.per_page,
            'prev_num': data.prev_num,
            'total': data.total,
            'items': [i.to_dict for i in data.items]
        }
        return ret

    def delete_session(self, clean_data: dict) -> None:
        sess = clean_data['session']
        tkn = db.session.query(Token).filter(Token.token == sess).first()
        if tkn is None:
            raise Exception(IMPORTED_SESSION_MESSAGE)
        db.session.delete(tkn)
        db.session.commit()

    def delete_all_sessions(self, clean_data: dict) -> Token:
        uid = clean_data['user_id']
        auth_tkn = clean_data['auth_token']
        tkns = db.session.query(Token).filter((Token.user_id == uid) & (Token.token != auth_tkn)).all()
        db.session.query(Token).filter((Token.user_id == uid) & (Token.token != auth_tkn)).delete()
        db.session.commit()
        return tkns


def send_email(receiver, message_text):
    import smtplib
    import ssl

    smtp_server = os.getenv('MAIL_SERVER')
    port = os.getenv('MAIL_PORT')
    sender_email = os.getenv('MAIL_SENDER')
    password = os.getenv('MAIL_PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message_text)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


def send_sms(receiver, message_text):
    from application import melipayamak_api
    sms = melipayamak_api.sms()
    response = sms.send(to=receiver,
                        _from=os.getenv('SMS_MELIPAYAMAK_FROM'),
                        text=message_text
                        )
    return response
