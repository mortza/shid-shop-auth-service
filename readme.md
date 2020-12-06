# AUTH SERVICE
این یک سیستم مدیریت کاربران است که به زبان برنامه نویسی پایتون و با استفاده از فریمورک فلسک نوشته شده است.

## ساختار استفاده از توابع درون سرویس
شکل کلی کار کردن با توابع درون سرویس بصورت زیر می باشد:
```python
{
    'request URL': 'path',
    'methods': '[POST or GET]',
    'Query Params': {
        'input': {
            'key': {
                'Value properties': ''
            }
        }
    },
    'Response': {
        "code": 'integer code',
        "information": {
            'output': {
                'key': {
                    'Value properties': ''
                }
            }
        },
        "message": "",
        "status": ""
    }
}
```
- request URL:
 <br />
  در این قسمت مسیر استفاده از هر تابع نمایش داده شده است.
- methods: 
<br />
این قسمت مربوط به متد مورد استفاده می باشد.
- Query Params:
 <br />
 در این قسمت مقادیر داده بصورت کلید-مقدار وارد می شود و هر مقدار متناظر با یک کلید ویژگی هایی دارد که عبارتند از:
 <br />
    - nullable:
    <br />
    این ویژگی بیانگر آن است که وجود داده ی موردنظر می تواند اختیاری یا اجباری باشد.
    <br />
        - True:
        <br />
         مقدار دهی اختیاری
        <br />
        - False:
        <br />
        مقداردهی اجباری
        <br />
    - max_length:
    <br />
    اندازه ی حداکثر طول داده مورد نظر می باشد.
    <br />
    - min_length:
    <br />
    اندازه ی حداقل طول داده مورد نظر می باشد.
    <br />
    - type:
    <br />
    نوع داده را مشخص می کند.
 - Response:
 <br />
 در اینجا مقدار ارسالی از تابع فرمت دهی شده است، در واقع تمام مقادیر خروجی از توابع این سرویس بر اساس چهار مقدار زیر فرمت دهی شده اند.
  <br />
    - code:
    <br />
    کدی که نمایانگر این ریسپانس است.
    <br />
    - information:
    <br />
    اطلاعاتی که برای توابع مختلف مقدار متفاوتی دارد و بصورت دیکشنری پایتونی به صورت کلید-مقدار برگردانده می شود و ویژگی مقادیر همانند ویژگی های در قسمت قبل تعریف و استفاده می شوند.
    <br />
    - message:
    <br />
    هر ریسپانس شامل پیغامی است که توضیحی مختصر در رابطه با عملیات انجام شده شرح می دهد.
    <br />
    - status:
    <br />
    این مقدار در ریسپانس مقدار استاتوس عملیات را بر میگرداند.
    <br />
*** 
None:
<br /> 
این مقدار به معنای نامشخص یا مشخص نشده می باشد.   
    
##ثبت نام کاربر 

```python
{
    'request URL': '/register',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'role': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'real_or_legal': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'phone_number': {
                'nullable': False,
                'max_length': 11,
                'min_length': 11,
                'type': 'snum'
            },
            'password': {
                'nullable': False,
                'max_length': None,
                'min_length': 8,
                'type': 'str'
            },
            'email': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'email'
            },
            'user_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'company_information': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'answers': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
            'configurations': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'auth_token': {
                    'nullable': False,
                    'type': 'str'
                },
                'role': {
                    'nullable': False,
                    'type': 'str'
                },
                'real_or_legal': {
                    'nullable': False,
                    'type': 'str'
                },
                'phone_number': {
                    'nullable': False,
                    'type': 'snum'
                },
                'email': {
                    'nullable': True,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'str'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                }, }
        }
    },
    "message": "",
    "status": ""
}
```

