from flask import Flask

app = Flask(__name__)

from app.api import bp as bp_api
from app.errors import bp as bp_errors

app.register_blueprint(bp_api)
app.register_blueprint(bp_errors)

