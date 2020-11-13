from application import app
from application.models import User

# data = {
#     'phone_number': 'phone_number_for_test',
#     'phone_number_is_validated': True,
#     'email': 'email_for_tst',
#     'password': 'password_for_test',
#     'first_name': 'first_name_for_test',
#     'last_name': 'last_name_for_test'
# }
#
# user = User()
# user.phone_number = "phone number"
# user.phone_is_valid = True
# user.first_name = "first name"
# user.password = "password"

if __name__ == '__main__':
    app.run()