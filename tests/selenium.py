import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase

from app import create_app, db
from config import TestConfig
from app.models import User

localHost = "http://localhost:5000/"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
        time.sleep(5) 

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.server_process.terminate()
        self.driver.close()

    def test_login(self):
        self.driver.get(localHost + '/login')
        username = "nonexistent_user"
        password = "wrong_password"

        username_element = self.driver.find_element(By.NAME, "username")
        password_element = self.driver.find_element(By.NAME, "password")
        submit_element = self.driver.find_element(By.NAME, "submit")

        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_element.click()

        messages = self.driver.find_elements(By.CLASS_NAME, "error")
        self.assertEqual(len(messages), 1, "Expected there to be a single error message when trying to login as a non-existent user")
        self.assertEqual(messages[0].text, f'No username found with {username}. Please try again.')
