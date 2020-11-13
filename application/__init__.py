from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)

# Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
Config.SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='postgres',
    pw='123456789',
    url='127.0.0.1:2345',
    db='test-auth-service'
)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes
