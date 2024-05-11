from flask import Flask
from .views import index, login, register, create_request, find_requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
