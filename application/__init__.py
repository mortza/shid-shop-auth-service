from application.config import Config, BASEDIR
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv
import os
from flask_redis import FlaskRedis

from repository.acceptabledata import AcceptableData

adata = AcceptableData()

load_dotenv()
app = Flask(__name__)
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
