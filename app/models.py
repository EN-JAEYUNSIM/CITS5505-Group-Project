from flask_login import UserMixin
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model,UserMixin):
    username = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password): 
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.username

@login.user_loader
def get_user(username):
    return User.query.get(username)

    
#TO DO: Add more models for the forum
# class Post(db.Model):
    
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     username = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     create_time = db.Column(db.DateTime, server_default=db.func.now())

# class Reply(db.Model):
    
#     content = db.Column(db.Text, nullable=False)
#     post_title = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     username = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     create_time = db.Column(db.DateTime, server_default=db.func.now())
