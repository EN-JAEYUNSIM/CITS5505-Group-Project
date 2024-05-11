from flask import render_template, request, redirect, url_for, flash
from app import app,db
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    
    username = form.username.data
    user = User.query.get(username)
    
    if not username :
        flash('Please enter username correctly')
        return render_template('login.html',form=form)

    password = form.password.data
    if not user.check_password(password):
        flash('Invalid password')
        return render_template('login.html', form=form)

    login_user(user)
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    return None


# @app.route('/submit')
# def submit():
#     form = CreatePostForm()
#     if not form.validate_on_submit():
#         return render_template('post.html', form=form)