## ورود کاربر 
```python
{
    'request URL': '/login',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'user_name': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'password': {
                'nullable': False,
                'max_length': None,
                'min_length': 8,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'auth_token': {
                    'nullable': False,
                    'type': 'str'
                },
                'role': {
                    'nullable': False,
                    'type': 'str'
                },
                'real_or_legal': {
                    'nullable': False,
                    'type': 'str'
                },
                'phone_number': {
                    'nullable': False,
                    'type': 'snum'
                },
                'email': {
                    'nullable': True,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'str'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## خروج کاربر 
```python
{
    'request URL': '/logout',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بروز رسانی کلمه عبور
در این بروزرسانی زمانی که کلمه ی عبور تغییر پیدا می کند، تمامی لاگین ها از سیستم های مختلف کاربر، لاگاوت می شود و نیاز است که کاربر برای ورود با رمز جدید برای ورود اقدام کند.  
```python
{
    'request URL': '/user/update/password',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'password': {
                'nullable': False,
                'max_length': None,
                'min_length': 8,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'auth_token': {
                    'nullable': False,
                    'type': 'str'
                },
                'role': {
                    'nullable': False,
                    'type': 'str'
                },
                'real_or_legal': {
                    'nullable': False,
                    'type': 'str'
                },
                'phone_number': {
                    'nullable': False,
                    'type': 'snum'
                },
                'email': {
                    'nullable': True,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'str'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## بروزرسانی شماره تلفن
در این بروز رسانی فعال بودن شماره تلفن به حالت فالس تبدیل میشود وبرای اعتبار سنجی و فعال ساختن شماره تلفن، کاربر اقدامات لازم را انجام دهد. 
```python
{
    'request URL': '/user/update/phone-number',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'phone_number': {
                'nullable': False,
                'max_length': 11,
                'min_length': 11,
                'type': 'snum'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بروزرسانی آدرس ایمیل
در این بروز رسانی فعال بودن آدرس ایمیل به حالت فالس تبدیل میشود وبرای اعتبار سنجی و فعال ساختن آدرس ایمیل، کاربر اقدامات لازم را انجام دهد. 
```python
{
    'request URL': '/user/update/email',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'email': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'email'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بروز رسانی اطلاعات کاربر حقیقی 
```python
{
    'request URL': '/user/update/user-information',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'user_information': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بروز رسانی اطلاعات کاربر حقوقی
```python
{
    'request URL': '/user/update/company-information',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'company_information': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بروزرسانی کانفیگوریشن ها 
```python
{
    'request URL': '/user/update/configurations',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'configurations': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بازیابی پروفایل کاربر در هنگام فراموشی کلمه عبور با استفاده از ارسال رمز موقت به شماره تلفن کاربر
```python
{
    'request URL': '/recovery-by/send-sms',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'phone_number': {
                'nullable': False,
                'max_length': 11,
                'min_length': 11,
                'type': 'snum'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بازیابی پروفایل کاربر در هنگام فراموشی کلمه عبور با استفاده از ارسال رمز موقت به آدرس ایمیل کاربر
```python
{
    'request URL': '/recovery-by/send-email',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'email': {
                'nullable': True,
                'max_length': None,
                'min_length': None,
                'type': 'email'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## بازیابی پروفایل کاربر و ورود کاربر در هنگام فراموشی کلمه عبور با استفاده از کلمه عبور قبلی کاربر
```python
{
    'request URL': '/recovery-by/last-password',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'user_name': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'last_password': {
                'nullable': False,
                'max_length': None,
                'min_length': 8,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'auth_token': {
                    'nullable': False,
                    'type': 'str'
                },
                'role': {
                    'nullable': False,
                    'type': 'str'
                },
                'real_or_legal': {
                    'nullable': False,
                    'type': 'str'
                },
                'phone_number': {
                    'nullable': False,
                    'type': 'snum'
                },
                'email': {
                    'nullable': True,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'str'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## بازیابی پروفایل کاربر و ورود کاربر در هنگام فراموشی کلمه عبور با استفاده پاسخ صحیح به پرسش های از قبل پرسیده شده
```python
{
    'request URL': '/recovery-by/answers',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'user_name': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'answers': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'auth_token': {
                    'nullable': False,
                    'type': 'str'
                },
                'role': {
                    'nullable': False,
                    'type': 'str'
                },
                'real_or_legal': {
                    'nullable': False,
                    'type': 'str'
                },
                'phone_number': {
                    'nullable': False,
                    'type': 'snum'
                },
                'email': {
                    'nullable': True,
                    'type': 'email'
                },
                'user_information': {
                    'nullable': True,
                    'type': 'json'
                },
                'company_information': {
                    'nullable': True,
                    'type': 'str'
                },
                'configurations': {
                    'nullable': True,
                    'type': 'json'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## حذف کامل کاربر 
```python
{
    'request URL': '/user/delete-account',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```

## ارسال کد تایید به شماره تلفن 
```python
{
    'request URL': '/register/vcode/send-sms',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'vcode_expiration_date': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## ارسال کد تایید به ایمیل کاربر 
```python
{
    'request URL': '/register/vcode/send-email',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'vcode_expiration_date': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## چک کردن صحت کد تایید از طریق اس ام اس
```python
{
    'request URL': '/register/vcode/send-sms/confirm',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'vcode': {
                'nullable': False,
                'max_length': 5,
                'min_length': 5,
                'type': 'snum'
            }
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'code_review_status': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## چک کردن صحت کد تایید از طریق ایمیل 
```python
{
    'request URL': '/register/vcode/send-email/confirm',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'vcode': {
                'nullable': False,
                'max_length': 4,
                'min_length': 4,
                'type': 'snum'
            }
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {
                'code_review_status': {
                    'nullable': False,
                    'max_length': None,
                    'min_length': None,
                    'type': 'str'
                },
            }
        }
    },
    "message": "",
    "status": ""
}
```

## اضافه کردن آدرس
```python
{
    'request URL': '/user/add-address',
    'methods': 'POST',
    'Query Params': {
        'input': {
            'auth_token': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'str'
            },
            'address': {
                'nullable': False,
                'max_length': None,
                'min_length': None,
                'type': 'json'
            }
        },
    },
    'Response': {
        "code": '',
        "information": {
            'output': {}
        }
    },
    "message": "",
    "status": ""
}
```