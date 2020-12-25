from repository.users import UserRepositoryBase
from application.models import User, Token, VCode, Address
from application import db
import json


class UserRepository(UserRepositoryBase):

    @staticmethod
    def _user_is_exist(user_name: str = None, phone_number: str = None, email: str = None) -> User:
        uemail: str
        uphone: str
        if user_name is None and \
                phone_number is None and \
                email is None:
            raise Exception('error in _user_is_exist')
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
            filter(or_(User.email == uemail,
                       User.phone_number == uphone)). \
            first()

    @staticmethod
    def _page_recovery_by_send_sms(user: User) -> dict:
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
            raise Exception('The previous password is incorrect.')
        user.password = last_password
        db.session.commit()
        return {'user_name': user.phone_number, 'temporary_password': last_password}

    @staticmethod
    def _page_recovery_by_answered_to_questions(user: User, answers: str) -> dict:
        # todo change answers format from str to dict and convert to string
        from werkzeug.security import check_password_hash
        if not check_password_hash(user.answers, answers):
            raise Exception('The answers are wrong.')
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

    def register(self, clean_data: dict) -> None:
        if 'email' not in clean_data:
            clean_data['email'] = None
        old_usr = self._user_is_exist(email=clean_data['email'], phone_number=clean_data['phone_number'])
        if old_usr is not None:
            raise Exception('user exist with uuid: {}'.format(old_usr.uid))
        usr = User(clean_data)
        db.session.add(usr)
        db.session.commit()
        db.create_all()
        return usr.to_dict

    def update(self, clean_data: dict, key: str):
        uid = clean_data['user_id']
        device_info = clean_data['auth_token_info_extract']['device_information']
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
            usr.user_information = clean_data['user_information']
        elif key == 'update_company_information':
            usr.company_information = clean_data['company_information']
        elif key == 'update_configurations':
            usr.configurations = clean_data['configurations']
        db.session.commit()
        return usr.to_dict

    def login(self, clean_data: dict) -> [Token, dict]:
        usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
        if usr is None:
            raise Exception('This username is not registered.')
        from werkzeug.security import check_password_hash
        if not check_password_hash(usr.password, clean_data['password']):
            raise Exception('The password is incorrect.')
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

    def page_recovery(self, clean_data: dict, key: str) -> dict:
        if key == 'recovery_by_send_sms':
            usr = UserRepository._user_is_exist(phone_number=clean_data['phone_number'])
            if usr is None:
                raise Exception('from repository.page_recovery: phone_number')
            return self._page_recovery_by_send_sms(usr)
        if key == 'recovery_by_send_email':
            usr = UserRepository._user_is_exist(email=clean_data['email'])
            if usr is None:
                raise Exception('from repository.page_recovery: email')
            return self._page_recovery_by_send_email(usr)
        if key == 'recovery_by_last_password':
            usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
            if usr is None:
                raise Exception('from repository.page_recovery: last password')
            return self._page_recovery_by_last_password(usr, clean_data['last_password'])
        if key == 'recovery_by_answers':
            usr = UserRepository._user_is_exist(user_name=clean_data['user_name'])
            if usr is None:
                raise Exception('from repository.page_recovery: answers')
            return self._page_recovery_by_answered_to_questions(usr, clean_data['answers'])
        # todo add true exception
        raise Exception('from repository.page_recovery:')

    def delete(self, clean_data: dict) -> Token:
        uid = clean_data['user_id']
        uid = int(uid)
        usr = db.session.query(User).filter(User.id == uid).first()
        tkns = usr.tokens
        db.session.delete(usr)
        db.session.commit()
        return tkns

    def create_verify_code(self, clean_data: dict, key: str) -> dict:
        uid = clean_data['user_id']
        uid = int(uid)
        v_code = VCode(uid)
        db.session.add(v_code)
        print(v_code)
        db.session.commit()
        usr = db.session.query(User).filter(User.id == int(uid)).first()
        ret = dict()
        if key == 'for_phone':
            phone_number = usr.phone_number
            vcode_for_phone = v_code.v_code_ph
            vcode_expiration_date = v_code.validity_date
            ret = {
                'phone_number': phone_number,
                'vcode_for_phone': vcode_for_phone,
                'vcode_expiration_date': vcode_expiration_date
            }
        elif key == 'for_email':
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

    def add_address(self, clean_data: dict) -> dict:
        address = Address(clean_data)
        db.session.add(address)
        db.session.commit()
        return address.to_dict

    def get_addresses(self, clean_data: dict) -> dict:
        uid = clean_data['user_id']
        usr = db.session.query(User).filter(User.id == uid).first()
        ret = dict()
        page = int(clean_data['page']) if 'page' in clean_data else 1
        ret['addresses'] = self._jsonify_pagination(
            db.session.query(Address).filter(Address.user_id == usr.id).paginate(page))
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
            raise Exception("Imported session does not exist or is entered incorrectly.")
        db.session.delete(tkn)
        db.session.commit()

    def delete_all_sessions(self, clean_data: dict) -> Token:
        uid = clean_data['user_id']
        auth_tkn = clean_data['auth_token']
        tkns = db.session.query(Token).filter((Token.user_id == uid) & (Token.token != auth_tkn)).all()
        db.session.query(Token).filter((Token.user_id == uid) & (Token.token != auth_tkn)).delete()
        db.session.commit()
        return tkns
