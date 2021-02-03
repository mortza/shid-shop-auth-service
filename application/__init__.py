import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from application.config import Config, BASEDIR
from melipayamak import Api
from repository.acceptabledata import AcceptableData

adata = AcceptableData()

load_dotenv()
logging.basicConfig(filename='app.log', filemode='a', level=logging.DEBUG)
app = Flask(__name__)
app.debug = True

Config.SECRET_KEY = os.getenv('SECRET_KEY')

RATE_LIMIT = os.getenv('RATE_LIMIT')

redis_client = FlaskRedis(app)

if os.getenv('DB_TYPE') == 'sqlite':
    Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
elif os.getenv('DB_TYPE') == 'postgres':
    Config.SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=os.getenv('DB_USER'),
        pw=os.getenv('DB_PASSWORD'),
        url=os.getenv('DB_URL'),
        db=os.getenv('DB_NAME')
    )

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)

melipayamak_api = Api(os.getenv('USERNAME_MELIPAYAMAK'), os.getenv('PASSWORD_MELIPAYAMAK'))
sms = melipayamak_api.sms('rest')