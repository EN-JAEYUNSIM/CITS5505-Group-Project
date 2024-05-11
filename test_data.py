from app import create_app, db
from app.models import User

app = create_app()

def create_test_users():
    with app.app_context():  # 使用应用上下文
        db.create_all()
        user1 = User(username='Alice')
        user1.set_password('password123')

        user2 = User(username='Bob')
        user2.set_password('password456')

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        
        print("Users have been added to the database.")

if __name__ == "__main__":
    create_test_users()
    app.run(debug=True)