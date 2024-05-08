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
        # 登录验证逻辑
        pass
    return render_template('login.html', form=form)

def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 注册逻辑
        pass
    return render_template('register.html', form=form)

def create_request():
    form = PostForm()
    if form.validate_on_submit():
        # 创建帖子逻辑
        pass
    return render_template('create_requests.html', form=form)

def find_requests():
    # 查找帖子逻辑
    pass
