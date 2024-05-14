from app import app, db
import os

os.environ['FLASK_APP'] = 'run.py'

if __name__ == '__main__':
    app.run(debug=True)