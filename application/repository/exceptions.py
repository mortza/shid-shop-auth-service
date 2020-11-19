class UserException(Exception):
    def __init__(self, **kwargs):
        super(UserException, self).__init__()
        self.message = kwargs['message'] if 'message' in kwargs else ''
        self.error_code = kwargs['error_code'] if 'error_code' in kwargs else -1