from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User, Question, Answer   

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', title='Log In', form=form)
    
    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
        flash(f'No username found with {form.username.data}. Please try again.', 'error')
        return render_template('login.html', title='Log In', form=form)
    
    if not user.check_password(form.password.data):
        flash('Invalid password. Please try again.', 'error')
        return render_template('login.html', title='Log In', form=form)
    
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you signed up successfully!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Singn Up', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/profile/<username>')
@login_required
def profile(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user, posts=posts)