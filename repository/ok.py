import os
import logging
from dotenv import load_dotenv

logging.debug(os.getenv('MESSAGE_LAGUEAGE_CHOICES'))
load_dotenv()
logging.debug(os.getenv('MESSAGE_LAGUEAGE_CHOICES'))

if os.getenv('MESSAGE_LAGUEAGE_CHOICES') == 'persian':
    OK_STATUS = 'OK'
    NOK_STATUS = 'NOK'

    SIGNUP_CODE = 270
    SIGNUP_MESSAGE = 'ثبت نام کاربر با موفقیت انجام شد.'

    LOGIN_CODE = 271
    LOGIN_MESSAGE = 'ورود کاربر موفقیت آمیز بود.'

    LOGOUT_CODE = 272
    LOGOUT_MESSAGE = 'خروج کاربر موفقیت آمیز بود.'

    UPDATE_PASSWORD_CODE = 273
    UPDATE_PASSWORD_MESSAGE = 'گذرواژه بروزرسانی شد.'

    UPDATE_PHONE_NUMBER_CODE = 274
    UPDATE_PHONE_NUMBER_MESSAGE = 'شماره تلفن به روزرسانی شد.'

    UPDATE_EMAIL_ADDRESS_CODE = 275
    UPDATE_EMAIL_ADDRESS_MESSAGE = 'آدرس ایمیل به روزرسانی شد.'

    UPDATE_USER_INFORMATION_CODE = 276
    UPDATE_USER_INFORMATION_MESSAGE = 'اطلاعات تکمیلی کاربر به روز رسانی شد.'

    UPDATE_COMPANY_INFORMATION_CODE = 277
    UPDATE_COMPANY_INFORMATION_MESSAGE = 'اطلاعات کمپانی به روزرسانی شد.'

    UPDATE_CONFIGURATIONS_CODE = 278
    UPDATE_CONFIGURATIONS_MESSAGE = 'کانفیگوریشن به روزرسانی شد.'

    RECOVERY_BY_SEND_SMS_CODE = 279
    RECOVERY_BY_SEND_SMS_MESSAGE = 'بازیابی رمز عبور با ارسال پیام به شماره تلفن کاربر انجام شد.'

    RECOVERY_BY_SEND_EMAIL_CODE = 280
    RECOVERY_BY_SEND_EMAIL_MESSAGE = 'بازیابی رمز عبور با ارسال پیام به آدرس ایمیل کاربر انجام شد.'

    RECOVERY_BY_LAST_PASSWORD_CODE = 281
    RECOVERY_BY_LAST_PASSWORD_MESSAGE = 'ورود کاربر با استفاده از رمز عبور قبلی انجام شد.'

    RECOVERY_BY_ANSWERS_CODE = 282
    RECOVERY_BY_ANSWERS_MESSAGE = 'ورود کاربر با استفاده از پاسخ به سوالات از پیش پرسیده شده، انجام شد.'

    DELETE_ACCOUNT_CODE = 283
    DELETE_ACCOUNT_MESSAGE = 'پاک کردن اکانت با موفقیت انجام شد.'

    SEND_VCODE_FOR_PHONE_NUMBER_CODE = 284
    SEND_VCODE_FOR_PHONE_NUMBER_MESSAGE = 'کد تأیید به شماره تلفن کاربر ارسال شد.'

    SEND_VCODE_FOR_EMAIL_ADDRESS_CODE = 285
    SEND_VCODE_FOR_EMAIL_ADDRESS_MESSAGE = 'کد تأیید به آدرس ایمیل کاربر ارسال شد.'

    CONFIRM_VCODE_FOR_PHONE_NUMBER_CODE = 286
    CONFIRM_VCODE_FOR_PHONE_NUMBER_MESSAGE = 'کد ارسالی به شماره تلفن بررسی شد.'

    CONFIRM_VCODE_FOR_EMAIL_ADDRESS_CODE = 287
    CONFIRM_VCODE_FOR_EMAIL_ADDRESS_MESSAGE = 'کد ارسال شده به آدرس ایمیل بررسی شد.'

    ADD_ADDRESS_CODE = 288
    ADD_ADDRESS_MESSAGE = 'آدرس ذخیره شد.'

    GET_ADDRESSES_CODE = 289
    GET_ADDRESSES_MESSAGE = 'لیست آدرس ها ارسال شد.'

    GET_ACTIVE_SESSIONS_CODE = 290
    GET_ACTIVE_SESSIONS_MESSAGE = 'لیست سشن های فعال ارسال شد.'

    DEL_SESSION_CODE = 291
    DEL_SESSION_MESSAGE = 'سشن مورد نظر پاک شد.'

    DEL_ALL_SESSION_CODE = 292
    DEL_ALL_SESSION_MESSAGE = 'تمام سش های فعال مربوطه پاک شدند.'

    USER_IS_LOGIN_CODE = 293
    USER_IS_LOGIN_MESSAGE = 'کاربر لاگین می باشد.'

    GET_USERS_CODE = 294
    GET_USER_MESSAGE = 'لیست کاربران ارسال شد.'

    SUPERUSER_ACCESS_MESSAGE = 'این قابلیت تنها برای کاربری که دارای role برابر با superuser می باشد، امکان پذیر است.'

    TOKEN_NOT_DEFINE_MESSAGE = 'توکن تعریف نشده است.'

    PREVIOUS_PASSWORD_INCORRECT_MESSAGE = 'پسوورد قبلی مطابقت ندارد.'

    ANSWER_WRONG_MESSAGE = 'پاسخ اشتباه است.'

    USER_EXIST_WITH_UUID_MESSAGE = 'کاربر موجود است و uuid آن برابر است با {}'

    # USERNAME_NOT_REGISTER_MESSAGE = 'کاربری با این نام کاربری ثبت نام نکرده است.'
    USERNAME_NOT_REGISTER_MESSAGE = 'نام کاربری با کلمه عبور مطابقت ندارد.'

    # PASSWORD_INCORRECT_MESSAGE = 'کلمه عبور اشتباه است.'
    PASSWORD_INCORRECT_MESSAGE = 'نام کاربری با کلمه عبور مطابقت ندارد.'

    PHONE_NUMBER_NOT_VALID_MESSAGE = 'شماره تلفن اشتباه است.'
    EMAIL_NOT_VALID_MESSAGE = 'آدرس ایمیل اشتباه است.'

    USER_NOT_DEFINE_MESSAGE = 'کاربری با این مشخصات وجود ندارد.'

    FROM_REPOSITORY_DOT_PAGE_DOT_RECOVERY_MESSAGE = 'from repository.page_recovery'

    IMPORTED_SESSION_MESSAGE = "سشن وارد شده وجود ندارد یا به اشتباه وارد شده است."

    ENTER_USERNAME_MESSAGE = 'کلمه عبور یا شماره تلفن ویا ایمیل آدرس وارد کنید.'

    INPUT_NOT_SET_MESSAGE = " ورودی {} تنظیم نشده است."

    INPUT_LENGTH_NOT_SET_MESSAGE = "طول ورودی {} صحیح نمی باشد."
    INPUT_TYPE_NOT_SET_MESSAGE = " نوع ورودی {} صحیح نمی باشد."
    STATUS_NOT_SET_MESSAGE = "'status' وارد نشده است."
    MESSAGE_NOT_SET_MESSAGE = "'message' وارد نشده است."
    CODE_NOT_SET_MESSAGE = "'code' وارد نشده است."
    DATA_NOT_SET_MESSAGE = "'data' وارد نشده است."
    OUTPUT_NOT_SET_MESSAGE = " خروجی {} تنظیم نشده است."
    TYPE_NAME_IS_NOT_DEFINE_MESSAGE = 'نوع داده ای فرستاده شده صحیح نمی باشد.'
    RANDOM_QUESTION_SEND_MESSAGE = 'پرسش رندوم ارسال شد.'
    RANDOM_QUESTION_SEND_CODE = 220
    LIMITED_SMS_MESSAGE = "شما بیشتر از حد مجاز درخواست ارسال کد تایید را به سیستم داده اید. لطفا ۲۴ ساعت بعد " \
                          "دوباره سعی کنید. "
    LIMITED_SMS_RECOVERY_MESSAGE = "شما بیشتر از حد مجاز از بازیابی رمز عبور با استفاده از اس ام اس استفاده نموده " \
                                   "اید. در صورت امکان برای بازیابی رمز عبور از روش های دیگر استفاده کنید و در صورتی " \
                                   "که مایل هستید از این روش استفاده کنید ۲۴ ساعت دیگر دوباره امتحان کنید. "

