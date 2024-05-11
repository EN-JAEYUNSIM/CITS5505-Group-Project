from flask import render_template, request, redirect, url_for, flash
from app import db
from .models import User, Post, Comment
from .forms import LoginForm, RegisterForm, PostForm, CommentForm

def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        pass
    return render_template('login.html', form=form)

def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        pass
    return render_template('signup.html', form=form)

def create_request():
    form = PostForm()
    if form.validate_on_submit():
        
        pass
    return render_template('newRequest.html', form=form)

def find_requests():
    
    pass
