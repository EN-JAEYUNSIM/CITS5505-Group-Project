from app import app, db
from flask import render_template, flash, redirect, url_for, request, session
from app.forms import LoginForm, SignupForm, PostForm, CommentForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User, Post, Comment  

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            user = User.query.filter_by(username=login_form.username.data).first()
            if user is None:
                flash(f'No username found with {login_form.username.data}. Please try again.', 'error')
                return render_template('login.html', title='Log In', form=login_form)
            if not user.check_password(login_form.password.data):
                flash('Invalid password. Please try again.', 'error')
                return render_template('login.html', title='Log In', form=login_form)
            
            login_user(user, remember=login_form.remember_me.data)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Please correct errors in the form.', 'error') 
    return render_template('login.html', title='Log In', form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        user = User(username=signup_form.username.data)
        user.set_password(signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you signed up successfully!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Singn Up', form=signup_form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Post(title=post_form.title.data,content=post_form.content.data, author=current_user, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!', 'success')
        return redirect(url_for('details', post_id=post.id, user_id=current_user.id))
    return render_template('post.html', title='Create Post', form=post_form, Legend='Create New Post', user=current_user)    

@app.route('/details/<int:post_id>', methods=['GET', 'POST'])
@login_required
def details(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data, author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment is now live!', 'success')
        return redirect(url_for('details', post_id=post_id, user_id=current_user.id))
    return render_template('details.html', post=post, comments=comments, form=comment_form, user=current_user, comment_form=comment_form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form=PostForm()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('dashboard.html', title='Dashboard', user=current_user, posts=posts, form=form, page=page)

@app.route('/profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(author=user).all()
    comments = Comment.query.filter_by(author=user).all()

    editprofile_form = EditProfileForm()
    if request.method == 'POST' and editprofile_form.validate_on_submit():
        if user == current_user:
            current_user.about_me = editprofile_form.about_me.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('profile', user_id=current_user.id))
    elif request.method == 'GET' and user == current_user:
        editprofile_form.about_me.data = current_user.about_me

    return render_template('profile.html', user=user, posts=posts, comments=comments, form=editprofile_form)

@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    page = request.args.get('page', 1, type=int)
    
    if not keyword:
        flash('Please enter a keyword to search for.', 'error')
        return render_template('search.html', results=[], keyword=keyword, user=current_user)
    
    results = Post.query.filter(
        (Post.title.ilike(f'%{keyword}%') | 
         Post.content.ilike(f'%{keyword}%'))
    ).order_by(Post.date_posted.desc())

    posts = results.paginate(page=page, per_page=4)
    
    if posts.total == 0:
        flash('No results found for your search.', 'error')

    return render_template('search.html', results=posts.items, keyword=keyword, user=current_user, posts=posts)