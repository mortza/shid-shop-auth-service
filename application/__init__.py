from application.config import Config, BASEDIR
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv
import os
from flask_redis import FlaskRedis

from repository.acceptabledata import AcceptableData
from flask_mail import Mail, Message

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

adata = AcceptableData()

load_dotenv()
application = Flask(__name__)
mail = Mail(application)


Config.MAIL_SERVER = os.getenv('MAIL_SERVER')
Config.MAIL_PORT = os.getenv('MAIL_PORT')
Config.MAIL_USERNAME = os.getenv('MAIL_USERNAME')
Config.MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
Config.MAIL_USE_TLS = False
Config.MAIL_USE_SSL = True

RATE_LIMIT = os.getenv('RATE_LIMIT')


redis_client = FlaskRedis(application)

if os.getenv('DB_TYPE') == 'sqlite':
    Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
elif os.getenv('DB_TYPE') == 'postgres':
    Config.SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=os.getenv('DB_USER'),
        pw=os.getenv('DB_PASSWORD'),
        url=os.getenv('DB_URL'),
        db=os.getenv('DB_NAME')
    )

application.config.from_object(Config)

db = SQLAlchemy(application)
mail = Mail(application)
migrate = Migrate(application, db)

limiter = Limiter(
    application,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)