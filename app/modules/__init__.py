from flask import Flask
from .views import index, login, register, create_request, find_requests

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/signup', 'register', register, methods=['GET', 'POST'])
    app.add_url_rule('/newRequest', 'create_request', create_request, methods=['GET', 'POST'])
    app.add_url_rule('/find_requests', 'find_requests', find_requests, methods=['GET', 'POST'])

    return app
