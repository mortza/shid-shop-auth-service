class UserException(Exception):
    def __init__(self, **kwargs):
        super(UserException, self).__init__()
        self.message = kwargs['message'] if 'message' in kwargs else ''
        self.error_code = kwargs['error_code'] if 'error_code' in kwargs else -1


class TokenException(Exception):
    def __init__(self, **kwargs):
        super(TokenException, self).__init__()
        self.message = kwargs['message'] if 'message' in kwargs else ''
        self.error_code = kwargs['error_code'] if 'error_code' in kwargs else -1


class ArgsException(Exception):
    def __init__(self, **kwargs):
        super(ArgsException, self).__init__()
        self.message = kwargs['message'] if 'message' in kwargs else ''
        self.error_code = kwargs['error_code'] if 'error_code' in kwargs else -1
