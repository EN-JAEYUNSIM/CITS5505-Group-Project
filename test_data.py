from app import db
from app.models import *

def create_tables():
    db.create_all()
    
def add_users():
    # 创建用户实例
    user1 = User(username='Alice')
    user1.set_password('password123')

    user2 = User(username='Bob')
    user2.set_password('password456')

    # 将用户添加到数据库会话
    db.session.add(user1)
    db.session.add(user2)

    # 提交会话以保存更改到数据库
    db.session.commit()

    print("Users have been added to the database.")
