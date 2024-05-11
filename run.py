from app import app, db
import os

os.environ['FLASK_APP'] = 'run.py'

if __name__ == '__main__':
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)