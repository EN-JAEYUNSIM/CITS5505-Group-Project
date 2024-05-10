from app import app, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user
import sqlalchemy as sa
from app.models import User
from werkzeug.security import generate_password_hash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/signup')
def signup():
    return render_template('signup.html', title='Sign Up')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/profile')
def profile():
    return render_template('profile.html')