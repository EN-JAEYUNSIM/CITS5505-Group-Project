from app import db, login
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from hashlib import md5
import sqlalchemy.orm as so
import sqlalchemy as sa
from typing import Optional


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, nullable=False, default=datetime.now)
    posts = db.relationship('Post', back_populates='author', lazy='dynamic')
    comments = db.relationship('Comment', back_populates='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.id
    
    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
    def avatar(self, size):
        digest = md5(self.username.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
    
@login.user_loader
def get_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post', order_by='Comment.id')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self) -> str:
        return f'<Post {self.title}>'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author = db.relationship('User', back_populates='comments')
    post = db.relationship('Post', back_populates='comments')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self) -> str:
        return f'<Comment {self.content}>'