if os.getenv('MESSAGE_LAGUEAGE_CHOICES') == 'eng':
    OK_STATUS = 'OK'
    NOK_STATUS = 'NOK'

    SIGNUP_CODE = 270
    SIGNUP_MESSAGE = 'Registration completed successfully.'

    LOGIN_CODE = 271
    LOGIN_MESSAGE = 'User login done.'

    LOGOUT_CODE = 272
    LOGOUT_MESSAGE = 'User logged out.'

    UPDATE_PASSWORD_CODE = 273
    UPDATE_PASSWORD_MESSAGE = 'Password updated.'

    UPDATE_PHONE_NUMBER_CODE = 274
    UPDATE_PHONE_NUMBER_MESSAGE = 'Phone number updated.'

    UPDATE_EMAIL_ADDRESS_CODE = 275
    UPDATE_EMAIL_ADDRESS_MESSAGE = 'Email address updated.'

    UPDATE_USER_INFORMATION_CODE = 276
    UPDATE_USER_INFORMATION_MESSAGE = 'User information updated.'

    UPDATE_COMPANY_INFORMATION_CODE = 277
    UPDATE_COMPANY_INFORMATION_MESSAGE = 'Company information updated.'

    UPDATE_CONFIGURATIONS_CODE = 278
    UPDATE_CONFIGURATIONS_MESSAGE = 'Configurations updated.'

    RECOVERY_BY_SEND_SMS_CODE = 279
    RECOVERY_BY_SEND_SMS_MESSAGE = 'Password recovery was performed by sending a message to the user\'s phone number.'

    RECOVERY_BY_SEND_EMAIL_CODE = 280
    RECOVERY_BY_SEND_EMAIL_MESSAGE = 'Password recovery was performed by sending a message to the user\'s email address.'

    RECOVERY_BY_LAST_PASSWORD_CODE = 281
    RECOVERY_BY_LAST_PASSWORD_MESSAGE = 'User login was done using the previous password.'

    RECOVERY_BY_ANSWERS_CODE = 282
    RECOVERY_BY_ANSWERS_MESSAGE = 'User login was done using the answers to the previously asked questions.'

    DELETE_ACCOUNT_CODE = 283
    DELETE_ACCOUNT_MESSAGE = 'Delete account completed.'

    SEND_VCODE_FOR_PHONE_NUMBER_CODE = 284
    SEND_VCODE_FOR_PHONE_NUMBER_MESSAGE = 'The verification code was sent to the user\'s phone number.'

    SEND_VCODE_FOR_EMAIL_ADDRESS_CODE = 285
    SEND_VCODE_FOR_EMAIL_ADDRESS_MESSAGE = 'The verification code was sent to the user\'s email address.'

    CONFIRM_VCODE_FOR_PHONE_NUMBER_CODE = 286
    CONFIRM_VCODE_FOR_PHONE_NUMBER_MESSAGE = 'The code sent to the phone number was checked.'

    CONFIRM_VCODE_FOR_EMAIL_ADDRESS_CODE = 287
    CONFIRM_VCODE_FOR_EMAIL_ADDRESS_MESSAGE = 'The code sent to the email address was checked.'

    ADD_ADDRESS_CODE = 288
    ADD_ADDRESS_MESSAGE = 'Address saved.'

    GET_ADDRESSES_CODE = 289
    GET_ADDRESSES_MESSAGE = 'List of addresses sent.'

    GET_ACTIVE_SESSIONS_CODE = 290
    GET_ACTIVE_SESSIONS_MESSAGE = 'List of active sessions.'

    DEL_SESSION_CODE = 291
    DEL_SESSION_MESSAGE = 'Delete session completed.'

    DEL_ALL_SESSION_CODE = 292
    DEL_ALL_SESSION_MESSAGE = 'Delete all active session completed.'

    USER_IS_LOGIN_CODE = 293
    USER_IS_LOGIN_MESSAGE = 'The user is logged in.'

    GET_USERS_CODE = 294
    GET_USER_MESSAGE = 'List of users sent.'

    SUPERUSER_ACCESS_MESSAGE = 'This access is given only to the superuser.'

    TOKEN_NOT_DEFINE_MESSAGE = 'Token is not define.'

    PREVIOUS_PASSWORD_INCORRECT_MESSAGE = 'The previous password is incorrect.'

    ANSWER_WRONG_MESSAGE = 'The answers are wrong.'

    USER_EXIST_WITH_UUID_MESSAGE = 'user exist with uuid: {}'

    # USERNAME_NOT_REGISTER_MESSAGE = 'This username is not registered.'
    USERNAME_NOT_REGISTER_MESSAGE = 'Username does not match password.'

    # PASSWORD_INCORRECT_MESSAGE = 'The password is incorrect.'
    PASSWORD_INCORRECT_MESSAGE = 'Username does not match password.'

    PHONE_NUMBER_NOT_VALID_MESSAGE = 'phone_number is not valid.'
    EMAIL_NOT_VALID_MESSAGE = 'email address is not valid.'

    USER_NOT_DEFINE_MESSAGE = 'user is not define.'

    FROM_REPOSITORY_DOT_PAGE_DOT_RECOVERY_MESSAGE = 'from repository.page_recovery'

    IMPORTED_SESSION_MESSAGE = "Imported session does not exist or is entered incorrectly."

    ENTER_USERNAME_MESSAGE = 'enter username or email address or phone number.'

    INPUT_NOT_SET_MESSAGE = " Input {} is not set."

    INPUT_LENGTH_NOT_SET_MESSAGE = " {} input length is not set correctly."
    INPUT_TYPE_NOT_SET_MESSAGE = " Input data type {} is not set correctly."
    STATUS_NOT_SET_MESSAGE = "'status' is not in arguments."
    MESSAGE_NOT_SET_MESSAGE = "'message' is not in arguments."
    CODE_NOT_SET_MESSAGE = "'code' is not in arguments."
    DATA_NOT_SET_MESSAGE = "'data' is not in arguments."
    OUTPUT_NOT_SET_MESSAGE = " Output {} is not set."

    TYPE_NAME_IS_NOT_DEFINE_MESSAGE = 'Type name is not define.'
    RANDOM_QUESTION_SEND_MESSAGE = 'Random question sent.'
    RANDOM_QUESTION_SEND_CODE = 220

    LIMITED_SMS_MESSAGE = "You have requested more than the requested verification code. Please try again 24 hours " \
                          "later. "

    LIMITED_SMS_RECOVERY_MESSAGE = "You have overused password recovery using SMS. If possible, use other methods to " \
                                   "recover the password, and if you want to use this method, try again in 24 hours. "
