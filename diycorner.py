from app import app, db


def setup_database():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)