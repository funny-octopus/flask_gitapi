import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


if not app.debug:
    if not os.path.exists(app.config['LOG_PATH']):
        os.mkdir(app.config['LOG_PATH'])
    file_handler = RotatingFileHandler(
            os.path.join(app.config['LOG_PATH'], 'app.log'),
            maxBytes=10240,
            backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)


from app.api import bp as bp_api
from app.errors import bp as bp_errors


app.register_blueprint(bp_api)
app.register_blueprint(bp_errors)

