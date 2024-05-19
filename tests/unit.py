import unittest
from app import create_app, db
from app.models import User
from config import TestConfig

from unittest import TestCase

class UserModelCase(TestCase):
    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        u = User(username='john')
        u.set_password('password')
        db.session.add(u)
        db.session.commit()
        self.assertTrue(User.query.filter_by(username='john').first() is not None)

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
