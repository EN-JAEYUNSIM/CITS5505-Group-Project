from faker import Faker
from app import db
from app.modules.models import User, Post, Comment
import random

fake = Faker()

def create_users(count=10):
    for _ in range(count):
        user = User(username=fake.user_name(),
                    email=fake.email(),
                    password_hash='fake_hash',  
                    registered_on=fake.past_date())
        db.session.add(user)
    db.session.commit()

def create_posts(count=10):
    users = User.query.all()
    if users:
        for _ in range(count):
            user = random.choice(users)
            post = Post(title=fake.sentence(),
                        body=fake.text(),
                        posted_on=fake.past_date(),
                        author_id=user.id)
            db.session.add(post)
    db.session.commit()

def create_comments(count=30):
    users = User.query.all()
    posts = Post.query.all()
    if users and posts:
        for _ in range(count):
            user = random.choice(users)
            post = random.choice(posts)
            comment = Comment(body=fake.text(),
                              posted_on=fake.past_date(),
                              author_id=user.id,
                              post_id=post.id)
            db.session.add(comment)
    db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    create_time = db.Column(db.DateTime, server_default=db.func.now())

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    create_time = db.Column(db.DateTime, server_default=db.func.now())

create_users()
create_posts()
create_comments()
