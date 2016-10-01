from flask import Flask
from flask_bcrypt import Bcrypt

from modules.secrets import secrets

app = Flask('bookmark')

app.secret_key = secrets.bookmark_secret

bcrypt = Bcrypt(app)